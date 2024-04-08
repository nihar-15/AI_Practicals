# -*- coding: utf-8 -*-
"""A2_19_Practical_07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zJKQufzSfgnrBKm2WyF8Sb6jaxarNydM
"""

## Name: Niharika Kumar
## Batch: A2
## Roll No: 19
                          ## Practical No. 07

## Aim: Write a program to implement Naive - Bayes Classifier.




## part A: Implement Naive Bayes Classifier

import pandas as pd

# Define the playtennis dataset
playtennis_data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

# Create DataFrame
df = pd.DataFrame(playtennis_data)

# Display the DataFrame
print(df)

# Calculating prior probability


prior_probability_yes = df['PlayTennis'].value_counts()['Yes']/14

prior_probability_no = df['PlayTennis'].value_counts()['No']/14

# Filter the DataFrame based on the conditions
overcast_yes_count = df[(df['Outlook'] == 'Overcast') & (df['PlayTennis'] == 'Yes')].shape[0]

overcast_yes_count = df[(df['Outlook'] == 'Overcast') & (df['PlayTennis'] == 'Yes')].shape[0]/9
overcast_no_count = df[(df['Outlook'] == 'Overcast') & (df['PlayTennis'] == 'No')].shape[0]/5
sunny_yes_count = df[(df['Outlook'] == 'Sunny') & (df['PlayTennis'] == 'Yes')].shape[0]/9
sunny_no_count = df[(df['Outlook'] == 'Sunny') & (df['PlayTennis'] == 'No')].shape[0]/5
rain_yes_count = df[(df['Outlook'] == 'Rain') & (df['PlayTennis'] == 'Yes')].shape[0]/9
rain_no_count = df[(df['Outlook'] == 'Rain') & (df['PlayTennis'] == 'No')].shape[0]/5

weak_yes_count = df[(df['Wind'] == 'Weak') & (df['PlayTennis'] == 'Yes')].shape[0]/9
weak_no_count = df[(df['Wind'] == 'Weak') & (df['PlayTennis'] == 'No')].shape[0]/5
strong_yes_count = df[(df['Wind'] == 'Strong') & (df['PlayTennis'] == 'Yes')].shape[0]/9
strong_no_count = df[(df['Wind'] == 'Strong') & (df['PlayTennis'] == 'No')].shape[0]/5

hot_yes_count = df[(df['Temperature'] == 'Hot') & (df['PlayTennis'] == 'Yes')].shape[0]/9
hot_no_count = df[(df['Temperature'] == 'Hot') & (df['PlayTennis'] == 'No')].shape[0]/5
mild_yes_count = df[(df['Temperature'] == 'Mild') & (df['PlayTennis'] == 'Yes')].shape[0]/9
mild_no_count = df[(df['Temperature'] == 'Mild') & (df['PlayTennis'] == 'No')].shape[0]/5
cool_yes_count = df[(df['Temperature'] == 'Cool') & (df['PlayTennis'] == 'Yes')].shape[0]/9
cool_no_count = df[(df['Temperature'] == 'Cool') & (df['PlayTennis'] == 'No')].shape[0]/5

high_yes_count = df[(df['Humidity'] == 'High') & (df['PlayTennis'] == 'Yes')].shape[0]/9
high_no_count = df[(df['Humidity'] == 'High') & (df['PlayTennis'] == 'No')].shape[0]/5
normal_yes_count = df[(df['Humidity'] == 'Normal') & (df['PlayTennis'] == 'Yes')].shape[0]/9
normal_no_count = df[(df['Humidity'] == 'Normal') & (df['PlayTennis'] == 'No')].shape[0]/5

print("We are now done with the precomputations.....")

today = ("Sunny" ,"Hot" , "Normal" ,"Weak")

# Calculate the probability of playing tennis
probability_yes_today = (sunny_yes_count * hot_yes_count * normal_yes_count * weak_yes_count * prior_probability_yes)

# Calculate the probability of not playing tennis
probability_no_today = (sunny_no_count * hot_no_count * normal_no_count * weak_no_count * prior_probability_no)

# Print the probabilities
print("Probability of playing tennis today:", probability_yes_today)
print("Probability of not playing tennis today:", probability_no_today)

# Compare the probabilities
if probability_yes_today > probability_no_today:
    print("The probability of playing tennis today is higher.")
elif probability_yes_today < probability_no_today:
    print("The probability of not playing tennis today is higher.")
else:
    print("The probabilities of playing tennis and not playing tennis today are equal.")

probability_yes_case1 = (overcast_yes_count*weak_yes_count*mild_yes_count*high_yes_count * prior_probability_yes)
probability_no_case1 = (overcast_no_count*weak_no_count*mild_no_count*high_no_count * prior_probability_no)

print("Test Case :")
print("Probability of playing tennis:", probability_yes_case1)
print("Probability of not playing tennis:", probability_no_case1)
if probability_yes_case1 > probability_no_case1:
    print("The probability of playing tennis is higher.")
elif probability_yes_case1 < probability_no_case1:
    print("The probability of not playing tennis is higher.")
else:
    print("The probabilities of playing tennis and not playing tennis are equal.")

## Part B : Using scikit learn library for Naive Bayes Classifier

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Define the playtennis dataset
playtennis_data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

# Create DataFrame from the playtennis_data
df = pd.DataFrame(playtennis_data)

# Convert categorical variables to numerical using one-hot encoding
df = pd.get_dummies(df, drop_first=True)

# Split the dataset into features (X) and target variable (y)
X = df.drop('PlayTennis_Yes', axis=1)
y = df['PlayTennis_Yes']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Multinomial Naive Bayes classifier
mnb = MultinomialNB()

# Train the classifier using the training data
mnb.fit(X_train, y_train)

# Predict using the trained classifier
y_pred = mnb.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

from sklearn.datasets import make_classification

X, y = make_classification(
    n_features=6,
    n_classes=3,
    n_samples=800,
    n_informative=2,
    random_state=1,
    n_clusters_per_class=1,
)

import matplotlib.pyplot as plt

plt.scatter(X[:, 0], X[:, 1], c=y, marker="*");

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=125
)

from sklearn.naive_bayes import GaussianNB

# Build a Gaussian Classifier
model = GaussianNB()

# Model training
model.fit(X_train, y_train)

# Predict Output
predicted = model.predict([X_test[6]])

print("Actual Value:", y_test[6])
print("Predicted Value:", predicted[0])

"""In this practical session:

1. We implemented a Naive Bayes classifier both manually and using scikit-learn library for the playtennis dataset.
2. The manual approach involved computing prior and conditional probabilities based on dataset attributes, and performing test cases to predict tennis playing probability.
3. We utilized scikit-learn to preprocess the dataset, train the classifier, and evaluate its accuracy.
4. Visualization was employed to understand the dataset's distribution and a Gaussian Naive Bayes model was built for classification.

In summary, we successfully applied Naive Bayes classification techniques to predict tennis playing probability, demonstrating both manual computation and library-based implementation for comparison."""