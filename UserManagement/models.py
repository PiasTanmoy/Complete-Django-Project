from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    contact_no = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=20)
    pro_pic = models.ImageField(upload_to='users/pro_pics', blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    cv = models.FileField(upload_to='users/cv', blank=True, null=True)

    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    status = models.CharField(max_length=10, blank=True, null=True, default='False')

    def __str__(self):
        return self.user.username

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')

    message = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='users/chat/images', blank=True, null=True)
    file = models.FileField(upload_to='users/chat/files', blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.sender.username + " : " + self.receiver.username