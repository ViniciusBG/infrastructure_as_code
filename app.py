#!/usr/bin/env python3
import os

from aws_cdk import core
from structure.structure import MyStack


app = core.App()
BootcampCdkTurma5Stack(app, "MyStack")
app.synth()