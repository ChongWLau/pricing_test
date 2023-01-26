from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.forms.models import model_to_dict

from dashboard.models import Quotes
from dashboard.utils import get_quotes_summary

from mock import Mock
from decimal import Decimal


def get_admin_change_view_url(obj: object) -> str:
    return reverse(
        'admin:{}_{}_change'.format(
            obj._meta.app_label,
            type(obj).__name__.lower()
        ),
        args=(obj.pk,)
    )
    

# Create your tests here.
class DashboardTestCase(TestCase):
    
    def setUp(self):
        # self.factory = RequestFactory()
        pass
    
    def test_retrieve_quote_summary(self):
        
        test_data_1 = {
            'sale_indicator': 0,
            'net_price': 1111.11000000,
            'total_price': 2222.22000000,
        }
        test_data_2 = {
            'sale_indicator': 1,
            'net_price': 2222.22000000,
            'total_price': 3333.33000000,
        }
        Quotes.objects.create(**test_data_1)
        Quotes.objects.create(**test_data_2)
        
        mock_qs = Quotes.objects
        expected_result = {
            'test_group': 'A',
            'sales_count': 1,
            'non_sales_count': 1,
            'total_price_sum': Decimal('5555.55'),
            'net_price_sum': Decimal('3333.33'),
            'gross_price_sum': Decimal('2222.22')
        }
        result = get_quotes_summary(mock_qs)
        self.assertEqual(result[0], expected_result)  

    
    def test_change_view_loads_normally(self):
        User.objects.create_superuser(
            username='superuser', password='secret', email='admin@example.com'
        )
        c = Client()
        c.login(username='superuser', password='secret')                
        my_group = Group.objects.create(name='Test Group')
        response = c.get(get_admin_change_view_url(my_group))
        self.assertEqual(response.status_code, 200)