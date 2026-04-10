##Comparative Analysis of COX-2 Inhibitors using Molecular Docking


#Description

This project analyzes how different anti-inflammatory drugs interact with the COX-2 enzyme using molecular docking. The drugs considered are Paracetamol, Aspirin, and Celecoxib.

Docking was performed using AutoDock Vina, and multiple parameters such as binding energy, interaction with amino acid residues, and drug properties were evaluated. The results show that Celecoxib has the strongest binding affinity compared to the other drugs.

This project demonstrates the use of computational methods for fast and cost-effective drug analysis and highlights the importance of bioinformatics in drug discovery.


Team & Contributions//


Bharath R – Data Collection

Vedhachalam M  – Paper Presentation

Roopesh G A – GitHub Maintenance

Institution

Vellore Institute of Technology, Vellore, India
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
