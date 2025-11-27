# 🎓 Admit Predict  
**Project Title:** Identifying Key Factors in College Admissions  
**Team Name:** Admit Predict  

---

## 🚀 Getting Started for New Collaborators  

Welcome to the **Admit Predict** project! 🎉  
Follow these quick steps to get your environment ready and start contributing:

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Mamasmess333/Admit_Predict.git
cd Admit_Predict
```

### 2️⃣ Install Git LFS (Large File Support)  
If you’ve never used Git LFS before, run:  
```bash
git lfs install
git lfs pull
```
> This ensures you download the large dataset files (`.csv`, `.xlsx`) from GitHub.

### 3️⃣ Set Up Your Python Environment  
We recommend Python 3.10+ (via venv, conda, or VS Code).  
Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn openpyxl scikit-learn scipy
```

### 4️⃣ Open the EDA Notebook  
In VS Code or Jupyter Lab:  
```
College_Scorecard_Most_Recent_Institutional_Data/Notebooks/01_EDA.ipynb
```

This notebook walks through:
- Dataset structure and schema  
- Missing-data analysis  
- Data dictionary lookups  
- Duplicate detection  

### 5️⃣ Collaborate and Contribute  
Create your own branch for new work (e.g., `feature-cleaning`):  
```bash
git checkout -b feature-cleaning
```
When ready to merge, open a Pull Request to the `main` branch.  
Please commit often and use clear messages (e.g., `"Added correlation heatmap for numeric variables"`).

---

## 🧠 Project Overview  

Getting into college has always been competitive, but few applicants understand *what truly drives admission decisions*.  
Our project, **Admit Predict**, uses supervised machine learning to uncover and model the key factors that most influence college acceptance rates across U.S. institutions.  

We analyze institutional-level data to identify relationships between:  
- **Academic metrics** (GPA, SAT/ACT scores)  
- **Institutional selectivity** (admission rate, faculty ratio)  
- **Demographics** (gender, ethnicity, income distributions)  
- **Financial factors** (average aid, average debt, Pell Grant percentages)  

The goal is to train regression models (Linear Regression, Decision Trees, k-Nearest Neighbors) to predict **admission rates** (ADM_RATE) at the institutional level and identify which factors most strongly influence admission decisions, making the admissions landscape more transparent.

**Problem Type**: Regression (predicting continuous admission rate 0-1)  
**Target Variable**: `ADM_RATE` (institutional admission rate)  
**Final Dataset**: 827 institutions, 11 features

---

## 🧩 Current Project Structure  

```
Admit_Predict/
│
├── College_Scorecard_Most_Recent_Institutional_Data/
│   ├── Data_Assets/
│   │   ├── Most-Recent-Cohorts-Institution.csv
│   │   ├── collegescorecarddatadictionary.xlsx
│   │   ├── college_scorecard_clean.csv
│   │   ├── college_scorecard_reduced.csv
│   │   └── college_scorecard_enriched.csv   # Scorecard + IPEDS + FSA features from Notebook 01
│   │
│   ├── Notebooks/
│   │   ├── 01_EDA.ipynb
│   │   ├── 02_Preprocessing_and_Modeling.ipynb
│   │   ├── 03_Explainability_and_Conclusions.ipynb
│   │   └── 04_Model_QA_and_Defense.ipynb
│   │
│   └── Outputs/
│       └── Cell_block_ouput/
│
├── .gitattributes
├── .gitignore
└── README.md
```

---

## 📦 Data Sources  

