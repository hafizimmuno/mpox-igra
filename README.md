# **Mpox IGRA Optimization Pipeline**

Python-based workflow developed as part of a research project at the **Institute of Tropical Medicine (ITM), Antwerp**, focused on optimizing an **Interferon-Gamma Release Assay (IGRA)** to evaluate T-cell responses following **MVA-BN Mpox vaccination**.

---

## **Project Overview**

This repository contains a self-contained analysis pipeline demonstrating:

- Cleaning and preprocessing of IFN-γ ELISA values  
- Statistical comparison between vaccinated vs. non-vaccinated individuals  
- Exploration of IGRA cutoff values  
- Generation of publication-style figures  
- A simplified demonstration dataset for reproducibility  

The dataset is anonymized and derived from a methodological IGRA optimization study performed during a Master's thesis (Jan–Jul 2025).

---

## **Repository Contents**

### **1. `igrascript.py`**
Core analysis script including:

- Data import and structure  
- Preprocessing and filtering  
- Non-parametric statistical testing (e.g., Mann–Whitney U)  
- Visualization (boxplots, dose-response curves)  
- Export of figures (`figure1.png`, `figure2.png`)

### **2. `figure1.png`**
Example visualization showing IFN-γ responses between study groups.

### **3. `figure2.png`**
Peptide titration curve illustrating the optimal antigen stimulation dose.

---

## **Peptide Concentration Behavior**

In antigen-specific stimulation assays, peptide-driven IFN-γ responses usually increase with rising concentration until reaching an optimal dose (here ~1.0 µg/mL).  
Beyond this point, responses may decline due to:

- Oversaturation of T-cell receptors  
- Reduced signaling efficiency  
- Early functional exhaustion  

This **“high-dose hook effect”** is commonly observed in ELISpot, ICS, and IGRA-type functional assays.  
The provided titration curve demonstrates this non-linear behavior.

---

## **Methods Summary**

- **Assay:** Interferon-Gamma Release Assay (IGRA)  
- **Readout:** IFN-γ ELISA  
- **Sample type:** Whole blood or PBMC stimulation  
- **Statistics:** Mann–Whitney U and related non-parametric tests  
- **Language:** Python  

---

## **Installation**

```bash
git clone https://github.com/hafizimmuno/mpox-igra
cd mpox-igra
pip install -r requirements.txt

## **Running the Script**

```bash
python igrascript.py

Running the Script
python igrascript.py

## Outputs

- `figure1.png` — IFN-γ comparison between groups  
- `figure2.png` — Peptide dose–response curve  

Figures are automatically saved in the project directory.

---

## Requirements

See `requirements.txt` for the full list of dependencies.

---

## License

Released under the **MIT License** — free for academic and scientific use.

---

## Contact

For questions or collaboration: **hafiz-hassan.ahmad@etu.univ-lyon1.fr**

