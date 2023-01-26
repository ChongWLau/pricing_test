from django.db.models import Count, Q, Sum
from django.db.models.functions import Round


summary = {
    'sales_count': Count('sale_indicator', filter=Q(sale_indicator__exact=1)),
    'non_sales_count': Count('sale_indicator', filter=Q(sale_indicator__exact=0)),
    'total_price_sum': Round(Sum('total_price'), precision=2),
    'net_profit': Round(Sum('profit') + Sum('tax'), precision=2),
    'gross_profit': Round(Sum('profit') + Sum('tax'), precision=2)
}


def get_quotes_summary(qs) -> dict:
    
    results = qs.values('test_group').annotate(**summary).order_by()
    
    return results


def get_quotes_summary_total(qs) -> dict:
    return qs.aggregate(**summary)
