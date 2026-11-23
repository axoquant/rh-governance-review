# Lean / lake build facts

Learned on the RH formalization build (175k files, 17.4M lines). Apply to any lake project.

## Resume state

- The only state a lake build needs to resume is `.olean` files under `.lake/build/lib/lean/` (plus the `.lake/packages` dep builds). Everything else under `.lake/build/ir/` (`.setup.json`, `.c`, `.hash`) is intermediate and discardable.
- Proof: lake skips a module whose `ir/` outputs were deleted while its `.olean` remains. Verify with a one-module test before mass deletion. The `ir/` dumps ran about 7.8 MB per module on this project and were 12x the size of the oleans.
- Oleans are deterministic per (toolchain version, source, dep oleans). Shards on different nodes cannot corrupt each other. Cross-node overlap only duplicates work.
- Toolchain pins: `lean-toolchain` file pins `leanprover/lean4:vX.Y.Z`. Install identically on every node with elan (`~/.elan/bin`).

## Dependencies

- Pin deps with `lake-manifest.json`. `lake build` auto-fetches at manifest revs. Never run `lake update` before a build you intend to compare across nodes; it can move revs.
- Try `lake cache get` (reservoir) first for dep oleans. If a dep has no cached outputs at the pinned rev for the toolchain (e.g. `Cli`), `lake cache get` fails the whole fetch; drop the cache route and build deps from source. `lake build` does not auto-fetch cache.
- Dep builds live in `.lake/packages/<dep>/.lake`. Sync that whole tree to each node.

## Running

- About 6 GB RAM peak per lean worker. Budget workers per node as floor((slurm MEM * 0.8) / 6.5GB), then trim for the node's current load.
- `lake build -j N` inside the chunk runner. Chunk module lists to about 4,000 names per invocation (ARG_MAX).
- Big elaboration needs `--tstack=400000` in lakefile `moreLeanArgs`; some projects set `maxHeartbeats` high. Keep the project's own settings.
- Run detached: `setsid nohup bash -c 'lake build Main >> build.log 2>&1' >/dev/null 2>&1 &`. Session loss must not kill it.
- Kill safely: `pkill -TERM -f 'v4[.]33[.]1/bin/lake'` (bracket regex so the pattern does not match the killing shell).
- Module-name targets work for any `lean_lib`: `lake build Module.Name`.

## Verifying

- The receipt for a proof claim: `lake env lean GovernorCheck.lean` containing `#print axioms <theorem>` for every final theorem. Empty axiom list is the pass. Any axiom, sorry, or compile error fails the claim.
- A module built on one node and rsynced back is accepted by lake on the coordinator without rebuild (same toolchain).
- Lake's step counter is a moving plan, not a total. Measure progress by counting `.olean` files, not by the `[n/m]` in the log.
