\# **Assignment 4 — Supervised Machine Learning (Housing Price Prediction)**



&nbsp;***Author***

\*\*Kopparthi Thanmai Sri\*\*  

Roll No: 24341A4254  

College: GMR Institute of Technology (GMRIT)



---



**Project Overview**

This project predicts \*\*house prices\*\* using supervised machine learning algorithms.  

The dataset used is `housing.csv`, which contains features such as area, bedrooms, bathrooms, and amenities.



---



&nbsp;**Step 1 — Data Preprocessing**

\- Handled missing values using `SimpleImputer`.

\- Encoded categorical features using `LabelEncoder` / `OneHotEncoder`.

\- Scaled numerical features using `StandardScaler`.

\- Split the dataset into \*\*80% training\*\* and \*\*20% testing\*\* sets.



---

&nbsp;**Step 2 — Models Used**

1\. \*\*Linear Regression\*\*  

2\. \*\*Decision Tree Regressor\*\*  

3\. \*\*Random Forest Regressor\*\*  

4\. \*\*KNN Regressor\*\*  

5\. \*\*SVM Regressor\*\*



---



**Step 3 — Evaluation Metrics**

Each model was evaluated using:

\- R² Score  

\- Mean Squared Error (MSE)  

\- Root Mean Squared Error (RMSE)  

\- Mean Absolute Error (MAE)



---



&nbsp;**Step 4 — Results Summary**

&nbsp;## Model Performance Comparison



| Model              | R² Score | MSE              | RMSE             | MAE             |

|--------------------|----------|------------------|------------------|-----------------|

| Linear Regression  | 0.611101 | 1.012526e+12     | 1.006244e+06     | 7.576762e+05    |

| Random Forest      | 0.593366 | 1.058700e+12     | 1.028931e+06     | 7.587695e+05    |

| KNN                | 0.547693 | 1.177611e+12     | 1.085178e+06     | 8.152734e+05    |

| Decision Tree      | 0.366538 | 1.649261e+12     | 1.284235e+06     | 9.661882e+05    |

| SVM                | -0.044907| 2.720487e+12     | 1.649390e+06     | 1.306995e+06    |



&nbsp;   



&nbsp;   

&nbsp;   

&nbsp;**Conclusion**

The Random Forest model performed the best overall, providing the highest R² score and lowest error metrics.  

This project demonstrates how various regression models can be applied to predict continuous values effectively.



---



 **Tools \& Libraries**

\- Python 3

\- Pandas, NumPy

\- Scikit-learn

\- Matplotlib / Seaborn

\- Google Colab



---



&nbsp;**Files Included**

\- `assignment4.ipynb` — Main Notebook  

\- `housing.csv` — Dataset  

\- `README.md` — Project Summary



