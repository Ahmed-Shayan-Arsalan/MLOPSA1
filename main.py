import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    # Load the CSV (assumes iris.csv is present in the working directory)
    df = pd.read_csv('iris.csv')

    # Define features and target
    X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
    y = df['Species']

    # Split the dataset (train/test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Predict and calculate accuracy
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

    test_input = [[5.1, 3.5, 1.4, 0.2]]
    expected_output = "Iris-setosa" 

    # Predict using the hardcoded test input
    test_prediction = model.predict(test_input)[0]
    print(f"Hardcoded Test Prediction: {test_prediction}")

    if test_prediction == expected_output:
        print("Hardcoded test passed!")
    else:
        print("Hardcoded test failed!")
if __name__ == "__main__":
    main()
