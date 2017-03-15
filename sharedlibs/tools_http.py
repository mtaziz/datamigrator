import json
import pickle
import time
import os

import requests

import config
import tools

__author__ = 'sbowers'


def get_api_cookie():
    try:
        f = open(os.path.dirname(os.path.dirname(__file__)) + '/__cookiedump', 'rb')
        try:
            cookies = pickle.load(f)
            #  debug("Cookie Got")
            return cookies
        except:
            tools.exception("EXCEPTION: No cookie returned on get_api_cookie")
            return ""
        finally:
            f.close()
    except:
        tools.exception("EXCEPTION: File " + os.path.dirname(os.path.dirname(__file__)) + "/__cookiedump NOT FOUND")
    return ""


def get_json(_tablename, _external_id):
    sess = requests.Session()
    r = http_do_get(sess, config.DynamoHost + _tablename)

    tools.debug(r.text if len(r.text) > 0 else r)
    decoded = json.loads(r.text)
    return decoded


def http_do_delete(_sess, _url):
    tools.debug("Delete to " + _url)
    t = time.time()
    r = _sess.delete(_url, cookies=get_api_cookie())
    if r.text.find("authentication.credentials.required") > 0:
        r = _sess.get(_url, cookies=set_api_cookie(_sess))
    tools.debug_timer("http_do_delete", time.time() - t)
    return r


def http_do_get(_sess, _url):
    tools.debug("Get to " + _url)
    t = time.time()
    r = _sess.get(_url, cookies=get_api_cookie())
    if r.text.find("authentication.credentials.required") > 0:
        r = _sess.get(_url, cookies=set_api_cookie(_sess))
    tools.debug_timer("http_do_get", time.time() - t)
    return r


def http_do_patch(_sess, _url, _json):
    tools.debug("PATCHING TO " + _url)
    tools.debug("JSON=" + json.dumps(_json))
    t = time.time()
    v_headers = {"content-type": "application/json"}
    r = _sess.patch(_url, cookies=get_api_cookie(),
                    data=json.dumps(_json), headers=v_headers)
    if r.text.find("authentication.credentials.required") > 0:
        r = _sess.patch(_url, cookies=set_api_cookie(_sess),
                        data=json.dumps(_json), headers=v_headers)
    tools.debug_timer("http_do_patch", time.time() - t)
    return r


def http_do_post(_sess, _url, _json):
    tools.debug("POSTING TO " + _url)
    tools.debug("JSON=" + json.dumps(_json))
    t = time.time()
    v_headers = {"content-type": "application/json"}
    r = _sess.post(_url, cookies=get_api_cookie(),
                   data=json.dumps(_json), headers=v_headers)
    if r.text.find("authentication.credentials.required") > 0:
        r = _sess.post(_url, cookies=set_api_cookie(_sess),
                       data=json.dumps(_json), headers=v_headers)
    tools.debug_timer("http_do_post", time.time() - t)
    return r


def http_do_put(_sess, _url, _json):
    tools.debug("Put to " + _url)
    tools.debug("JSON=" + json.dumps(_json))
    t = time.time()
    v_headers = {"content-type": "application/json"}
    r = _sess.put(_url, cookies=get_api_cookie(),
                  data=json.dumps(_json), headers=v_headers)
    if r.text.find("authentication.credentials.required") > 0:
        r = _sess.put(_url, cookies=set_api_cookie(_sess),
                      data=json.dumps(_json), headers=v_headers)
    tools.debug_timer("http_do_put", time.time() - t)
    return r


def set_api_cookie(_sess):
    tools.debug("Setting Cookie")
    _sess.get(config.DynamoHost + 'me', auth=(config.DynamoUser, config.DynamoPassword))
    f = open(os.path.dirname(os.path.dirname(__file__)) + '/__cookiedump', 'wb')
    try:
        pickle.dump(_sess.cookies, f)
        tools.debug('COOKIE WRITTEN TO ' + os.path.dirname(os.path.dirname(__file__)) + '/__cookiedump')
    except:
        tools.error("set_api_cookie failed")
    finally:
        f.close()
    return get_api_cookie()


