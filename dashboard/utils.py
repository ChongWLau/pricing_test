from django.db.models import Count, Q, Sum

from .models import Quotes


def get_quotes_summary() -> dict:
    
    summary = {
        'sales_count': Count('sale_indicator', filter=Q(sale_indicator__exact=1)),
        'non_sales_count': Count('sale_indicator', filter=Q(sale_indicator__exact=0)),
        'total_price_sum': Sum('total_price'),
        'net_profit': Sum('profit') + Sum('tax'),
        'gross_profit': Sum('profit') + Sum('tax')
    }
    
    results = Quotes.objects.values('test_group').annotate(**summary).order_by()
    
    q = results[0]
    q['total_price_sum'] = round(q['total_price_sum'], 2)
    q['net_profit'] = round(q['net_profit'], 2)
    q['gross_profit'] = round(q['gross_profit'], 2)
    
    return q
