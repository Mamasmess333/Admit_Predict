# 📊 Project Review Summary: Notebooks 1–4

## 🔄 Guideline vs. Project Description Crosswalk

| Source Requirement | Status | Evidence / Notes |
|--------------------|--------|------------------|
| Guideline Step 1 (EDA) | ✅ | `01_EDA.ipynb` covers schema (6,429×3,306 raw), missingness plots, duplicate/anomaly checks, and target definition (`ADM_RATE`). |
| Guideline Step 2 (≤20 features & drop high correlation) | ✅ | Corr/MI filters cap predictors at 20 (Scorecard + IPEDS + FSA). `ACTCMMID`/`TUITIONFEE_IN` removed when |r| ≥ 0.85. |
| Guideline Step 3 (preprocessing & splits) | ✅ | Notebook 2 performs 80/20 split, numeric scaling, and one-hot encoding for `CONTROL`, `HIGHDEG`, `REGION`. |
| Guideline Step 4 (≥2 models + tuning + CV) | ✅ | Linear Regression, Decision Tree, kNN run with MAE/RMSE/R². GridSearchCV tunes tree + kNN with 5-fold CV RMSE tracking. |
| Guideline Step 5 (explainability & diagnostics) | ✅ | Notebook 2 residual plots; Notebook 3 covers coefficients, tree importances, permutation importance, and comparison chart. |
| Guideline Step 6 (Conclusions/defense) | ✅ | Notebook 4 documents pipeline narrative, evaluation metric definitions, mutual information, p-values, and FAQ responses. |
| Project description emphasis on classification | ⚠️ Partial | Current data best supports regression on `ADM_RATE`. README/Notebook 4 explain rationale and note future option to binarize for logistic regression if labels become available. |
| Project description data sources (Scorecard + IPEDS + FSA + Census) | ✅ / 🔜 | Scorecard, IPEDS, Pell, Direct Loan integrated. Census socioeconomic context listed as next enrichment opportunity. |

---

## ✅ What's Working Well

- **End-to-end flow**: Notebook 1 exports `college_scorecard_enriched.csv` (610 institutions, 20 predictors + target) consumed by Notebooks 2–4 without reloading raw Scorecard later.  
- **Feature discipline**: Combination of missingness filters, correlation checks, and mutual information keeps ≤20 interpretable variables aligned with the rubric.  
- **Model coverage**: Linear Regression, Decision Tree, and kNN baselines, plus tuned variants, satisfy “3 models + comparisons” requirement.  
- **Explainability assets**: Feature importances, coefficients, permutation importance, and textual summaries are ready for presentations/defense.  
- **Bonus classification context**: Logistic regression on selective (≤50% ADM_RATE) vs accessible campuses delivers Accuracy 0.93, Precision 0.95, Recall 0.74, F1 0.83, ROC AUC 0.87 for oral defense talking points without new datasets.

---

## 📓 Notebook Findings Snapshot

| Notebook | Highlights | Guideline Coverage |
|----------|------------|--------------------|
| `01_EDA.ipynb` | Cleans Scorecard, merges IPEDS 2023 + Pell & Direct Loan aggregates, drops sparse columns, enforces ≤20 features, outputs enriched CSV. | Steps 1–2 |
| `02_Preprocessing_and_Modeling.ipynb` | 80/20 split, scaling, GridSearchCV, MAE/RMSE/R² table, residual diagnostics, model comparison plots, plus optional logistic regression lens (ADM_RATE ≤ 0.50). | Steps 3–4 (+ bonus classification) |
| `03_Explainability_and_Conclusions.ipynb` | Linear coefficients, tree importances, permutation importance, cross-model feature comparison, storyline + recommended model write-up. | Step 5 |
| `04_Model_QA_and_Defense.ipynb` | Defense brief: pipeline recap, concept glossary (metrics, MI, p-values, one-hot columns), anticipated questions, three effective models with trade-offs. | Step 6 |

---

## ⚠️ Issues Found & Fixed

1. **Multiple `df = pd.read_csv(...)` calls wiping merged columns** – Notebook 1 now loads Scorecard once, then sequentially merges IPEDS + Pell + Direct Loans so `selected_features` exist downstream.  
2. **Overly strict merge validation** – Pell & Direct Loan merges switched to `validate="many_to_one"` to accommodate branch campuses sharing `OPEID`.  
3. **High-correlation duplicates** – Automated filter retains the higher-target-correlation member of each |r| ≥ 0.85 pair (`ACTCMMID`, `TUITIONFEE_IN`).  
4. **Emoji-related encoding errors in scripts** – Removed emojis from `pell_stitch.py` / `fsa_stitch.py` print statements to prevent `UnicodeEncodeError`.  
5. **xlrd dependency gaps** – Added `xlrd` installation note so `.xls` quarterly files read successfully.

