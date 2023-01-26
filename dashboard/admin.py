from django.contrib import admin
from django.db.models import Count, Q, Sum, F

from .models import Quotes
from .utils import get_quotes_summary


# Register your models here.
@admin.register(Quotes)
class DashboardViewAdmin(admin.ModelAdmin):
    change_list_template = 'admin/quotes_change_list.html'
    
    def changelist_view(self, request, extra_content=None):
        response = super().changelist_view(
            request, extra_context=extra_content
        )
        
        # try:
        #     qs = response.context_data['cl'].queryset
        # except (AttributeError, KeyError):
        #     return response
        
        response.context_data['quote_summary_total'] = get_quotes_summary()

        return response