# # core/models.py
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# import uuid

# class User(AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     nama = models.CharField(max_length=255)
#     jenis_kelamin = models.CharField(max_length=1, choices=[('L', 'Laki-laki'), ('P', 'Perempuan')])
#     no_hp = models.CharField(max_length=15, unique=True)
#     tgl_lahir = models.DateField()
#     alamat = models.TextField()
#     saldo_mypay = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
#     # Override username field to use no_hp instead
#     username = None
#     USERNAME_FIELD = 'no_hp'
#     REQUIRED_FIELDS = ['nama', 'jenis_kelamin', 'tgl_lahir', 'alamat']
    
#     def __str__(self):
#         return self.nama

# class TimeStampedModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True