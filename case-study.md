# Case study: a claimed proof of the Riemann Hypothesis, checked

Dr Alex (Aco) Kovaceski, AxoQuant. 25 November 2026.

On 20 November 2026 a paper appeared claiming a proof of the Riemann Hypothesis, developed with Claude and formalized in Lean without assumptions. The only public evidence was a Lean archive: 175,187 files, 17.4 million lines, no human-readable proof. The author said he had not mastered the argument.

AxoQuant ran the claim through the Governor, the same process used in production to screen model output. For a mathematical claim the check is the strongest one available: make the Lean kernel accept the entire archive and show the final theorem depends on no axioms.

## What the check found

The static review came back clean. The final theorem states the real thing, using mathlib's own zeta function and its canonical RiemannHypothesis definition. Zero axioms, zero sorry, zero duplication across 17.4 million lines, zero unresolved imports. None of that settles the claim, because elaboration fails in ways no static scan sees.

So we built it. The archive compiled in full with the pinned toolchain and mathlib revision, distributed across the AxoQuant Slurm cluster. On 24 November 2026 the receipt ran:

```
'riemannHypothesis' depends on axioms: [propext, Classical.choice, Quot.sound]
'riemannZeta_eq_zero_re' depends on axioms: [propext, Classical.choice, Quot.sound]
'LFunction_eq_zero_re' depends on axioms: [propext, Classical.choice, Quot.sound]
'LFunction_eq_zero_re_of_isPrimitive' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The three axioms are the standard axioms of Lean's logic, present in every mathlib proof. The claim is verified: a compiled, axiom-clean term of type RiemannHypothesis is a proof of the Riemann Hypothesis, and the three GRH forms follow the same way.

## Why the process exists

The Governor was not designed on paper. It was hardened over more than two years and 500,000 automated development and review cycles inside AxoQuant's trading operation, where a fluent wrong answer costs money. Agents certified their own work, and a second model reviewing the first scored at chance. The fix was to change the task: never ask whether work is good, ask whether the output of a check demonstrates the claim. The jailbreak that followed showed the same failure at the prompt layer, and the answer was the same: a control is something an adversary cannot address, enforced in code before the model is reached.

The Riemann claim is that discipline applied to a public mathematical claim. A fluent claim, an artifact no human can read, and a check that settles it. The enforcement layer is the subject of Australian provisional application 2026907221, filed 23 August 2026, with a PCT international application in preparation.

## The role this creates

The work splits into three jobs. The director steers the machine to the target; Alpöge supplied the analogies and then the machine outran him. The interpreter reads the artifact and writes down what a human can and cannot understand; Slijepčević's 94-page outline and its list of open questions is that job. The third job is new: take a mathematical claim, build a mechanical check that can fail, run it, and publish the receipt. That job is a proof certifier. It did not exist as a job before the artifacts got too big to read.

## The receipts

The review note, the axioms check file, the shard tooling and the fleet build record are public at https://github.com/axoquant/rh-governance-review. Anyone can re-run the check. The arXiv report carries the same receipt. The cluster-shard skill, which distributes this kind of build across the fleet, is published with the repo and is available to every agent on the estate.

Contact: alex@axoquant.com.
