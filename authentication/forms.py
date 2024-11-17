from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    no_hp = forms.CharField(max_length=15, label='No HP')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class RegisterPenggunaForm(UserCreationForm):
    no_hp = forms.CharField(max_length=15, label='No HP')
    tgl_lahir = forms.DateField(label='Tanggal Lahir', widget=forms.DateInput(attrs={'type': 'date'}))
    alamat = forms.CharField(widget=forms.Textarea, label='Alamat')

    class Meta:
        model = User
        fields = ['username', 'no_hp', 'password1', 'password2', 'tgl_lahir', 'alamat']

class RegisterPekerjaForm(UserCreationForm):
    no_hp = forms.CharField(max_length=15, label='No HP')
    tgl_lahir = forms.DateField(label='Tanggal Lahir', widget=forms.DateInput(attrs={'type': 'date'}))
    alamat = forms.CharField(widget=forms.Textarea, label='Alamat')
    nama_bank = forms.ChoiceField(choices=[('GoPay', 'GoPay'), ('OVO', 'OVO'), ('VA_BCA', 'Virtual Account BCA'), ('VA_BNI', 'Virtual Account BNI'), ('VA_Mandiri', 'Virtual Account Mandiri')], label='Nama Bank')
    no_rekening = forms.CharField(max_length=20, label='No Rekening')
    npwp = forms.CharField(max_length=15, label='NPWP')
    foto_url = forms.URLField(label='URL Foto', required=True)

    class Meta:
        model = User
        fields = ['username', 'no_hp', 'password1', 'password2', 'tgl_lahir', 'alamat', 'nama_bank', 'no_rekening', 'npwp', 'foto_url']

class UpdatePenggunaForm(forms.Form):
    username = forms.CharField(max_length=150)
    no_hp = forms.CharField(max_length=15)
    tgl_lahir = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    alamat = forms.CharField(widget=forms.Textarea)

class UpdatePekerjaForm(UpdatePenggunaForm):
    nama_bank = forms.ChoiceField(choices=[
        ('GoPay', 'GoPay'),
        ('OVO', 'OVO'),
        ('VA_BCA', 'Virtual Account BCA'),
        ('VA_BNI', 'Virtual Account BNI'),
        ('VA_Mandiri', 'Virtual Account Mandiri')
    ])
    no_rekening = forms.CharField(max_length=20)
    npwp = forms.CharField(max_length=15)
    foto_url = forms.URLField(required=False)