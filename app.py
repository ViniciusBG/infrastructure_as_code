#!/usr/bin/env python3
import os

from aws_cdk import core
from structure.structure import MyStack
from structure.ec2 import EC2InstanceStack


app = core.App()
MyStack(app, "DeployingStack")
app.synth()