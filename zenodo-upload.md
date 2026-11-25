# Zenodo upload package: An independent machine check of a claimed Riemann Hypothesis proof

Everything needed to publish the verified receipt on Zenodo with a DOI. Give this to the browser agent along with the PDF at `publish/arxiv/note.pdf` in the Investigation workspace.

## Steps for the browser agent

1. Go to https://zenodo.org and log in. GitHub or ORCID both work. If no account exists, create one.
2. Click the "+" menu, then "New upload".
3. Attach the PDF: `publish/arxiv/note.pdf` (3 pages, 48 KiB). Resource type: **Publication → Preprint**.
4. Fill in the fields below exactly, then click **Publish**. A DOI is issued immediately.

## Fields

**Title**
An independent machine check of a claimed Riemann Hypothesis proof

**Authors**
Dr Alex (Aco) Kovaceski (AxoQuant, Kovacorp Pty Ltd, Canberra, ACT)

**Publication date**
25 November 2026

**Description (abstract)**
A paper posted at https://alpo.ge/remark.pdf claims a proof of the Riemann Hypothesis, developed with Claude and formalized in Lean without assumptions. The only public evidence is a Lean archive of 175,187 files and 17.4 million lines. This report records an independent check of that claim. The archive was statically screened, compiled from source with the pinned toolchain and mathlib revision across a Slurm cluster, and the four final theorems were examined for axiom dependencies. The final theorems depend only on the standard axioms of Lean's logic (propext, Classical.choice, Quot.sound). The claim is verified. The receipt and reproduction commands are published alongside this note. Independently corroborated by Michael Rubinstein (University of Waterloo), including a replay through Lean's kernel and a check by the independent nanoda kernel.

**Keywords**
Riemann Hypothesis, Lean, formal verification, proof assistants, axiom audit, independent verification, mathematical proof, machine-generated mathematics

**Licence**
Creative Commons Attribution 4.0 International (CC BY 4.0)

**Subjects / categories**
cs.LO (Logic in Computer Science), math.NT (Number Theory)

**Related identifiers**
- GitHub repository (check file, review notes, shard tooling, build record): https://github.com/axoquant/rh-governance-review
- Case study on axoquant.com: https://axoquant.com/case-study-riemann.html
- Source claim paper: https://alpo.ge/remark.pdf
- Source Lean archive: https://alpo.ge/lean.tar.gz.part01 .. part14
- Independent verification by Michael Rubinstein: https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/

**Notes**
The three axioms listed are the standard axioms of Lean's underlying logic (propositional extensionality, the axiom of choice, quotient soundness), present in every mathlib proof. No custom axioms, no sorry, no interface assumptions. A compiled, axiom-clean term of type RiemannHypothesis is a proof of the Riemann Hypothesis, and the three GRH forms follow the same way.

## After publishing

Record the DOI here and link it back into the GitHub repo README and the axoquant.com case study. Submit the same source to arXiv in parallel for the long-term index (cs.LO primary, math.NT cross-list).
