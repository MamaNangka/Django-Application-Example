from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    portofolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class Pekerjaan(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name


class daftartabel(models.Model):
    nama = models.CharField(max_length=500)
    usia = models.CharField( max_length=100)
    alamat = models.CharField( max_length=1000)
    pekerjaan = models.ForeignKey(Pekerjaan, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama +' - '+ self.usia +' - '+ self.alamat
