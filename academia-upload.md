# Academia.edu upload instructions: two papers

Give this to the browser agent along with the academia.edu login (or have the user log in themselves first). Two papers, both compiled PDFs in `publish/papers/`.

## Steps (repeat for each paper)

1. Go to https://www.academia.edu/upload/document and log in if asked.
2. Attach the PDF listed below.
3. Fill in the title, abstract, and keywords for that paper, then publish.
4. Record the resulting URL and link it back into the repo README.

## Paper 1: the verification report

**File**: `publish/papers/paper1-verification.pdf` (3 pages, 48 KiB)

**Title**: An independent machine check of a claimed Riemann Hypothesis proof

**Author**: Dr Alex (Aco) Kovaceski, AxoQuant (Kovacorp Pty Ltd), Canberra, ACT

**Date**: 26 November 2026

**Abstract**: A paper posted at https://alpo.ge/remark.pdf claims a proof of the Riemann Hypothesis, developed with Claude and formalized in Lean without assumptions. The only public evidence is a Lean archive of 175,187 files and 17.4 million lines. This report records an independent check of that claim. The archive was statically screened, compiled from source with the pinned toolchain and mathlib revision across a Slurm cluster, and the four final theorems were examined for axiom dependencies. The final theorems depend only on the standard axioms of Lean's logic (propext, Classical.choice, Quot.sound). The claim is verified. The receipt and reproduction commands are published alongside this note. Independently corroborated by Michael Rubinstein (University of Waterloo), including a replay through Lean's kernel and a check by the independent nanoda kernel.

**Keywords**: Riemann Hypothesis, Lean, formal verification, proof assistants, axiom audit, independent verification, mathematical proof

**Subject areas**: Computer Science (Logic in Computer Science), Mathematics (Number Theory)

## Paper 2: the new role

**File**: `publish/papers/paper2-proof-certifier.pdf` (3 pages, 35 KiB)

**Title**: The proof certifier: a new role in machine-generated mathematics

**Author**: Dr Alex (Aco) Kovaceski, AxoQuant (Kovacorp Pty Ltd), Canberra, ACT

**Date**: 26 November 2026

**Abstract**: On 20 November 2026 a paper claimed a proof of the Riemann Hypothesis, developed with Claude. The only public evidence was a Lean archive of 175,187 files and 17.4 million lines. No human can read that archive. This note argues that the episode marks a split in the mathematician's job. The director steers the machine to the target. The interpreter reads the artifact and explains what a human can understand. A third job is new: the proof certifier, who takes a claim, builds a mechanical check that can fail, runs it, and publishes the receipt. That job did not exist before the artifacts got too big to read. The scarce human input does not move: taste in targets, and judgement about what a proof ought to be. The machine supplies volume. What changes is who certifies the result.

**Keywords**: proof certifier, mathematical practice, formal verification, machine-generated mathematics, assurance, Lean, role of the mathematician

**Subject areas**: Mathematics, Computer Science, Philosophy of Science

## After publishing

Record both URLs and link them into the repo README and the axoquant.com case study. The same two sources go to arXiv (cs.LO primary, math.NT cross-list) when the queue is worth the wait, and the Zenodo record at https://zenodo.org/records/24519677 already carries the verification report.
