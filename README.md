# COX-2 Docking Analysis

## Comparative Analysis of COX-2 Inhibitors using Molecular Docking and Multi-Metric Evaluation

This project analyzes how different anti-inflammatory drugs interact with the COX-2 enzyme using molecular docking. The study compares Paracetamol, Aspirin, and Celecoxib based on binding energy, residue interactions, and drug-likeness properties.

---

## 📁 Repository Structure

```
COX2-Docking-Analysis/
│
├── data/
│   └── dataset.csv           # Drug binding energy and properties dataset
│
├── code/
│   └── analysis.py           # Python script for drug ranking analysis
│
├── images/
│   ├── paracetamol.png       # Docking interaction of Paracetamol with COX-2
│   ├── aspirin.png           # Docking interaction of Aspirin with COX-2
│   └── celecoxib.png         # Docking interaction of Celecoxib with COX-2
│
├── results/
│   └── results_summary.txt   # Summary of docking results
│
├── paper/
│   └── conference_paper.pdf  # Full conference paper
│
├── README.md
└── requirements.txt
```

---

## 🧪 Methods

- **Tool:** AutoDock Vina
- **Protein:** COX-2 (from RCSB Protein Data Bank)
- **Ligands:** Paracetamol, Aspirin, Celecoxib (from PubChem)
- **Protein Preparation:** UCSF Chimera

---

## 📊 Results

| Drug        | Binding Energy (kcal/mol) | H-Bonds | Residues | MW    | Score  |
|-------------|---------------------------|---------|----------|-------|--------|
| Paracetamol | -6.0                      | 1       | 2        | 151.2 | Low    |
| Aspirin     | -6.4                      | 2       | 2        | 180.1 | Medium |
| Celecoxib   | -7.0                      | 3       | 3        | 381.3 | High   |

**Celecoxib** showed the strongest binding affinity (-7.0 kcal/mol), consistent with its design as a selective COX-2 inhibitor.

---

## 🖼️ Docking Visualizations

### Paracetamol
![Paracetamol Docking](images/paracetamol.png)

### Aspirin
![Aspirin Docking](images/aspirin.png)

### Celecoxib
![Celecoxib Docking](images/celecoxib.png)

---
---
## Team & Contributions

Bharath R – Data Collection  
Vedhachalam M (24BCB0107) – Paper Presentation  
Roopesh G A – GitHub & Coding 
---

## ▶️ How to Run

```bash
pip install -r requirements.txt
cd code
python analysis.py
```

---

## 📄 Paper

See [`paper/conference_paper.pdf`](paper/conference_paper.pdf) for the full write-up.

---

## 🔗 References

1. Trott & Olson, AutoDock Vina, *J. Computational Chemistry*, 2010.
2. PubChem Database: https://pubchem.ncbi.nlm.nih.gov
3. RCSB Protein Data Bank: https://www.rcsb.org
4. UCSF Chimera: https://www.cgl.ucsf.edu/chimera/
