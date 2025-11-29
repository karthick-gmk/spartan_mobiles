from django.contrib import admin
from usermanagement.models.user_model import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'first_name','phone','city', 'date_joined')
    search_fields = ('username',)
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined',)