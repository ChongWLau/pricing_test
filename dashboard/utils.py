from django.db.models import Count, Q, Sum
from django.db.models.functions import Round, ExtractWeekDay, ExtractWeek


summary = {
    'sales_count': Count('sale_indicator', filter=Q(sale_indicator__exact=1)),
    'non_sales_count': Count('sale_indicator', filter=Q(sale_indicator__exact=0)),
    'total_price_sum': Round(Sum('total_price'), precision=2),
    'net_profit': Round(Sum('profit') + Sum('tax'), precision=2),
    'gross_profit': Round(Sum('profit') + Sum('tax'), precision=2)
}


def get_quotes_summary(qs, split_by: str) -> dict:
    return qs.values(split_by).annotate(**summary).order_by()


def get_quotes_summary_total(qs) -> dict:
    return qs.aggregate(**summary)


# def get_quotes_summary_by_day(qs):
#     return qs.values(
#         day=ExtractWeekDay('transaction_date')
#     ).annotate(
#         total_price_sum=Sum('total_price', distinct=True),
#     ).order_by('day')

# def get_quotes_summary_by_week(qs):
#     return qs.values(
#         day=ExtractWeek('transaction_date')
#     ).annotate(
#         total_price_sum=Sum('total_price', distinct=True),
#     ).order_by('week')

# values(week=ExtractWeek('transaction_date')).annotate(total_price_sum=Sum('total_price', distinct=
# True)).order_by('week')