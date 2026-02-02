# House Prices Data Preprocessing Project

## Overview
This project performs end-to-end data preprocessing on the House Prices dataset.

### Steps Included
1. **Data Cleaning:**
   - Missing values handled using median.
   - Outliers treated using IQR.
   - Duplicate and irrelevant records removed.
2. **Categorical Encoding:**
   - One-Hot, Label, Ordinal, Frequency, and Target Encoding applied.
3. **Feature Scaling:**
   - Min-Max, Max-Abs, Z-score, and Normalization demonstrated.
4. **Additional:**
   - Log transformation for skewed target.

### Conclusion
- **Missing Values:** Median imputation performed best since LotArea had skewed distribution.
- **Encoding:**
  - One-Hot worked best for nominal features (e.g., HouseStyle).
  - Label Encoding suited ordinal features.
  - Target Encoding improved correlation for target-related categorical features.
- **Scaling:** Standardization (Z-score) gave stable results across numeric features.
- **Outliers:** IQR-based capping effectively reduced variance without major data loss.

### How to Run
1. Place the dataset file (`train.csv`) into the `dataset/` folder.
2. Run `data_preprocessing.ipynb` using Jupyter Notebook.
3. The preprocessed data will be saved in the same folder.
