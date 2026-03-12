import json
import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor_count')

def lambda_handler(event, context):
    
    # Update the item in the database (Add +1 atomically)
    # Since 'views' is reserved, we use '#v' as a placeholder
    response = table.update_item(
        Key={
            'id': 'page_view'
        },
        UpdateExpression='SET #v = #v + :val',
        ExpressionAttributeNames={
            '#v': 'views'
        },
        ExpressionAttributeValues={
            ':val': 1
        },
        ReturnValues='UPDATED_NEW'
    )
    
    # Get the new view count from the response
    # Note: response['Attributes'] contains the new values
    views = response['Attributes']['views']
    
    # Return the count to the website
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(str(views))
    }