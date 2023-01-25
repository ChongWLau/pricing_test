from django.contrib import admin
from django.db.models import Count, Q, Sum, F

from .models import Quotes


# Register your models here.
@admin.register(Quotes)
class DashboardViewAdmin(admin.ModelAdmin):
    change_list_template = 'admin/quotes_change_list.html'
    
    def changelist_view(self, request, extra_content=None):
        response = super().changelist_view(
            request, extra_context=extra_content
        )
        
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        
        summary = {
            'sales_count': Count('sale_indicator', filter=Q(sale_indicator__exact=1)),
            'non_sales_count': Count('sale_indicator', filter=Q(sale_indicator__exact=0)),
            'total_price_sum': Sum('total_price'),
            'net_price_sum': Sum('net_price'),
            'gross_price_sum': F('total_price_sum') - F('net_price_sum')
        }
        
        response.context_data['quote_summary_total'] = \
            qs.values('test_group').annotate(**summary).order_by()

        return response