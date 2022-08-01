from django.db import models



class Member(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
  

    def __str__(self):
        return self.name