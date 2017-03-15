import config
import datetime

__author__ = 'scottbowers'


def debug(_message):
    if config.cDebug:
        print config.cOKGREEN + str(_message) + config.cENDC + " " + str(datetime.datetime.now())


def debug_return_message(_r):
    _message = _r.text if len(_r.text) > 0 else _r

    if str(_message) == "<Response [200]>" or str(_message) == "<Response [201]>" or str(_message) == "<Response [204]>":
        if config.cDebug:
            print config.cOKBLUE + str(_message) + config.cENDC + " " + str(datetime.datetime.now())
    else:
        error(_r.text)
        error(_r)


def debug_timer(_message, _time):
    print config.cOKBLUE + _message + str(_time) + config.cENDC + " " + str(datetime.datetime.now())


def error(_message):
    print config.cFAIL + str(_message) + config.cENDC + " " + str(datetime.datetime.now())


def exception(_message):
    print config.cWARNING + str(_message) + config.cENDC + " " + str(datetime.datetime.now())

