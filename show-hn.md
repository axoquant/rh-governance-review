# Show HN submission package (revised)

Give this to the browser agent along with an HN login. The verified receipt, the DOI and all three publication links are ready.

## Steps for the agent

1. Go to https://news.ycombinator.com and log in (or create an account).
2. Click **submit** in the top nav.
3. Title: `Show HN: I independently verified a claimed Riemann Hypothesis proof`
4. URL: `https://axoquant.com/case-study-riemann.html`
5. Leave the text field empty (the link carries the post) and submit.
6. Immediately post the top-level comment below as the author.
7. Record the thread URL when it exists and link it from the repo README and the case study.

## Top-level comment

```
I built the full Lean archive Alpöge published for his Riemann Hypothesis claim (175,187 files, 17.4M lines) with the pinned toolchain and checked axiom dependencies on the four final theorems. All four depend only on the standard axioms of Lean's logic (propext, Classical.choice, Quot.sound). The claim is verified.

Michael Rubinstein at Waterloo independently got the same result, including a replay through Lean's kernel and a check by a second independent kernel (nanoda) of 1.48M declarations with no errors.

The 250,000-page figure in the original footnote was a joke, as Alpöge later clarified. The archive itself is machine-checked and holds.

Check file, review notes, shard tooling and the fleet build record: https://github.com/axoquant/rh-governance-review
arXiv PDF: same repo, arxiv/note.pdf
Citable record (DOI): https://zenodo.org/records/24519677
Case study: https://axoquant.com/case-study-riemann.html
The role this creates (the proof certifier): https://acokovaceski.com/writing/the-assayer.html

Happy to answer how the build was distributed across the Slurm cluster and why a static review alone cannot settle a claim like this.
```

## Notes for the agent

- Post during US morning hours if possible.
- Do not ask for upvotes or use second accounts.
- The pitch is the check, not the hype: a 175k-file archive, a full build, an axiom receipt, and an independent second kernel.
- If a commenter asks for the proof itself, point them to the arXiv PDF and the Zenodo record, not to the 1.4 GB archive directly; the reproduction commands in the repo fetch it from alpo.ge.
