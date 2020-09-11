from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    contact_no = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=20)
    pro_pic = models.ImageField(upload_to='users/pro_pics', blank=True, null=True, default='users/pro_pics/default.jpg')
    portfolio_url = models.URLField(blank=True, null=True)
    cv = models.FileField(upload_to='users/cv', blank=True, null=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username