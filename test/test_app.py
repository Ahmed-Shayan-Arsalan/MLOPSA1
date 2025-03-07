import unittest
import joblib

class TestIrisModel(unittest.TestCase):
    def test_hardcoded_prediction(self):
        model = joblib.load('model.pkl')
        test_input = [[5.1, 3.5, 1.4, 0.2]]
        expected_output = "Iris-setosa"
        test_prediction = model.predict(test_input)[0]
        self.assertEqual(test_prediction, expected_output)

if __name__ == "__main__":
    unittest.main()
