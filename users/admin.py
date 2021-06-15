from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from csv_export.views import CSVExportView
from django.utils.html import format_html


class UserAdminClass(UserAdmin):
    @staticmethod
    def photo(obj):
        return format_html(
            '<img src="{}" width="40" />'.format(obj.image.url))

    actions = ('export_data_csv',)
    list_display = ('email', 'photo', 'name', 'college_name')
    # search by following fields
    search_fields = ('email', 'name', 'college_name')
    list_filter = ('college_name', )
    # cannot be edited
    readonly_fields = ()

    # required features that should be overriding the UserAdmin,
    filter_horizontal = ()
    fieldsets = ()
    def export_data_csv(self, request, queryset):
        view = CSVExportView(queryset=queryset, fields='__all__')
        return view.get(request)

    export_data_csv.short_description = 'Export the Selected Data as CSV'


admin.site.register(User, UserAdminClass)

