from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, dni, password, **extra_fields):
        if not dni:
            raise ValueError('El correo electrónico es necesario.')
        email = self.normalize_email(dni)
        user = self.model(dni=dni, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, dni, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El supersusuario debe tener is_staff = True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser = True.')
        return self.create_user(dni, password, **extra_fields)
