from django.contrib import admin

from .models import Quotes
from .utils import (
    get_quotes_summary_total, get_quotes_summary
)


# Register your models here.
class BaseSummaryAdmin(admin.ModelAdmin):
    list_filter = [
        'test_group', 'sale_indicator'
    ]


@admin.register(Quotes)
class DashboardViewAdmin(BaseSummaryAdmin):
    change_list_template = 'admin/quotes_change_list.html'
    
    def changelist_view(self, request, extra_content=None):
        response = super().changelist_view(
            request, extra_context=extra_content
        )
        
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        
        response.context_data['quote_summary_test_group'] = get_quotes_summary(qs, 'test_group')
        response.context_data['quote_summary_total'] = get_quotes_summary_total(qs)
        response.context_data['quote_summary_by_age'] = get_quotes_summary(qs, 'customer_age')
        # response.context_data['quote_summary_by_day'] = get_quotes_summary_by_day(qs)

        return response
