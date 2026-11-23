# Fleet build record: RH archive, 23 November 2026

How the archive build was distributed. Kept as the worked example behind the cluster-shard skill.

## Numbers

- Archive: 175,187 Lean files, 17.4M lines, 1.03 GB source
- Pins: leanprover/lean4:v4.33.1, mathlib 0df444a360eaa60ab8c11dca51a86af692955474
- Built state at freeze: 93,293 oleans. Remaining: 81,893 modules, of which Development 77,555
- Cluster: dr-nefario, idc-1..idc-6 under one slurm partition

## Shards

Weighted by worker budget per node (about 6 GB RAM per lean worker, headroom for co-resident jobs):

| Node | Workers | Modules |
|---|---|---|
| idc-3 | 16 | 18,311 |
| idc-4 | 16 | 13,905 |
| idc-5 | 16 | 13,761 |
| idc-6 | 16 | 13,752 |
| idc-2 | 8 | 6,740 |
| idc-1 | 4 | 3,412 |
| dr-nefario | 14 | 12,012 |

Main and Supplements.Kernels reserved for the closing pass on dr-nefario.

## Procedure

1. Freeze: stop the local build, snapshot the state
2. Toolchain: elan + lean4 v4.33.1 installed user-local on every node
3. Ship: parallel rsync of src, .lake/packages, .lake/build/lib to each node (about 67 GB each). Exclude .lake/build/ir, which is discardable
4. Submit: one sbatch per node, pinned with --nodelist, --cpus-per-task set to the worker count, --mem about 6.5 GB per worker
5. Run: cluster-shard/scripts/run_lake_shard.py <node> <jobs>, chunks of 4,000 modules per lake invocation
6. Merge: rsync finished oleans back to dr-nefario as shards complete
7. Close: lake build Main on dr-nefario, then lake env lean GovernorCheck.lean for the receipt

## Incidents

- The single-box build filled the root filesystem. .lake/build/ir held 620 GB of .setup.json environment dumps. Deleting ir outputs from one built module and re-running lake showed the module is skipped: the dumps are not resume state. Deleted, kept the 50 GB of oleans.
- Two harness-side kills of the detached build were survived by restarting from oleans. The detached pattern used throughout: setsid nohup bash -c 'cmd >> log 2>&1' >/dev/null 2>&1 &
- A pkill pattern matched its own command line once. All kill patterns use bracket regex now, e.g. v4[.]33[.]1/bin/lake
- lake cache get fails if any dep lacks reservoir outputs at the pinned rev for the toolchain (Cli did). Dropped the cache route and built mathlib from source
