# Publish the verification on the two claim-tracking dashboards

Give this to the browser agent. Two targets: the community verification log and the riemann-rev dashboard. Both take primary sources, which is exactly what we have.

## 1. Community verification log

Site: https://riemannhypothesisclaude.org/verification-log

Mechanism: the site's **About and corrections** page accepts new sources. It prefers primary sources (build logs, the author's own notes, expert posts, preprints), which is what my repo and DOI are.

Do this:

1. Open https://riemannhypothesisclaude.org/verification-log and find the **About and corrections** link (in the page footer or the About section).
2. Submit a new entry with the text below, and attach the links.

Text to submit:

> Independent build and axiom audit by Dr Alex (Aco) Kovaceski (AxoQuant), 24 November 2026. The full archive of 175,187 Lean modules compiled with the pinned toolchain (leanprover/lean4:v4.33.1) and mathlib revision 0df444a360eaa60ab8c11dca51a86af692955474, with zero errors, across a Slurm cluster. #print axioms on all four final theorems shows only propext, Classical.choice and Quot.sound. No sorry, no custom axioms, no interface assumptions. Static review: statement matches mathlib's canonical RiemannHypothesis, zero sorry/admit/axiom/unsafe in 17.4M lines, zero unresolved imports, 14 duplicate files of 175,187. Sources: GitHub repo with check file and reproduction commands (https://github.com/axoquant/rh-governance-review), arXiv PDF in the same repo (arxiv/note.pdf), citable record with DOI (https://zenodo.org/records/24519677), case study (https://axoquant.com/case-study-riemann.html).

## 2. riemann-rev dashboard (Bartosz Naskręcki)

Repo: https://github.com/nasqret/riemann-rev (dashboard at https://nasqret.github.io/riemann-rev/)

Mechanism: it is a GitHub repo, so submit a GitHub issue with the verification details and links. Use the same GitHub account as the repo pushes (alexkovaceski).

Do this:

1. Open https://github.com/nasqret/riemann-rev/issues and click **New issue**.
2. Title: `Independent build + axiom audit by AxoQuant (Kovaceski), 24 November 2026`
3. Body: the same text as above, plus the links.
4. Submit.

## Notes

- Both venues record independent builds and axiom audits, which is exactly what this is.
- The five-theorem wording: the Lean and Mathlib joint statement certifies RH; the GRH theorems cover Dirichlet L-functions only. My check covers the four final theorems in Main.lean (RH plus the three GRH forms). Do not overstate the scope beyond that.
- The receipt ran on 24 November 2026 on the cluster; the static review is dated 25 November 2026.
