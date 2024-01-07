from django.db import models

# Create your models here.


class Server(models.Model):
    address = models.CharField(
        verbose_name="Adres",
        max_length=500,
    )
    user = models.CharField(
        verbose_name="Kullanıcı Adı",
        max_length=500,
    )
    password = models.CharField(
        verbose_name="Şifre",
        max_length=500,
    )

    def __str__(self) -> str:
        return self.address

    class Meta:
        verbose_name = "Server"
        verbose_name_plural = "Serverlar"
