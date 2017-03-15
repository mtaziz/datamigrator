from unittest import TestCase
from extractor import Extractor
import sharedlibs.config as _config
import datetime
import json
import pickle
import requests

class TestFailer(TestCase):
    def test_should_fail(self):
        self.fail()

class TestDependencies(TestCase):
    def test_datetime_dependency(self):
        n = datetime.datetime.now()
        self.assertIsInstance(n, datetime.datetime)

    def test_json_dependency(self):
        try:
            x = json.loads("{}")
        except:
            self.fail()
        self.assertTrue(True)

    #def test_pickle_dependency(self):
    #    f = open('__cookiedump', 'rb')
    #    try:
    #        cookies = pickle.load(f)
    #    except:
    #        self.fail()
    #    finally:
    #       f.close()


    def test_requests_dependency(self):
        sess = requests.Session()
        r = sess.get('http://www.planetscott.com')
        self.assertEquals(str(r), '<Response [200]>')


class TestExtractor(TestCase):
    def test_extractor_database_connection(self):
        e =  Extractor()
        self.assertTrue(e.extract_tester)








