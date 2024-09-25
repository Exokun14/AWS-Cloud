import json

def lambda_handler(event, context):
    print("## Event Received ##")
    record = event.get("Records")[0]
    bucket = record.get("s3").get("bucket").get("name")
    file_name = record.get("s3").get("object").get("key")

    print(f"Bucket: {bucket}")
    print(f"File: {file_name}")
    
    return {
        "statusCode": 200,
        "body": "Ok!"
    }
    
#lambda_handler(None, None)