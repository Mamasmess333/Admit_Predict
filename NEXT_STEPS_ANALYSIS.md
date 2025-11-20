# 📊 EDA Notebook Analysis & Next Steps

## ✅ What's Already Complete in `01_EDA.ipynb`

### Phase 1: Data Structure & Quality ✅
- ✅ Dataset loaded and shape analyzed (6429 rows, 3306 columns)
- ✅ Data dictionary integrated and schema merged
- ✅ Data type conversion completed (integer, float, string)
- ✅ Invalid values handled (PrivacySuppressed, NULL, NaN)
- ✅ Missingness analysis with visualizations (bar chart, heatmap)
- ✅ Columns with >90% missingness dropped
- ✅ Duplicate rows checked and removed
- ✅ Numeric anomaly detection

### Phase 2: Target & Initial Feature Selection ✅
- ✅ **Target variable defined:** `ADM_RATE` (Admission Rate)
- ✅ **13 features pre-selected:**
  - `SAT_AVG`, `ACTCMMID` (test scores)
  - `COSTT4_A`, `TUITIONFEE_IN` (costs)
  - `UGDS_WHITE`, `UGDS_BLACK`, `UGDS_HISP`, `UGDS_ASIAN` (demographics)
  - `CONTROL`, `HIGHDEG`, `REGION` (institutional)
  - `PCTPELL`, `DEBT_MDN` (financial aid)

### Phase 3: Exploratory Visualizations ✅
- ✅ Univariate analysis: Histograms for numeric, bar charts for categorical
- ✅ Bivariate analysis: Scatter plots (SAT vs ADM_RATE, Tuition vs ADM_RATE)
- ✅ Bivariate analysis: Box plots (CONTROL vs ADM_RATE, REGION vs ADM_RATE)
- ✅ Correlation matrix created

---

## 🔜 What Needs to Be Done in `02_Feature_Engineering.ipynb`

### Task 1: Formal Feature Selection & Justification
**Status:** ⚠️ Features are pre-selected but need formal justification

**What to do:**
1. **Check for highly correlated pairs** (|r| >= 0.85)
   - From the correlation matrix, identify redundant features
   - Example: If `COSTT4_A` and `TUITIONFEE_IN` are highly correlated, keep only one
   - Document which one you keep and why

2. **Rank features by correlation with target**
   ```python
   # Calculate correlation with ADM_RATE
   target_corr = df_corr.corr()['ADM_RATE'].abs().sort_values(ascending=False)
   print(target_corr)
   ```

3. **Use mutual information** (optional but recommended)
   ```python
   from sklearn.feature_selection import mutual_info_regression
   mi_scores = mutual_info_regression(X, y, random_state=42)
   ```

4. **Create feature selection table**
   | Feature | Kept? (Y/N) | Reason | Preprocessing Needed? |
   |---------|-------------|--------|----------------------|
   | SAT_AVG | Y | Strong negative correlation with ADM_RATE | Scale |
   | ... | ... | ... | ... |

5. **Final feature count check**
   - Current: 13 features ✅ (under 20 limit)
   - Document before/after if you remove any redundant ones

---

### Task 2: Handle Remaining Missing Values
**Status:** ⚠️ Missingness analyzed but not handled for modeling

**What to do:**
1. **Check missing values in selected features**
   ```python
   missing_in_features = X.isna().sum()
   print(missing_in_features)
   ```

2. **Decide on strategy for each feature:**
   - **Impute:** Use median/mean for numeric, mode for categorical
   - **Drop rows:** If missing is minimal (<5%)
   - **Drop feature:** If missing is excessive (>50%) and not critical

3. **Implement imputation**
   ```python
   from sklearn.impute import SimpleImputer
   # For numeric features
   imputer = SimpleImputer(strategy='median')
   X_imputed = imputer.fit_transform(X_numeric)
   ```

---

### Task 3: Encode Categorical Variables
**Status:** ❌ Not done yet

**What to do:**
1. **Identify categorical features:**
   - `CONTROL` (1=Public, 2=Private Non-Profit, 3=For-Profit)
   - `REGION` (categorical codes)
   - `HIGHDEG` (degree level)

2. **One-hot encode nominal categories**
   ```python
   X_encoded = pd.get_dummies(X, columns=['CONTROL', 'REGION', 'HIGHDEG'], drop_first=True)
   ```
   - Use `drop_first=True` to avoid multicollinearity

3. **Consider ordinal encoding** if order matters (e.g., HIGHDEG might be ordinal)

---

### Task 4: Scale Numeric Features
**Status:** ❌ Not done yet

