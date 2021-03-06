import sys
from traceback import print_exc
import simplejson

from byzantine.model.models import *
import byzantine.model.meta as meta

def commit():
    meta.session.commit()

def rollback():
    meta.session.rollback()
    
def create_response(code, type=None, value=None):
    if type == None and value == None:
        response = {
                        "version": 1.0,
                        "code": code,
                        "data": None
                   }
    else:
        response = { 
                        "version": 1.0,
                        "code": code,
                        "data": {
                            "type": type,
                            "body": value
                            }
                   }

    return simplejson.dumps(response)

def commit_or_rollback(func):
    def inner_func(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            commit()
            return response
        except Exception, e:
            rollback()
            (type, value, traceback) = sys.exc_info()
            #log type, value, traceback to file
            print_exc()
            raise e

    inner_func.__name__ = func.__name__
    inner_func.__dict__ = func.__dict__

    return inner_func


def json_response(func):
    def inner_func(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            if isinstance(response, tuple) and len(response) == 2:
                (type, value) = response
                return create_response(0, type, value)
            else:
                return create_response(0)
        except:
            print_exc()
            return create_response(500, "string", "Internal Error")


    inner_func.__name__ = func.__name__
    inner_func.__dict__ = func.__dict__

    return inner_func

def add_and_flush(object):
    meta.session.add(object)
    meta.session.flush()
    
def delete_and_flush(object):
    meta.session.delete(object)
    meta.session.flush()
