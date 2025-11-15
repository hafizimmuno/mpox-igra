# igrascript.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import mannwhitneyu

DATA_PATH = "data/synthetic_igra.csv"

def load_data(path=DATA_PATH):
    df = pd.read_csv(path)
    return df

def summary_stats(df):
    print("N total:", len(df))
    print(df['Group'].value_counts())
    print("\nGroup IFN-γ summary:")
    print(df.groupby('Group')['IFN_gamma_IU_per_mL'].describe())

def run_test(df):
    vac = df[df['Group']=='Vaccinated']['IFN_gamma_IU_per_mL']
    ctrl = df[df['Group']=='Control']['IFN_gamma_IU_per_mL']
    u_stat, p_value = mannwhitneyu(ctrl, vac, alternative='two-sided')
    print(f"\nMann-Whitney U: {u_stat:.2f}, p-value: {p_value:.4f}")
    return u_stat, p_value

def compute_cutoff(df):
    ctrl = df[df['Group']=='Control']['IFN_gamma_IU_per_mL']
    mean_ctrl = ctrl.mean()
    sd_ctrl = ctrl.std(ddof=1)
    cutoff = mean_ctrl + 2 * sd_ctrl
    print(f"\nControl mean: {mean_ctrl:.4f}, SD: {sd_ctrl:.4f}, cutoff (mean+2SD): {cutoff:.4f}")
    return cutoff

def sensitivity_specificity(df, cutoff):
    df['positive'] = df['IFN_gamma_IU_per_mL'] >= cutoff
    vac = df[df['Group']=='Vaccinated']
    ctrl = df[df['Group']=='Control']
    sens = vac['positive'].sum() / len(vac) if len(vac)>0 else np.nan
    spec = 1 - (ctrl['positive'].sum() / len(ctrl)) if len(ctrl)>0 else np.nan
    print(f"\nSensitivity: {sens:.3f}, Specificity: {spec:.3f}")
    return sens, spec

def plot_figures(df, p_value):
    sns.set(style="whitegrid")
    # Figure 1: boxplot + strip
    plt.figure(figsize=(6,5))
    ax = sns.boxplot(x='Group', y='IFN_gamma_IU_per_mL', data=df)
    sns.stripplot(x='Group', y='IFN_gamma_IU_per_mL', data=df, color='black', size=6)
    plt.title('IFN-γ Response (synthetic data)')
    plt.ylabel('IFN-γ (IU/mL)')
    plt.text(0.5, df['IFN_gamma_IU_per_mL'].max()*0.9, f'p = {p_value:.3f}', ha='center')
    plt.tight_layout()
    plt.savefig('figure1.png', dpi=300)
    plt.close()

    # Figure 2: anticoagulant & peptide summary (use thesis-like medians for illustration)
    anticoagulants = ['EDTA', 'Lithium Heparin']
    anticoag_vals = [0.052, 0.154]  # illustrative medians (thesis-like)
    peptide_conc = [0.1, 1.0, 2.0]
    peptide_vals = [0.071, 0.154, 0.152]  # illustrative from validation summary

    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,4))
    ax1.bar(anticoagulants, anticoag_vals)
    ax1.set_title('Anticoagulant comparison (median IFN-γ)')
    ax1.set_ylabel('IFN-γ (IU/mL)')

    ax2.plot(peptide_conc, peptide_vals, marker='o')
    ax2.set_title('Peptide concentration (median IFN-γ)')
    ax2.set_xlabel('Concentration (µg/mL)')
    ax2.set_ylabel('IFN-γ (IU/mL)')

    plt.tight_layout()
    plt.savefig('figure2.png', dpi=300)
    plt.close()
    print("\nSaved figure1.png and figure2.png")

def main():
    df = load_data()
    summary_stats(df)
    u_stat, p_value = run_test(df)
    cutoff = compute_cutoff(df)
    sensitivity_specificity(df, cutoff)
    plot_figures(df, p_value)

if __name__ == "__main__":
    main()
