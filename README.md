# Mpox IGRA Optimization Pipeline

Python workflow developed as part of a research project at the Institute of Tropical Medicine (ITM), Antwerp, focused on optimizing an Interferon-Gamma Release Assay (IGRA) to evaluate T-cell responses following MVA-BN (Mpox) vaccination.

---

## Project Overview
This repository contains a small, self-contained analysis pipeline demonstrating:

- Data cleaning and preprocessing (IFN-γ ELISA values)  
- Statistical comparison between groups  
- Cutoff exploration  
- Plot generation for IGRA response visualization  

The project uses anonymized example data derived from a methodological IGRA optimization study performed during a Master’s thesis (Jan–Jul 2025).

---

## Files Included

**`igrascript.py`**  
Python script demonstrating:

- Data import and structure  
- Basic statistical workflow (e.g., non-parametric testing)  
- Visualization using boxplots and simple line graphs  
- Export of figures (`figure1.png`, `figure2.png`)

**`figure1.png`**  
Example visualization of IFN-γ responses.

**`figure2.png`**  
Example optimization curve exploring assay parameters.

Peptide Concentration Behavior

During antigen stimulation assays, peptide-specific IFN-γ responses typically follow a non-linear pattern. Increases in peptide concentration enhance T-cell activation up to an optimal point (here ~1.0 µg/mL). Beyond this dose, stimulation may decline due to antigen oversaturation, reduced T-cell receptor signaling efficiency, or early exhaustion-like effects. This “high-dose hook” or “prozone-like” behavior is commonly observed in functional T-cell assays and is illustrated in the peptide titration curve included in this pipeline

---

## Methods Summary

- **Assay:** Interferon-Gamma Release Assay (IGRA)  
- **Cytokine measurement:** IFN-γ ELISA  
- **Sample type:** Whole blood / PBMC stimulation  
- **Statistics:** Non-parametric tests (e.g., Mann–Whitney U)

The code is provided for demonstration and reproducibility purposes.

---

## Environment & Dependencies
The analysis uses:

- Python 3.9+  
- pandas  
- scipy  
- matplotlib  
- seaborn  

---

## License

This repository is open-source under the MIT License.

---

## Contact

For questions or collaboration:
hafiz-hassan.ahmad@etu.univ-lyon1.fr
