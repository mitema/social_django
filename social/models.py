from django.db import models

class Profile(models.Model):
    text = models.CharField(max_length=4096)

    def __str__(self):
        if self.member:
            return self.member.username + ": " + self.text
        return self.text

class Member(models.Model):
    username = models.CharField(max_length=16,primary_key=True)
    password = models.CharField(max_length=16)
    profile = models.OneToOneField(Profile, null=True)
    following = models.ManyToManyField("self", symmetrical=False)

    def __str__(self):
        return self.username

class Messages(models.Model):
    ID =  models.AutoField(primary_key=True) 
    auth = models.CharField(max_length=16)
    recip = models.CharField(max_length = 16)
    pm = models.BooleanField()
    time = models.DateTimeField()
    message = models.CharField(max_length=4096)
    
    def __str__(self):
        return self.message