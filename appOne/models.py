from django.db import models

# Create your models here.
class Record(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    client_first_name = models.CharField(max_length=60)
    client_last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=60)

    def __str__(self) -> str:
        return f"{self.client_first_name} "
    