### **1. College Scorecard (U.S. Department of Education)**  
- **Description:** Admissions rates, test scores, costs, demographics  
- **Link:** [College Scorecard Dataset](https://catalog.data.gov/dataset/college-scorecard)  
- **Files:**  
  - `Most-Recent-Cohorts-Institution.csv`  
  - `collegescorecarddatadictionary.xlsx`

- **Description:** Institution-level demographics (gender/race), Pell recipients, federal loan uptake, net price by income.  
- **Link:** [IPEDS Custom Data Files](https://nces.ed.gov/ipeds/use-the-data)  
- **Files:**  
  - `Data_Assets/external/ipeds/CSV_11262025-608/ipeds_final_2023.csv` (Final Release 2023 custom pull)  
- **Join Key:** `UNITID` (also provides `OPEID` for consistency with Scorecard/FSA).

### **3. Federal Student Aid Data Center (FSA)**  
- **Description:** Institution-level Pell/TEACH/Iraq-Afghanistan grant totals plus Direct Loan program volumes.  
- **Files:**  
  - `22-23 Pell Grants/pell_grants_ay2022_2023_fullyear.csv` (stitched Q1–Q4 Pell/TEACH/IASG recipients + disbursements)  
  - `Data_Assets/external/fsa/dl_dashboard_ay2022_2023_fullyear.csv` (stitched Direct Loan dashboard totals)  
- **Join Key:** `OPEID` (padded to 8 digits to align with Scorecard).

### **4. U.S. Census Bureau (optional)**  
- Regional income and education data for socioeconomic context

---

## ⚙️ Setup Instructions  

(If you already followed **Getting Started**, skip this section.)

1. **Clone the repo**
   ```bash
   git clone https://github.com/Mamasmess333/Admit_Predict.git
   cd Admit_Predict
   ```

2. **Pull LFS files**
   ```bash
   git lfs pull
   ```

3. **Install dependencies**
   ```bash
   pip install pandas numpy matplotlib seaborn openpyxl scikit-learn scipy
   ```

4. **Run the EDA Notebook**
   Explore dataset structure, missingness, and duplicates.

---

## 🔍 Project Progress So Far  

| Task | Status | Description |
|------|---------|-------------|
| Repository setup | ✅ | Project folders + LFS configuration |
| Core dataset acquisition | ✅ | Downloaded from College Scorecard |
| Data dictionary | ✅ | Added and linked |
| Git LFS setup | ✅ | Large files handled efficiently |
| **Step 1: EDA** | ✅ | Structure, missingness, duplicates, feature selection |
| **Step 2: Feature Reduction** | ✅ | Reduced to 20 features (Scorecard + IPEDS + Pell/Loan aggregates) |
| **Step 3: Preprocessing** | ✅ | Train/test split, encoding, scaling |
| **Step 4: Modeling** | ✅ | 3 models: Linear Regression, Decision Tree, kNN |
| **Step 4: Hyperparameter Tuning** | ✅ | GridSearchCV for Decision Tree and kNN |
| **Step 4: Evaluation** | ✅ | MAE, RMSE, R², residual plots, model comparison |
| **Step 5: Explainability** | ✅ | Feature importance, coefficients, permutation importance |
| **Step 6: Conclusions** | ✅ | Model recommendation, limitations, next steps |

### 📊 Model Performance Summary
- **Best Model**: kNN (Tuned) – Test RMSE: **0.1576**, Test R²: **0.5615**, Test MAE: **0.1262**
- **Dataset**: 610 institutions, 20 features (Scorecard + IPEDS + FSA Pell/Loan totals)
- **Train/Test Split**: 488 train / 122 test (80/20)

---

## 👩‍💻 Next Steps for Teammates  

1. `git pull origin main` → `git lfs pull`  
2. Run notebooks in order:
   - `01_EDA.ipynb` - Exploratory data analysis and feature selection
   - `02_Preprocessing_and_Modeling.ipynb` - Data preprocessing and model building
   - `03_Explainability_and_Conclusions.ipynb` - Feature importance and final conclusions
   - `04_Model_QA_and_Defense.ipynb` - Oral defense prep, overfitting checks, FAQs
3. Review model outputs and feature importance insights
4. Document findings and push updates with clear commits

### 📚 Notebook Workflow
1. **Notebook 1 (EDA)**: Loads Scorecard + IPEDS + FSA Pell/Loan → cleans/merges → exports `college_scorecard_enriched.csv`
2. **Notebook 2 (Modeling)**: Loads enriched data → preprocesses → trains/tunes models → evaluates
3. **Notebook 3 (Explainability)**: Analyzes best model → feature importance → conclusions  

---

## 🧠 Collaboration Guidelines  

- **Data files are handled via Git LFS** — don’t manually upload datasets.  
- **Use clear commit messages.** Example: `"Added correlation matrix and boxplots"`.  
- **Keep notebooks numbered** sequentially: `01_EDA.ipynb`, `02_Cleaning.ipynb`, etc.  
- **Avoid pushing large raw outputs** unless necessary.  

---

## 📚 References  

- [College Scorecard Data Documentation](https://collegescorecard.ed.gov/data/documentation/)  
- [IPEDS Data Center](https://nces.ed.gov/ipeds/)  
- [Federal Student Aid Data Center](https://studentaid.gov/data-center)  
- [U.S. Census Bureau Income Dataset](https://tinyurl.com/Household-income)

---

## 📄 License & Acknowledgments  

This project was developed for educational purposes under the **Georgia State University Data Science Project (Fall 2025)**.  
Data provided by the **U.S. Department of Education**, **IPEDS**, and **Federal Student Aid**.  
All rights to the data remain with their respective owners.  

---
