from django.contrib import admin
from echowave.models import * 


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    list_display_links = ["__str__"]
    search_fields = ["__str__"]


@admin.register(NotificationModel)
class NotificationModelAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    list_display_links = ["__str__"]
    search_fields = ["__str__"]


@admin.register(NotifyTypeModel)
class NotifyTypeModelAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    list_display_links = ["__str__"]
    search_fields = ["__str__"]
    