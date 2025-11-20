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
pip install pandas numpy matplotlib seaborn openpyxl scikit-learn pytz tzdata threadpoolctl scipy
```
Or using the Python launcher on Windows:
```bash
py -m pip install pandas numpy matplotlib seaborn openpyxl scikit-learn pytz tzdata threadpoolctl scipy
```

### 4️⃣ Run the Notebooks in Order  
In VS Code or Jupyter Lab, run notebooks sequentially:

1. **`01_EDA.ipynb`** - Exploratory Data Analysis
   - Dataset structure and schema  
   - Missing-data analysis  
   - Data dictionary lookups  
   - Duplicate detection
   - Univariate and bivariate visualizations

2. **`02_Feature_Engineering.ipynb`** - Feature Selection & Preprocessing
   - Feature selection (correlation, mutual information)
   - Missing value imputation
   - Categorical encoding
   - Feature scaling
   - Train/test split

3. **`03_Modeling.ipynb`** - Model Building & Evaluation
   - Linear Regression (baseline)
   - Decision Tree Regressor
   - k-Nearest Neighbors Regressor
   - Support Vector Regressor
   - Hyperparameter tuning
   - Model comparison and evaluation  

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

The goal is to train models such as Logistic Regression and Decision Trees to predict admission likelihood and make the admissions landscape more transparent.

---

## 🧩 Current Project Structure  

```
Admit_Predict/
│
├── College_Scorecard_Most_Recent_Institutional_Data/
│   ├── Data_Assets/
│   │   ├── Most-Recent-Cohorts-Institution.csv
│   │   ├── collegescorecarddatadictionary.xlsx
│   │
│   ├── Notebooks/
│   │   ├── 01_EDA.ipynb                    # Exploratory Data Analysis
│   │   ├── 02_Feature_Engineering.ipynb    # Feature Selection & Preprocessing
│   │   └── 03_Modeling.ipynb               # Model Building & Evaluation
│   │
│   ├── Outputs/
│   │   └── Cell_block_output/
│   │       └── cell_block1.txt
│
├── NEXT_STEPS_ANALYSIS.md                  # Analysis of EDA and next steps
├── PROJECT_COMPLETION_CHECKLIST.md          # Project requirements checklist
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

### **2. Federal Student Aid Data Center (optional)**  
- Pell Grant and loan statistics for financial-aid analysis  
- Merge later via `OPEID`

### **3. U.S. Census Bureau (optional)**  
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
   pip install pandas numpy matplotlib seaborn openpyxl scikit-learn pytz tzdata threadpoolctl scipy
   ```
   Or on Windows:
   ```bash
   py -m pip install pandas numpy matplotlib seaborn openpyxl scikit-learn pytz tzdata threadpoolctl scipy
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
| **Phase 3: Data Understanding** | | |
| Initial EDA | ✅ | Structure, missingness, duplicates, visualizations complete |
| Feature selection | ✅ | Reduced to 25 features using correlation & mutual information |
| Data cleaning | ✅ | Missing value imputation, encoding, scaling complete |
| **Phase 4: Modeling** | | |
| Baseline model | ✅ | Linear Regression implemented |
| Decision Tree | ✅ | With hyperparameter tuning (GridSearchCV) |
| k-Nearest Neighbors | ✅ | With hyperparameter tuning |
| Support Vector Regressor | ✅ | With hyperparameter tuning |
| Model evaluation | ✅ | Cross-validation, metrics (MAE, RMSE, R²) |
| Feature importance | ✅ | Coefficients, importances, permutation importance |
| Model comparison | ✅ | Comprehensive comparison and visualization |
| **Phase 5: Communication** | | |
| Final report | 🔜 | PDF report needed |
| Presentation | 🔜 | 12-15 minute presentation needed |

---

## 👩‍💻 Next Steps for Teammates  

1. `git pull origin main` → `git lfs pull`  
2. Run notebooks in order: `01_EDA.ipynb` → `02_Feature_Engineering.ipynb` → `03_Modeling.ipynb`
3. Review `PROJECT_COMPLETION_CHECKLIST.md` for remaining tasks
4. **Remaining work:**
   - Add Naive Bayes model (required for probability-based category)
   - Write final PDF report
   - Create presentation slides (12-15 minutes)
5. Document findings and push updates with clear commits.

## 📋 Project Status

**Current Completion: ~70%**

✅ **Completed:**
- Complete EDA with comprehensive visualizations
- Feature engineering and preprocessing pipeline
- 4 regression models with hyperparameter tuning
- Model evaluation and comparison
- Feature importance analysis

⚠️ **Remaining:**
- Naive Bayes model (required)
- Final PDF report (25 points)
- Presentation (30 points)

See `PROJECT_COMPLETION_CHECKLIST.md` for detailed requirements.  

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
