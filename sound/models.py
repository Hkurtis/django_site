from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=250)
    show_num = models.CharField(max_length=1000)
    hosts = models.CharField(max_length=250)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.title + '- hosted by ' + self.hosts
#the actual podcast file
class Pod(models.Model):
    show = models.ForeignKey(Show, on_delete = models.CASCADE)
    title = models.CharField(max_length=250)
    file_type = models.CharField(max_length=10)#wav

    def __str__(self):
        return self.title 
