import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the Wine Quality dataset
# HOUSING_PATH = 'csit881-programming-python/WineQT.csv'
wine_df = pd.read_csv('WineQT.csv')

# Split data into features (X) and target (y)
x = wine_df.iloc[:, :-1]
# print("This is x {}".format(x))
y = wine_df.iloc[:, -1]
# print("This is y {}".format(y))
# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Initialize and fit the logistic regression model
logreg = LogisticRegression(solver='lbfgs', max_iter=1000)
logreg.fit(X_train, y_train)

# Make predictions on the test set
y_pred = logreg.predict(X_test)
print("This is y-test {}".format(y_test))
print("This is y-pred {}".format(y_pred))

# Calculate accuracy, precision, recall, and F1-score
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Print results
print("Experiment 1 - Logistic Regression")
print("Accuracy: {:.2f}".format(accuracy))
print("Precision: {:.2f}".format(precision))
print("Recall: {:.2f}".format(recall))
print("F1-Score: {:.2f}".format(f1))
