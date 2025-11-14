# mpox-igra
Python pipeline for IGRA optimization in Mpox vaccine responses (IFN-γ cytokine data) – Master's thesis, ITM Antwerp
# Mpox IGRA Optimization Pipeline

Master's thesis project at ITM Antwerp (Jan–Jul 2025): Optimized Interferon-Gamma Release Assay (IGRA) for monitoring T-cell responses to MVA-BN Mpox vaccination.

## Summary
- n=14 participants (6 vaccinated, 8 controls)
- IFN-γ levels: Median 0.19 IU/mL (vaccinated) vs 0.00 IU/mL (controls), p=0.04
- Optimized: Lithium heparin anticoagulant + 1 μg/mL orthopox peptide pool
- Code: Python for data analysis and visualization

## Files
- `igrascript.py`: Python code for data analysis, cutoff optimization, and figure generation (uses pandas, scipy, seaborn, matplotlib)
- `figure1.png`: Boxplot of IFN-γ response pre/post-vaccination
- `figure2.png`: Optimization curve for anticoagulant and peptide concentration

## Methods
- PBMC isolation, ELISA for IFN-γ
- Statistical analysis: Mann-Whitney U test
- Code availability: Open-source under MIT License

Preprint: Ahmad, H.H. et al. (2025). Optimizing IGRA for Mpox vaccine monitoring. bioRxiv (submitted)

Contact: hafiz-hassan.ahmad@etu.univ-lyon1.fr
