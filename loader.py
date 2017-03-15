__author__ = 'scottbowers'

import requests
import sharedlibs.tools as _tools
import sharedlibs.config as _config
import sharedlibs.tools_http as _tools_http


sess = requests.Session()

r = _tools_http.http_do_delete(sess, _config.DynamoHost)