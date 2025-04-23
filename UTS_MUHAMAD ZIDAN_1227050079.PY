#%%
# Loading libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import tree

#%%
# Load the citrus_data dataset
citrus_data = pd.read_csv('citrus.csv')
print(citrus_data.info())


#%%
# Explore the data
print(citrus_data.head())
print("\nData description:")
print(citrus_data.describe())
print("\nClass distribution:")
print(citrus_data['name'].value_counts())

#%%
citrus_data['size_category'] = pd.qcut(citrus_data['weight'], q=3, labels=['small', 'medium', 'large'])

#%%
# Visualize the data
plt.figure(figsize=(12, 6))
sns.pairplot(citrus_data, hue='size_category', vars=['diameter', 'weight', 'red', 'green', 'blue'], palette='Set1')
plt.suptitle('Pairplot of Citrus_data Features by Size Category', y=1.02)
plt.show()

#%%
# Prepare data for modeling
X = citrus_data[['diameter', 'weight', 'red', 'green', 'blue']]
y = citrus_data['size_category']

#%%
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#%%
# Train the decision tree model
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

#%%
# Make predictions
y_pred = model.predict(X_test)

#%%
# Evaluate the model
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

#%%
# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=model.classes_, 
            yticklabels=model.classes_)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

#%%
# Visualize the decision tree
plt.figure(figsize=(20,10))
tree.plot_tree(model, 
               feature_names=X.columns, 
               class_names=model.classes_,
               filled=True, 
               rounded=True,
               proportion=True)
plt.title("Decision Tree for Citrus_data Size Classification")
plt.show()

# Example prediction
#%%
sample_orange = {
    'diameter': 6.5,
    'weight': 130,
    'red': 160,
    'green': 80,
    'blue': 10
}

sample_df = pd.DataFrame([sample_orange])
prediction = model.predict(sample_df)
print(f"\nPrediction for sample orange: {prediction[0]}")