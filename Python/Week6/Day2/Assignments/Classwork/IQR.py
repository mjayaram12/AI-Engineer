import numpy as np
import pandas as pd

df =pd.read_csv('SalesDataset_05OCT.csv')
print(df.head())

p25 = np.percentile(df['Total Amount'], 25)
p75 = np.percentile(df['Total Amount'], 75)
IQR = p75 - p25

print(f"IQR", IQR)
Q1 = p25
Q3 = p75

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Total Amount'] < lower_bound) | (df['Total Amount'] > upper_bound)]
print("Outliers:", outliers)

# Save outliers to a CSV file
outliers.to_csv('Data_with_Outliers_IQR.csv', index=False)
print("Data with outliers:", outliers)


# Remove outliers from the original dataset
df_no_outliers = df[(df['Total Amount'] >= lower_bound) & (df['Total Amount'] <= upper_bound)]
print("Data without outliers:", df_no_outliers)

df_no_outliers.to_csv('Data_Without_Outliers_IQR.csv', index=False) 
print("Data without outliers saved to 'Data_Without_Outliers_IQR.csv'")