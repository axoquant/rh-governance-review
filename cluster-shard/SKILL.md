---
name: cluster-shard
description: Distribute large deterministic compute jobs across the AxoQuant slurm cluster. Use when a task's estimated single-box runtime exceeds about 2 hours, when build state or data exceeds about 50 GB, when a user asks to "use the cluster" or "fast track" a long build, or when sharding work across the fleet nodes (dr-nefario, idc-1..idc-6). Covers probing the cluster, freezing a consistent snapshot, weighted hash sharding, parallel rsync, sbatch submission, incremental sync-back, and the final verification receipt on the coordinator.
---

# Cluster-shard

Split a large, deterministic job across the AxoQuant slurm cluster. One coordinator (usually dr-nefario) plans and merges; the fleet builds.

## Trigger check

Use this pattern when any of: single-box ETA over roughly 2 hours, more than roughly 1,000 independent units, build state or data over roughly 50 GB, or the user asks to use the cluster or fast track. If the job cannot be split into independent deterministic units, say so instead of forcing it.

## Hard rules

1. Probe the scheduler before touching anything. `sinfo -N -l`, `squeue`, and `uptime` per node. Trust Slurm's CPU/MEM numbers over nproc/free. The node set changes; never reuse a node table from memory.
2. All work goes through `sbatch`. Never ssh onto a fleet box to run an unscheduled job. Pin placement with `--nodelist` or `--exclude`.
3. Respect stated exclusions. Standing rule: work on idc-1 and idc-2 goes through slurm only, no raw ssh jobs. Change this only if the user says so.
4. Freeze before distributing. Stop the source build, take one consistent snapshot, sync that. Never distribute a moving target.
5. Shard by content hash (md5 of the unit name) with weights proportional to each node's worker budget: RAM divided by per-worker peak, minus headroom for the node's other jobs. Reserve the final target and its last-mile modules for the coordinator's closing pass.
6. Deterministic outputs make overlap harmless. Same toolchain, same inputs, identical artifacts. A node building a module assigned elsewhere costs a little duplication, never corruption. Design so the closing pass rebuilds anything any node failed to finish; missing remote work is slower, never wrong.
7. Detach everything: `setsid nohup bash -c 'cmd >> log 2>&1' >/dev/null 2>&1 &` on every box, including the coordinator.
8. Kill patterns must not match their own command line. Use a bracket regex, e.g. `pkill -TERM -f 'v4[.]33[.]1/bin/lake'`.
9. Ship only what matters. Before moving or deleting hundreds of GB, identify the real resume state and verify empirically with a one-unit test. In this fleet, build intermediates have dwarfed the artifacts that matter.
10. Chunk argument lists under ARG_MAX: about 4,000 unit names per build invocation.
11. The verification receipt is part of the pattern. After the merge, run the project's real check on the coordinator. A distributed build with no final verification is not done.
12. Watch disk throughout. A full filesystem kills the build and the box's other work.

## Workflow

1. Estimate whether the trigger applies. Get the user's node constraints in writing (which boxes are off limits, whether slurm-only counts as allowed).
2. Probe: `sinfo -N -l`, `squeue`, per-node `uptime` and writable paths (`/data` vs home). Build the node table: CPUs, RAM, current load, worker budget, destination path.
3. Freeze: stop the source build. Snapshot the state.
4. Generate shards with `scripts/shard_units.py`. Reserve the closing modules first.
5. Toolchain: install user-local (elan or equivalent) on each participating node if missing.
6. Ship: parallel rsync of the snapshot to each node. Exclude known junk. Watch transfer rates.
7. Submit: one `sbatch` per node, `--nodelist=<node> --cpus-per-task=<workers> --mem=<workers*peak+margin> --job-name=<name>`, running the shard runner detached, logging per node.
8. Monitor through `squeue` and the per-node logs, not by pinging boxes. Sync finished shards back to the coordinator incrementally.
9. When all shards are in: run the closing pass on the coordinator (reserved modules plus any stragglers), then the verification receipt.
10. Report: what ran where, per-node stats, the receipt output.

## Bundled tools

- `scripts/shard_units.py`: weighted hash shard generator. Takes a project dir, the unit extension, the built-state directory, node weights, reserve patterns, and chunk size. Writes per-node shard files with `---CHUNK---` separators.
- `scripts/run_lake_shard.py`: per-node runner for Lean projects. Runs `lake build -j N` over each chunk in the node's shard file, logs per chunk, exits non-zero only if the last chunk fails.

## Lean builds

For lake/Lean specifics (olean resume state, discardable intermediates, cache fallback, worker RAM), read `references/lean-builds.md`.
