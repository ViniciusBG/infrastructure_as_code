from aws_cdk import core as cdk
from aws_cdk import aws_s3 as s3

class MyStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        name = "first-deployed-bucket"
        s3.Bucket(
            self,
            id=name,
            bucket_name=name,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED
        )
