# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile, Toolkit, Invites

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    # Display user_type and email in the list view
    list_display = ('email', 'username', 'user_type', 'is_staff')
    list_filter = ('user_type',)

    # Use email for searching
    search_fields = ('email', 'username')

    # Specify what fields to use in forms (very important for custom User)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)  # Register your custom one


@admin.register(Toolkit)
class ToolkitAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'level')
    list_filter = ('content_type', 'level')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}  # auto-generate slug
    filter_horizontal = ('tags',)  # for better tag selection

@admin.register(Invites)
class InvitesAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
