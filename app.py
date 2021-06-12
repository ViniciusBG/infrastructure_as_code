#!/usr/bin/env python3
import os

from aws_cdk import core
from structure.structure import MyStack


app = core.App()
MyStack(app, "DeployStack")
app.synth()