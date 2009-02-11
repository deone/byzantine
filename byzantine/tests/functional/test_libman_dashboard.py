from byzantine.tests import *

class TestLibmanDashboardController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='libman_dashboard'))
        # Test response...
