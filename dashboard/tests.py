from django.test import TestCase, RequestFactory
from dashboard.models import Quotes
from dashboard.admin import DashboardViewAdmin

# Create your tests here.
class DashboardTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Quotes.objects.create()