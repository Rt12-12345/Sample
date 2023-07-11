
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()



class CustomUser(User):
    class Meta:
        proxy = True


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    actions = ['block_users', 'unblock_users']

    def block_users(self, request, queryset):
        queryset.update(is_active=False)
    block_users.short_description = "Block selected users"

    def unblock_users(self, request, queryset):
        queryset.update(is_active=True)
    unblock_users.short_description = "Unblock selected users"

admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)



