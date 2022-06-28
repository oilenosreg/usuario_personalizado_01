from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustormUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('dni', 'apellidos', 'nombres', 'email', 'is_staff', 'is_active',)
    list_filter = ('dni', 'apellidos', 'nombres', 'email', 'is_staff', 'is_active',)
    # Muestra la información relacionada del modelo dentro del formulario de detalle.
    fieldsets = (
        (
            'Cuenta de usuario', {
            'fields': ('dni', 'nombres', 'apellidos', 'email', 'password')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active')
        }),
    )
    # Indica los campos que se mostrarán en la página de creación del usuario.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'dni', 'nombres', 'apellidos', 'email', 'password1', 'password2', 'is_staff', 'is_active'
            ),
        }),
    )
    search_fields = ('apellidos',)
    ordering = ('apellidos',)


admin.site.register(CustomUser, CustormUserAdmin)

