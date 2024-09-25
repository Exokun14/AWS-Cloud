def lambda_handler(event, context):
    print("Hello World")

    return {
        "statusCode": 200,
        "body": "Ok!"
    }
    
#lambda_handler(None, None)