from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.core.validators import MinLengthValidator, RegexValidator
from .models import Usuario, Rol, Genero

class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Contraseña',
        validators=[
            MinLengthValidator(limit_value=8, message='La contraseña debe tener al menos 8 caracteres.'),
            RegexValidator(
                regex='^(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$',
                message='La contraseña debe contener al menos un número, una mayúscula y un carácter especial.'
            ),
            # Agrega otras validaciones según tus requisitos
        ]
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Confirmar contraseña',
        help_text='Ingrese la misma contraseña que antes, para verificación.'
    )

    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'rol', 'genero']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        # Asigna los valores del formulario a los campos adicionales de Usuario
        user.name = self.cleaned_data['first_name']
        user.lastname = self.cleaned_data['last_name']
        user.rol = self.cleaned_data['rol']
        user.genero = self.cleaned_data['genero']

        if commit:
            user.save()

        return user
