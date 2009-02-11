import logging

from byzantine.lib.base import *

log = logging.getLogger(__name__)

class LibmanDashboardController(BaseController):

    def index(self):
        return 'Hello World'
