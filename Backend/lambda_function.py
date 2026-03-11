import json
import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor_count')

def lambda_handler(event, context):
    # Increment the visitor count in DynamoDB
    response = table.update_item(
        Key={'id': 'visitor_count'},
        UpdateExpression='ADD count :increment',
        ExpressionAttributeValues={':increment': 1},
        ReturnValues='UPDATED_NEW'
    )
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps({'views': views})
    }