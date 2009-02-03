import logging

from byzantine.lib.base import *

log = logging.getLogger(__name__)

class HomeController(BaseController):

    def index(self):
        return render("/index.html")
