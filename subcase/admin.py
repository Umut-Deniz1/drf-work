from django.contrib import admin

from subcase.models import Organizations, Users, Transactions
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(Organizations)
# admin.site.register(Users)
admin.site.register(Transactions)

class UsersResource(resources.ModelResource):
    class Meta:
        model = Users


class UsersAdmin(ImportExportModelAdmin):
    resource_class = UsersResource
admin.site.register(Users, UsersAdmin)