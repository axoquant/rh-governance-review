#!/usr/bin/env python3
"""Per-node shard runner for lake projects.

Usage: run_lake_shard.py <node>
Reads shards/<node>.txt, runs `lake build` over each chunk in order, logs per
chunk. Lake sizes its worker pool from the CPUs it sees; run under slurm with
--cpus-per-task to control it. Stops at the first failed chunk.
"""
import subprocess
import sys


def main():
    node = sys.argv[1]
    chunks = open(f'shards/{node}.txt').read().split('---CHUNK---')
    for i, c in enumerate(chunks):
        mods = [m for m in c.strip().split('\n') if m]
        print(f'=== chunk {i}: {len(mods)} modules ===', flush=True)
        r = subprocess.run(['lake', 'build'] + mods)
        print(f'=== chunk {i} exit {r.returncode} ===', flush=True)
        if r.returncode != 0:
            sys.exit(r.returncode)


if __name__ == '__main__':
    main()
