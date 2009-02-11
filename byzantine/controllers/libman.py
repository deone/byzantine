import logging

from byzantine.lib.base import *
import byzantine.model.helpers as h

log = logging.getLogger(__name__)

def authenticate(username, password):
    if username == "manager":
        if password == "manager":
            user_id = 1
            return user_id

    return False

class User(object):
    def __init__(self, username, id):
        self.username = username
        self.id = 1

class LibmanController(BaseController):

    def index(self):
        return render('/librarymanager/index.html')

    @h.json_response
    def login(self, **kwargs):
        username = request.params['username']
        password = request.params['password']

        id = authenticate(username, password)
        session['user'] = User(username, id)
        session.save()

        return ("object", id)
