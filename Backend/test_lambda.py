import unittest
from unittest.mock import MagicMock 
import lambda_function

class TestLambdaFunction(unittest.TestCase):

    def test_lambda_handler(self):
        
        lambda_function.mock_table = MagicMock()
        lambda_function.table.update_item.return_value ={
            'Attributes': {'views': 100}
            }
        
        result = lambda_function.lambda_handler({}, {})
        self.assertEqual(result['statusCode'], 200)
        
        # Is the 'views' count inside the body?
        self.assertIn('views', result['body'])
        
        # Did we send the CORS headers? (Crucial check!)
        self.assertEqual(result['headers']['Access-Control-Allow-Origin'], '*')

if __name__ == '__main__':
    unittest.main()
