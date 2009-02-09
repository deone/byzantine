import logging

from byzantine.lib.base import *

log = logging.getLogger(__name__)

class LibmanController(BaseController):

    def index(self):
        return render('/librarymanager/index.html')
