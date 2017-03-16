import json
import pickle
import time
import os
import requests
import config
import debug

__author__ = 'sbowers'

# NOTE, THIS IS CURRENTLY A STUB WAITING FOR A SANDBOX FOR DYNAMO DB...


class ToolsHttp(object):
    @staticmethod
    def get_api_cookie():
        try:
            f = open(os.path.dirname(os.path.dirname(__file__)) + '/__cookiedump', 'rb')
            try:
                cookies = pickle.load(f)
                #  debug("Cookie Got")
                return cookies
            except:
                debug.exception("EXCEPTION: No cookie returned on get_api_cookie")
                return ""
            finally:
                f.close()
        except:
            debug.exception("EXCEPTION: File " + os.path.dirname(os.path.dirname(__file__)) + "/__cookiedump NOT FOUND")
        return ""

    def get_json(self, _tablename):
        sess = requests.Session()
        r = self.do_get(sess, config.DynamoHost + _tablename)

        # debug.debug(r.text if len(r.text) > 0 else r)
        decoded = json.loads(r.text)
        return decoded

    def http_do_delete(self, _sess, _url):
        # debug.debug("Delete to " + _url)
        t = time.time()
        r = _sess.delete(_url, cookies=self.get_api_cookie())
        if r.text.find("authentication.credentials.required") > 0:
            r = _sess.get(_url, cookies=self.set_api_cookie(_sess))
        # debug.debug_timer("http_do_delete", time.time() - t)
        return r

    def do_get(self, _url):
        # debug.debug("Get to " + _url)
        t = time.time()
        r = _sess.get(_url, cookies=self.get_api_cookie())
        if r.text.find("authentication.credentials.required") > 0:
            r = _sess.get(_url, cookies=self.set_api_cookie(_sess))
        # debug.debug_timer("http_do_get", time.time() - t)
        return r

    def http_do_patch(self, _sess, _url, _json):
        # debug.debug("PATCHING TO " + _url)
        # debug.debug("JSON=" + json.dumps(_json))
        t = time.time()
        v_headers = {"content-type": "application/json"}
        r = _sess.patch(_url, cookies=self.get_api_cookie(),
                        data=json.dumps(_json), headers=v_headers)
        if r.text.find("authentication.credentials.required") > 0:
            r = _sess.patch(_url, cookies=self.set_api_cookie(_sess),
                            data=json.dumps(_json), headers=v_headers)
        # debug.debug_timer("http_do_patch", time.time() - t)
        return r

    def http_do_post(self, _sess, _url, _json):
        # debug.debug("POSTING TO " + _url)
        # debug.debug("JSON=" + json.dumps(_json))
        t = time.time()
        v_headers = {"content-type": "application/json"}
        r = _sess.post(_url, cookies=self.get_api_cookie(),
                       data=json.dumps(_json), headers=v_headers)
        if r.text.find("authentication.credentials.required") > 0:
            r = _sess.post(_url, cookies=self.set_api_cookie(_sess),
                           data=json.dumps(_json), headers=v_headers)
        # debug.debug_timer("http_do_post", time.time() - t)
        return r

    def http_do_put(self, _sess, _url, _json):
        # debug.debug("Put to " + _url)
        # debug.debug("JSON=" + json.dumps(_json))
        t = time.time()
        v_headers = {"content-type": "application/json"}
        r = _sess.put(_url, cookies=self.get_api_cookie(),
                      data=json.dumps(_json), headers=v_headers)
        if r.text.find("authentication.credentials.required") > 0:
            r = _sess.put(_url, cookies=self.set_api_cookie(_sess),
                          data=json.dumps(_json), headers=v_headers)
        # debug.debug_timer("http_do_put", time.time() - t)
        return r

    def set_api_cookie(self, _sess):
        # debug.debug("Setting Cookie")
        _sess.get(config.DynamoHost + 'me', auth=(config.DynamoUser, config.DynamoPassword))
        f = open(os.path.dirname(os.path.dirname(__file__)) + '/__cookiedump', 'wb')
        try:
            pickle.dump(_sess.cookies, f)
            # debug.debug('COOKIE WRITTEN TO ' + os.path.dirname(os.path.dirname(__file__)) + '/__cookiedump')
        except:
            debug.error("set_api_cookie failed")
        finally:
            f.close()
        return self.get_api_cookie()


