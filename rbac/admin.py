from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group, Permission
from django.db.models.query import Q
from .models import User
from .forms import UserCreationNewForm, UserChangeNewForm

class UserNewAdmin(UserAdmin):
    add_form = UserCreationNewForm
    form = UserChangeNewForm
    model = User 
    ordering = ['-id']
    list_display = ('id', 'is_superuser', 'email', 'first_name', 'middle_name', 'last_name', 'get_roles', 'is_staff', 'is_active')

    # Fields/Permissions for User creation form.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'middle_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
    )

    # Fields/Permissions for User change form.
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'middle_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
    )

    def get_roles(self, obj):
        '''custom attribute/column/key to get roles assigned to the user'''
        return ", ".join([group.name for group in obj.groups.all()])
    get_roles.short_description = 'Roles'
    
    
    def has_change_permission(self, request, obj=None):
        '''Allow change permission for superusers only if the user is a superuser'''
        if obj and obj.is_superuser and not request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        '''Allow delete permission for superusers only if the user is a superuser'''
        if obj and obj.is_superuser and not request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)


class LimitedGroupAdmin(GroupAdmin):
    '''Limit the permissions displayed based on the group's permissions if current user is not a superuser'''
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            # Retrieve only permissions related to a specific app or model
            # For example, let's say we want to limit to permissions for 'rbac'
            limited_permissions = Permission.objects.filter(Q(content_type__app_label__in=['rbac']) | Q(content_type__model__in=['group'])).exclude(Q(codename__in=['delete_group']))
            form.base_fields['permissions'].queryset = limited_permissions
        return form


admin.site.register(User, UserNewAdmin)

# Unregister the original Group admin from auth
admin.site.unregister(Group)
# Register the new Limited Group admin
admin.site.register(Group, LimitedGroupAdmin)

# Customized title and header message for admin-webpage
admin.site.index_title="RBAC"
admin.site.site_title="Role Based Access Control"
admin.site.site_header="RBAC Assessment | VRV Security's"