# Governing a machine claim: the alpo.ge Riemann Hypothesis archive, reviewed

Dr Alex (Aco) Kovaceski

24 November 2026

## Summary

A paper posted at alpo.ge claims a proof of the Riemann Hypothesis, worked out with Claude, and says the arguments are formalized in Lean without assumptions. The only public evidence is a Lean archive in 14 parts.

I ran the claim through the Governor process AxoQuant uses in production: extract the falsifiable claims, build a mechanical check for each, and refuse to pass anything the check does not demonstrate. The check for this claim is the strongest one mathematics has: make the Lean kernel accept the entire archive and show the final theorem depends on no axioms.

This note records what was checked, what was found, and the receipt.

## The claim

From remark.pdf:

1. A proof of the Riemann Hypothesis has been discovered.
2. The arguments are formalized in Lean without assumptions.
3. The method resolves the Generalized Riemann Hypothesis.

The paper states the human readable version would run 250,000 pages and declines to publish it. The archive is the argument.

## The artifact

175,187 Lean files, 17.4 million lines, 1.03 GB of source. For scale, mathlib is about 7,000 files. Pinned to lean4 v4.33.1 and one mathlib commit.

## Checks that ran before the build

Statement integrity. Verified. The final theorem in src/Main.lean has type RiemannHypothesis. At the pinned mathlib commit that name is the canonical statement: every nontrivial zero of the Riemann zeta function has real part 1/2. No shadow definition of the zeta function exists in the archive.

Unsoundness sweep. Verified statically. Zero occurrences of axiom, constant, sorry, admit, unsafe, implemented_by or opaque in 17.4 million lines. No declaration injecting elaborator.

Vacuity sweep. Verified at the traced nodes. The statements carrying the proof hold real mathematical content. None is defined as True.

Wiring integrity. Verified. 753,569 internal imports, zero unresolved.

Duplication. 14 duplicate files out of 175,187.

None of these checks settles the claim. Elaboration fails in ways no static scan sees. The compiler is the instrument.

## The build

The archive was built from source with the pinned toolchain and pinned mathlib. The build was distributed across the AxoQuant slurm cluster: seven nodes, 90 workers, hash sharded, with the closing pass and the receipt run on the coordinator.

Two operational findings worth recording. The build state is the compiled oleans, about 50 GB. The environment dumps lake also produces, 620 GB of them, are discardable, proven by deleting them from one module and watching lake skip it. And a full filesystem kills a build exactly the way any other resource exhaustion does: one module failed with no space left on device before the disk was cleaned and the build resumed.

## The receipt

Run on idc-3, 24 November 2026, after the full archive compiled with lean4 v4.33.1 and the pinned mathlib revision. `lake env lean GovernorCheck.lean`:

```
'riemannHypothesis' depends on axioms: [propext, Classical.choice, Quot.sound]
'riemannZeta_eq_zero_re' depends on axioms: [propext, Classical.choice, Quot.sound]
'LFunction_eq_zero_re' depends on axioms: [propext, Classical.choice, Quot.sound]
'LFunction_eq_zero_re_of_isPrimitive' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The three axioms listed are the standard axioms of Lean's underlying logic (propositional extensionality, the axiom of choice, quotient soundness), present in every mathlib proof. No custom axioms, no sorry, no interface assumptions.

## What the role is called

The work splits into three jobs. The director steers the machine to the target. The interpreter reads the artifact and writes down what a human can and cannot understand. The third job is new: take a mathematical claim, build a mechanical check that can fail, run it, and publish the receipt. That job is a proof certifier. In the case study it is also an assayer: the person who tests what a claimed proof is made of. It did not exist as a job before the artifacts got too big to read.

## Verdict

Verified. The archive compiles in full with the pinned toolchain and mathlib revision, and the four final theorems depend only on the standard logical axioms. The final theorem is mathlib's canonical statement of the Riemann Hypothesis. A compiled, axiom-clean term of that type is a proof of the Riemann Hypothesis, and the same holds for the three GRH forms. The claim in remark.pdf is demonstrated, not just asserted.

## Reproduction

```
git clone <this repo>
# toolchain
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y
elan toolchain install leanprover/lean4:v4.33.1
# source archive
# fetch lean.tar.gz.part01 .. part14 from https://alpo.ge, cat into lean.tar.gz, extract
cd lean && lake build Main
lake env lean GovernorCheck.lean
```

The shard tooling lives in cluster-shard/ and the fleet procedure in docs/cluster-run.md.

## Links

- Claim paper: https://alpo.ge/remark.pdf
- Claim archive: https://alpo.ge/lean.tar.gz.part01 .. part14
- This repo: https://github.com/axoquant/rh-governance-review
- Zenodo record (DOI): https://zenodo.org/records/24519677
- AxoQuant Governor whitepaper: [URL]
