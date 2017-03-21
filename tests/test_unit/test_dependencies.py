from unittest import TestCase


class TestDependencies(TestCase):
    def test_awscli_dependency(self):
        try:
            import awscli
        except:
            self.fail(msg="failed to load awscli dependency")

    def test_boto3_dependency(self):
        try:
            import boto3
        except:
            self.fail(msg="failed to load boto3 dependency")

    def test_configparser_dependency(self):
        try:
            import configparser
        except:
            self.fail(msg="failed to load configparser dependency")

    def test_cx_Oracle_dependency(self):
        try:
            import cx_Oracle
        except:
            self.fail(msg="failed to load cx_Oracle dependency")

    def test_datetime_dependency(self):
        try:
            import datetime
        except:
            self.fail(msg="failed to load datetime dependency")

    def test_json_dependency(self):
        try:
            import json
            x = json.loads("{}")
        except:
            self.fail(msg="failed to load json dependency")

    def test_os_dependency(self):
        try:
            import os
        except:
            self.fail(msg="failed to load os dependency")

    def test_time_dependency(self):
        try:
            import time
        except:
            self.fail(msg="failed to load time dependency")