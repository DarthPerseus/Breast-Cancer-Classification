# -*- coding: utf-8 -*-
"""Breast cancer AIML project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qULEstpl5KMFeKcPFJnSaAK14WEcLITb
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
import pandas as pd

# Upload the dataset file
uploaded = files.upload()

# Assuming you've uploaded a CSV file, read it into a DataFrame
df = pd.read_csv(next(iter(uploaded)))

# Now you can use 'df' as your DataFrame
# For example, print the first few rows
print(df.head())

df.head()

df.tail()

df.shape

df.describe().T

df.diagnosis.unique()

df['diagnosis'].value_counts()

# Set figure size
plt.figure(figsize=(10, 6))

# Create the count plot
sns.countplot(x='diagnosis', data=df, palette='husl')

# Add title and labels
plt.title('Count of Diagnoses')
plt.xlabel('Diagnosis Type')
plt.ylabel('Count')

# Show the plot
plt.show()



"""clean and prepare the data"""

# Set the figure size for better visibility
plt.figure(figsize=(8, 6))

# Plot the histogram
plt.hist(df['diagnosis'], bins=2, color='g', edgecolor='black', alpha=0.7)

# Add title and axis labels
plt.title('Diagnosis Distribution (M=1, B=0)', fontsize=16)
plt.xlabel('Diagnosis (M=1, B=0)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Customize the x-axis ticks to show only 0 and 1
plt.xticks([0, 1], labels=['Benign (B=0)', 'Malignant (M=1)'])

# Add gridlines for better readability
plt.grid(True, axis='y', linestyle='--', alpha=0.6)

# Show the plot
plt.tight_layout()
plt.show()

# Filter only the numerical columns from the DataFrame
numerical_df = df.select_dtypes(include=['float64', 'int64'])

# Set the figure size
plt.figure(figsize=(20, 20))

# Create the heatmap for the correlation matrix of the numerical columns
sns.heatmap(numerical_df.corr(), annot=True)

# Show the plot
plt.show()

# Filter only the numerical columns from the DataFrame
numerical_df = df.select_dtypes(include=['float64', 'int64'])

# Set the figure size
plt.figure(figsize=(16, 12))

# Calculate the correlation matrix
corr = numerical_df.corr()

# Create a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set the color palette
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Create the heatmap for the correlation matrix of the numerical columns
sns.heatmap(corr, mask=mask, cmap=cmap, annot=True, fmt=".2f",
            linewidths=.5, cbar_kws={"shrink": .8}, annot_kws={"size": 10})

# Add title and labels
plt.title('Correlation Heatmap of Numerical Features', fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()

# generate a scatter plot matrix with the "mean" columns
cols = ['diagnosis',
        'radius_mean',
        'texture_mean',
        'perimeter_mean',
        'area_mean',
        'smoothness_mean',
        'compactness_mean',
        'concavity_mean',
        'concave points_mean',
        'symmetry_mean',
        'fractal_dimension_mean']

sns.pairplot(data=df[cols], hue='diagnosis', palette='rocket')

# Filter only the numerical columns from the DataFrame
numerical_df = df.select_dtypes(include=['float64', 'int64'])

# Compute the correlation matrix
corr = numerical_df.corr().round(2)

# Mask for the upper triangle
mask = np.zeros_like(corr, dtype=bool)  # Use bool instead of np.bool
mask[np.triu_indices_from(mask)] = True

# Set figure size
f, ax = plt.subplots(figsize=(20, 20))

# Define custom colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmin=-1, vmax=1, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)

# Show the plot
plt.show()

# Define a function to drop specified columns from the DataFrame
def drop_columns(dataframe, columns):
    """Drops specified columns from the given DataFrame if they exist."""
    # Filter out columns that are not in the DataFrame
    columns_to_drop = [col for col in columns if col in dataframe.columns]
    if columns_to_drop:
        dataframe.drop(columns=columns_to_drop, axis=1, inplace=True)
    else:
        print("No columns to drop from DataFrame.")

# List of columns to drop related to worst attributes
worst_columns = [
    'radius_worst', 'texture_worst', 'perimeter_worst',
    'area_worst', 'smoothness_worst', 'compactness_worst',
    'concavity_worst', 'concave points_worst', 'symmetry_worst',
    'fractal_dimension_worst'
]

# List of columns to drop related to perimeter and area attributes
perimeter_area_columns = [
    'perimeter_mean', 'perimeter_se', 'area_mean', 'area_se'
]

# List of columns to drop related to concavity and concave points
concavity_columns = [
    'concavity_mean', 'concavity_se', 'concave points_mean', 'concave points_se'
]

# Combine all columns to drop into a single list
all_columns_to_drop = worst_columns + perimeter_area_columns + concavity_columns

# Drop the specified columns from the DataFrame
drop_columns(df, all_columns_to_drop)

# Verify remaining columns
remaining_columns = df.columns
print("Remaining columns after dropping:", remaining_columns)

# Filter only the numerical columns from the DataFrame
numerical_df = df.select_dtypes(include=['float64', 'int64'])

# Compute the correlation matrix
corr = numerical_df.corr().round(2)

# Mask for the upper triangle
mask = np.zeros_like(corr, dtype=bool)  # Use 'bool' instead of 'np.bool'
mask[np.triu_indices_from(mask)] = True

# Set figure size
f, ax = plt.subplots(figsize=(20, 20))

# Define custom colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmin=-1, vmax=1, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)

# Tight layout to improve spacing
plt.tight_layout()

# Show the plot
plt.show()



"""Buidling Model"""

# Check if 'diagnosis' column exists in the DataFrame
if 'diagnosis' in df.columns:
    # Separate the features (X) and the target variable (y)
    X = df.drop(['diagnosis'], axis=1)  # Features (all columns except 'diagnosis')
    y = df['diagnosis']  # Target variable (the 'diagnosis' column)
else:
    print("'diagnosis' column not found in the DataFrame.")

from sklearn.model_selection import train_test_split

# Split the dataset into training and testing sets
# test_size=0.3 means 30% of the data will be used for testing
# random_state=40 ensures reproducibility of the split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)

# Print the shapes of the resulting sets to verify the split
print("Training set size:", X_train.shape, "Testing set size:", X_test.shape)

# Create an instance of StandardScaler
ss = StandardScaler()

# Fit the scaler on the training data and transform it
X_train = ss.fit_transform(X_train)

# Transform the test data using the scaler fitted on the training data
X_test = ss.transform(X_test)  # Use transform instead of fit_transform

# Optional: Print the shapes of the transformed sets to verify the transformation
print("Transformed training set shape:", X_train.shape)
print("Transformed testing set shape:", X_test.shape)

"""Logistic Regression"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Create an instance of LogisticRegression
lr = LogisticRegression()

