#!/usr/bin/env python3
"""Weighted hash shard generator for cluster-shard.

Splits unbuilt units across nodes so each node's share is proportional to its
worker budget. Units whose module does not start with --stem-prefix go to the
first node (the strongest), which keeps small cross-cutting subtrees together.
"""
import argparse
import hashlib
import os


def modules_built(built_dir):
    out = set()
    for root, _dirs, files in os.walk(built_dir):
        for f in files:
            if f.endswith('.olean'):
                out.add(os.path.relpath(os.path.join(root, f), built_dir)[:-6].replace('/', '.'))
    return out


def modules_total(src_dir, ext):
    out = []
    for root, _dirs, files in os.walk(src_dir):
        for f in files:
            if f.endswith(ext):
                out.append(os.path.relpath(os.path.join(root, f), src_dir)[:-len(ext)].replace('/', '.'))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--project', required=True)
    ap.add_argument('--src-dir', default='src')
    ap.add_argument('--ext', default='.lean')
    ap.add_argument('--built-dir', default='.lake/build/lib/lean')
    ap.add_argument('--workers', required=True, help='node=weight,node=weight,... (first node is strongest)')
    ap.add_argument('--reserve', default='', help='comma-separated module prefixes kept off the shards for the closing pass')
    ap.add_argument('--stem-prefix', default='Development.')
    ap.add_argument('--chunk', type=int, default=4000)
    ap.add_argument('--outdir', default='shards')
    args = ap.parse_args()

    os.chdir(args.project)
    workers = [w.split('=') for w in args.workers.split(',')]
    nodes = [w[0] for w in workers]
    weights = {w[0]: int(w[1]) for w in workers}
    total_w = sum(weights.values())

    built = modules_built(args.built_dir)
    reserves = [r for r in args.reserve.split(',') if r]
    remaining = [m for m in modules_total(args.src_dir, args.ext)
                 if m not in built and not any(m == r or m.startswith(r) for r in reserves)]

    shards = {n: [] for n in nodes}
    for m in remaining:
        if not m.startswith(args.stem_prefix):
            shards[nodes[0]].append(m)
            continue
        h = int(hashlib.md5(m.encode()).hexdigest(), 16) % total_w
        acc = 0
        for n in nodes:
            acc += weights[n]
            if h < acc:
                shards[n].append(m)
                break

    os.makedirs(args.outdir, exist_ok=True)
    for n in nodes:
        lst = shards[n]
        chunks = [lst[i:i + args.chunk] for i in range(0, len(lst), args.chunk)]
        with open(os.path.join(args.outdir, f'{n}.txt'), 'w') as fh:
            for c in chunks:
                fh.write('\n'.join(c) + '\n---CHUNK---\n')
        print(f'{n} {len(lst)} modules, {len(chunks)} chunks', flush=True)
    print(f'reserved off shards: {len(reserves)} patterns', flush=True)


if __name__ == '__main__':
    main()