---

## 📈 Model Performance Analysis

### Best Model: **kNN (Tuned)** 🏆

| Metric | Value |
|--------|-------|
| **Test RMSE** | **0.1576** |
| **Test R²** | **0.5615** |
| **Test MAE** | **0.1262** |
| **CV RMSE (5-fold)** | 0.1526 |
| **Hyperparameters** | `n_neighbors=25`, `weights='distance'`, `p=1` |

**Why it wins**
- Lowest test RMSE and highest R² among all candidates  
- Cross-validation RMSE close to holdout RMSE → limited overfitting  
- Distance-weighted Manhattan neighborhood captures regional & financial gradients better than Euclidean default

### Model Ranking (by Test RMSE)
1. **kNN (Tuned)** – RMSE 0.1576, R² 0.5615  
2. **Decision Tree (Tuned)** – RMSE 0.1636, R² 0.5274  
3. **Linear Regression** – RMSE 0.1637, R² 0.5269  
4. **kNN (Default)** – RMSE 0.1651, R² 0.5187  
5. **Decision Tree (Default)** – RMSE 0.2191, R² 0.1523 (overfit)

### Key Observations
- Default Decision Tree memorizes training set (R²=1.0) but fails on test; tuning depth/leaves resolves variance.  
- Linear Regression remains a transparent baseline with competitive error, useful for presentations even if not best RMSE.  
- Train/test vs CV agreement indicates preprocessing + feature set are stable; no major leakage detected.

---

## 🔧 Improvements Applied This Pass

1. **Documentation sync** – README + this summary updated with 610×20 dataset stats, notebook findings, and best-model metrics so all deliverables match Notebook outputs.  
2. **Crosswalk transparency** – Added explicit rubric vs project description table to show compliance and call out the regression-vs-classification nuance for graders.  
3. **Defense-readiness evidence** – Notebook highlights now reference where evaluation metrics, mutual information, p-values, regional encodings, one-hot columns, and the new logistic classification metrics are explained.  
4. **Future-facing guidance** – Next enrichment (Census socioeconomic context, potential multi-threshold classification beyond the ≤50% view) is noted to satisfy project description aspirations.

---

## ✅ Alignment Checklist

| Requirement | Status | Notes |
|-------------|--------|-------|
| EDA completed | ✅ | Scorecard + IPEDS + FSA merged; schema/missingness/duplicates documented |
| ≤20 features | ✅ | Exactly 20 predictors retained with rationale |
| Train/test split | ✅ | 80/20 with random_state=42 |
| Encoding & scaling | ✅ | StandardScaler for numeric, OneHotEncoder for categorical |
| ≥3 models | ✅ | Linear Regression, Decision Tree, kNN |
| Hyperparameter tuning | ✅ | GridSearchCV (DT & kNN) |
| Cross-validation | ✅ | 5-fold CV RMSE reported |
| Regression metrics | ✅ | MAE, RMSE, R² |
| Residual plots | ✅ | Notebook 2 includes residual vs predicted, hist, QQ, actual vs predicted |
| Model comparison | ✅ | Table + bar charts + CV boxplot |
| Explainability artifacts | ✅ | Coefficients, tree importances, permutation importance |
| Defense readiness | ✅ | Notebook 4 concept glossary + FAQ |

---

## 📝 Summary

The project now fully mirrors the professor’s six-step guide while honoring the Admit Predict problem statement:
- **Data pipeline**: Stable enriched dataset (Scorecard + IPEDS + Pell + Direct Loan) with stitched quarterly files and reproducible scripts.  
- **Modeling**: Three comparable models with tuning, diagnostics, and clear evidence favoring tuned kNN for accuracy vs simplicity trade-offs.  
- **Explainability**: Multiple complementary views (coefficients, feature importances, permutation) to answer “why” questions.  
- **Documentation**: README and this summary highlight notebook findings, metrics, and next steps (Census enrichment, optional expansion of the new classification lens).  
  
Future enhancement: incorporate Census socioeconomic context and/or explore alternate admission-rate thresholds (e.g., top quartile selectivity) to extend the existing logistic lens if deliverables require additional classification detail.