# Fit the model on the training data
model1 = lr.fit(X_train, y_train)

# Make predictions on the test data
predictions1 = model1.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, predictions1)
confusion = confusion_matrix(y_test, predictions1)
report = classification_report(y_test, predictions1)

# Print the evaluation results
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", confusion)
print("Classification Report:\n", report)

from sklearn.metrics import confusion_matrix

# Calculate the confusion matrix
cm = confusion_matrix(y_test, predictions1)

# Print the confusion matrix
print("Confusion Matrix:\n", cm)

# Set up the figure size
plt.figure(figsize=(8, 6))

# Create a heatmap to visualize the confusion matrix
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Benign (B=0)', 'Malignant (M=1)'],
            yticklabels=['Benign (B=0)', 'Malignant (M=1)'])

# Set titles and labels
plt.title('Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')

# Show the plot
plt.show()

sns.heatmap(cm, annot=True)  # Create a heatmap with annotations
# Save the figure as a PNG file
plt.savefig('confusion_matrix.png', dpi=300, bbox_inches='tight')
# Show the plot
plt.show()

"""Accuracy =
TP
+
TN
/
(
TP
+
TN
+
FP
+
FN
)
"""

TP = cm[0][0]  # True Positives
TN = cm[1][1]  # True Negatives
FN = cm[1][0]  # False Negatives
FP = cm[0][1]  # False Positives

# Calculate Testing Accuracy
accuracy = (TP + TN) / (TP + TN + FN + FP)
print('Testing Accuracy:', accuracy)