from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

# Usado para criar usuário
class CustomUserCreateForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'fone')
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1']) # Confirmar password
        user.email = self.cleaned_data['username'] # Colocar o E-mail como usernme

        if commit:
            user.save()

        return user

# Usado para modificar usuário
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'fone')