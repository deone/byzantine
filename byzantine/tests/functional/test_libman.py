from byzantine.tests import *

class TestLibmanController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='libman'))
        # Test response...
