from django.contrib import admin
from .models import Legal

class LegalAdmin(admin.ModelAdmin):
    ''' Register and display all fields in the correct order for the various 'legal' sections '''
    list_display = (
        'name',
        'titleprivacypolicy',
        'bodyprivacypolicy',
        'titletermsandconditions',
        'bodytermsandconditions',
        'titlereturnspolicy',
        'bodyreturnspolicy'
    )

    ordering = ('name', 'titleprivacypolicy', 'bodyprivacypolicy',
    'titletermsandconditions', 'bodytermsandconditions', 'titlereturnspolicy', 'bodyreturnspolicy')

admin.site.register(Legal, LegalAdmin)
