import os
import unittest
import pandas as pd
from sklearn.linear_model import LogisticRegression

class TestIrisModel(unittest.TestCase):
    def test_hardcoded_prediction(self):
        # Construct the path to Iris.csv in the same folder as test_app.py
        base_dir = os.path.dirname(os.path.abspath(__file__))
        iris_path = os.path.join(base_dir, 'iris.csv')
        
        # Load the CSV using the constructed path
        df = pd.read_csv(iris_path)
        
        # Define features and target
        X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
        y = df['Species']
        
        # Train the model (for testing purposes, we train on the whole dataset)
        model = LogisticRegression(max_iter=200)
        model.fit(X, y)
        
        # Use a hardcoded test input
        test_input = [[5.1, 3.5, 1.4, 0.2]]
        expected_output = "Iris-setosa"
        
        # Predict and check result
        prediction = model.predict(test_input)[0]
        self.assertEqual(prediction, expected_output, "Hardcoded tests prediction did not match.")

if __name__ == '__main__':
    unittest.main()
