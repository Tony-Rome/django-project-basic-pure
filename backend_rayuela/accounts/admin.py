from django.contrib import admin
from .models import Writer
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class WriterCreationForm(forms.ModelForm):  # Formulario para crear usuarios
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = Writer
        fields = ('email', 'first_name', 'last_name', 'web_site', 'signing', 'user_permissions')

    def clean_password2(self):  # Verifica si coinciden  pass

        password1 = self.cleaned_data.get("password1")  # Obtiene y limpia
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords must match")
        return password2

    def save(self, commit=True):  # Guarda password hasheado

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user


class WriterChangeForm(forms.ModelForm):  # Formulario solo para modificar datos de usuarios
    '''
        Formulario para actualizar usuarios admin
    '''

    password = ReadOnlyPasswordHashField

    class Meta:
        model = Writer
        fields = "__all__"

    def clean_password(self):  # El campo del form no tiene acceso al valor incial, por ende se debe hacer a través de esta funcion
        return self.initial["password"]


class WriterAdmin(BaseUserAdmin):

    form = WriterChangeForm
    add_form = WriterCreationForm

    list_display = ['first_name', 'last_name', 'timestamp', 'writer_level']
    list_filter = ('is_admin',)

    ''' Campos que se muestran para administrar usuarios '''
    readonly_fields = ('timestamp',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'writer_level')}),
        ('Permissions', {'fields': ('is_admin', 'user_permissions')}),
    )

    ''' Campos que se muestran para agregar un usuario nuevo '''
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name',
                       'last_name', 'writer_level', 'signing', 'web_site', 'user_permissions',
                       'is_admin', 'is_staff', 'is_active',
                       )
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()  # opciones de filtro al costado izq.


admin.site.register(Writer, WriterAdmin)

admin.site.unregister(Group)