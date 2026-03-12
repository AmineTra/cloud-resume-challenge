import unittest
from unittest.mock import MagicMock
import lambda_function # Imports your code

class TestLambda(unittest.TestCase):

    def test_lambda_handler(self):
        # 1. SETUP: Create a fake table
        mock_table = MagicMock()
        
        # 2. Tell the fake table to return '123' when updated
        mock_table.update_item.return_value = {
            'Attributes': {'views': 123}
        }

        lambda_function.table = mock_table

        result = lambda_function.lambda_handler(None, None)

        self.assertEqual(result['statusCode'], 200)
        
        # We expect "123" (string) because your code does json.dumps(str(views))
        self.assertEqual(result['body'], '"123"') 
        
        self.assertEqual(result['headers']['Access-Control-Allow-Origin'], '*')

if __name__ == '__main__':
    unittest.main()