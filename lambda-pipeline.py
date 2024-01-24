import boto3
lambda_Client = boto3.client('lambda', region_name='us-east-1')
response =lambda_Client.create_function(
          Code={
                'S3Bucket': 'deepthi777',
                'S3Key': 'demo.zip', #how can i create or fetch this S3Key
          },
          Description='Process image objects from Amazon S3.',
          FunctionName="test",
          Handler='demo.lambda_handler',
          Publish=True,
          Role='arn:aws:iam::532351638542:role/service-role/boto3-role-qlc606my',
          Runtime='python3.12'
          )