**What to do:**
1. **Standardize numeric features** (required for Logistic Regression, kNN, SVM)
   ```python
   from sklearn.preprocessing import StandardScaler
   scaler = StandardScaler()
   X_scaled = scaler.fit_transform(X_numeric)
   ```
   - **Important:** Fit on training set only, then transform both train and test

2. **Note:** Decision Trees and Naive Bayes don't require scaling, but it's good practice to scale anyway for consistency

---

### Task 5: Train/Test Split
**Status:** ❌ Not done yet

**What to do:**
1. **Create train/test split**
   ```python
   from sklearn.model_selection import train_test_split
   X_train, X_test, y_train, y_test = train_test_split(
       X_final, y, 
       test_size=0.2, 
       random_state=42,
       stratify=None  # Use stratify=y if converting ADM_RATE to categories
   )
   ```

2. **Check class distribution** (if doing classification)
   ```python
   print("Train distribution:", y_train.value_counts())
   print("Test distribution:", y_test.value_counts())
   ```

3. **Handle class imbalance** if present:
   - Use stratified split
   - Or use class weights in models
   - Or use resampling (SMOTE, etc.)

---

### Task 6: Final Feature Matrix Preparation
**Status:** ⚠️ Partially done

**What to do:**
1. **Combine all preprocessing steps:**
   - Imputed numeric features
   - Encoded categorical features
   - Scaled features

2. **Create final feature matrix**
   ```python
   # Combine numeric (scaled) and categorical (encoded)
   X_final = np.hstack([X_numeric_scaled, X_categorical_encoded])
   # Or use pandas
   X_final = pd.concat([X_numeric_scaled_df, X_categorical_encoded_df], axis=1)
   ```

3. **Verify final shape and data types**
   ```python
   print(f"Final feature matrix shape: {X_final.shape}")
   print(f"Target shape: {y.shape}")
   print(f"Missing values: {X_final.isna().sum().sum()}")
   ```

---

## 📝 Recommended Structure for `02_Feature_Engineering.ipynb`

```python
# Cell 1: Load cleaned data from EDA
import pandas as pd
import numpy as np
from sklearn.feature_selection import mutual_info_regression
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

# Load the cleaned dataframe (or reload and apply same cleaning)
df = pd.read_csv("../Data_Assets/Most-Recent-Cohorts-Institution.csv", dtype=str)
# ... apply same cleaning steps from 01_EDA ...

# Cell 2: Feature Selection - Check Correlations
# - Identify highly correlated pairs
# - Rank by correlation with target
# - Use mutual information
# - Create feature selection table

# Cell 3: Handle Missing Values
# - Check missing in selected features
# - Impute or drop

# Cell 4: Encode Categorical Variables
# - One-hot encode CONTROL, REGION, HIGHDEG

# Cell 5: Scale Numeric Features
# - Standardize all numeric features

# Cell 6: Train/Test Split
# - Split with appropriate parameters
# - Check distributions

# Cell 7: Final Feature Matrix
# - Combine all preprocessed features
# - Verify shape and quality
# - Save preprocessed data (optional)
```

---

## 🎯 Summary: What's Next

1. ✅ **EDA is complete** - Great foundation!
2. 🔜 **Create `02_Feature_Engineering.ipynb`** with:
   - Formal feature selection justification
   - Missing value handling
   - Categorical encoding
   - Feature scaling
   - Train/test split
3. 🔜 **Then move to `03_Modeling.ipynb`** for model building

---

## 💡 Key Decisions Needed

1. **Regression vs Classification?**
   - Current target: `ADM_RATE` (continuous 0-1)
   - **Option A:** Keep as regression (predict exact admission rate)
   - **Option B:** Convert to classification (e.g., High/Low admission rate)
   - **Recommendation:** Start with regression, can convert later if needed

2. **Which features to keep?**
   - Current 13 features look good
   - Need to check for redundancy (highly correlated pairs)
   - Document why each is kept

3. **Missing value strategy?**
   - Check actual missing % in the 13 selected features
   - Decide: impute vs drop vs drop feature

---

## ✅ Checklist for `02_Feature_Engineering.ipynb`

- [ ] Load and verify cleaned data from EDA
- [ ] Check correlations between features (remove if |r| >= 0.85)
- [ ] Rank features by correlation with target
- [ ] Create feature selection justification table
- [ ] Handle missing values (impute/drop)
- [ ] One-hot encode categorical variables
- [ ] Scale numeric features
- [ ] Create train/test split
- [ ] Verify final feature matrix quality
- [ ] Document all decisions and rationale



