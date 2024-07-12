from django.contrib import admin
from .models import ArticleNews, ArticleElon, ekranImages, ArticleQabul2024, CustomUser
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'birth_date')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)



admin.site.register(ArticleNews)

admin.site.register(ArticleElon)

admin.site.register(ekranImages)
admin.site.register(ArticleQabul2024)


# Group modelini admin panelidan olib tashlash
admin.site.unregister(Group)
