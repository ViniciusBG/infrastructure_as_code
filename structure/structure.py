from aws_cdk import core as cdk
from aws_cdk import aws_s3 as s3

import os.path

from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    core    
)

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

        name = "second-deployed-bucket"
        s3.Bucket(
            self,
            id=name,
            bucket_name=name,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED
        )

        name = "third-deployed-bucket"
        s3.Bucket(
            self,
            id=name,
            bucket_name=name,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED
        )

    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # VPC
        vpc = ec2.Vpc(
            self,
            "VPC",
            nat_gateways=0,
            subnet_configuration=[ec2.SubnetConfiguration(
                name="public",
                subnet_type=ec2.SubnetType.PUBLIC)]
            )

        # AMI 
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
            )

        # Instance Role and SSM Managed Policy
        role = iam.Role(
            self,
            "InstanceSSM",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))

        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonEC2RoleforSSM"))

        # Instance
        instance = ec2.Instance(
            self,
            "Instance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=amzn_linux,
            vpc = vpc,
            role = role
            )




