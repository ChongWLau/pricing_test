from dashboard.models import Quotes


def run():
    
    old_data = Quotes.objects.all()
    old_data.delete()