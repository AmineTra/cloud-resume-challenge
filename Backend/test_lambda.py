import unittest
from unittest.mock import MagicMock
import lambda_function

class TestLambda(unittest.TestCase):

    def test_lambda_handler(self):
        mock_table = MagicMock()
        
        mock_table.update_item.return_value = {
            'Attributes': {'views': 100}
        }
        
        lambda_function.table = mock_table

        
        result = lambda_function.lambda_handler(None, None)

        self.assertEqual(result['statusCode'], 200)
        self.assertIn('views', result['body'])
        self.assertEqual(result['headers']['Access-Control-Allow-Origin'], '*')

if __name__ == '__main__':
    unittest.main()