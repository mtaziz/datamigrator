from unittest import TestCase


class TestDependencies(TestCase):
    def test_configparser_dependency(self):
        try:
            import configparser
        except:
            self.fail(msg="could not load configparser")

    def test_datetime_dependency(self):
        try:
            import datetime
        except:
            self.fail(msg="could not load datetime")

    def test_json_dependency(self):
        try:
            import json
            x = json.loads("{}")
        except:
            self.fail(msg="could not load json")
        self.assertTrue(True)

    def test_pickle_dependency(self):
        try:
            import pickle
        except:
            self.fail(msg="could not load pickle")

    def test_requests_dependency(self):
        try:
            import requests
        except:
            self.fail(msg="could not load requests")

        sess = requests.Session()
        r = sess.get('http://www.planetscott.com')
        self.assertEquals(str(r), '<Response [200]>')

    def test_time_dependency(self):
        try:
            import time
        except:
            self.fail(msg="could not load time")