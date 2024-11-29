from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.apps import apps
from django.db.models.query import Q

class UserForm(forms.ModelForm):
    '''Common form to limit user_permissions field to show only limited (allowed) permissions'''
    class Meta:
        model = User
        # Include all fields
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get the auth & Permission model
        Permission = apps.get_model('auth', 'Permission')
        limited_permissions = Permission.objects.filter(Q(content_type__app_label__in=['rbac']) | Q(content_type__model__in=['group'])).exclude(Q(codename__in=['delete_group']))
        self.fields['user_permissions'].queryset = limited_permissions


class UserCreationNewForm(UserForm, UserCreationForm):
    '''Form to Create User with customized settings'''
    ...

class UserChangeNewForm(UserForm, UserChangeForm):
    '''Form to Change/Update User with customized settings'''
    ...