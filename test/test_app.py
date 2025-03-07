import unittest
import pandas as pd
from sklearn.linear_model import LogisticRegression

class TestIrisModel(unittest.TestCase):
    def test_hardcoded_prediction(self):
        # Load the CSV from the repo root. Adjust the path if necessary.
        df = pd.read_csv('../Iris.csv')
        
        # Define features and target.
        X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
        y = df['Species']

        # Train the model on the entire dataset (for this test).
        model = LogisticRegression(max_iter=200)
        model.fit(X, y)

        # Use a hardcoded test input.
        test_input = [[5.1, 3.5, 1.4, 0.2]]
        expected_output = "Iris-setosa"

        # Get the prediction.
        prediction = model.predict(test_input)[0]
        self.assertEqual(prediction, expected_output, "Hardcoded test prediction did not match.")

if __name__ == '__main__':
    unittest.main()
