from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:131]

    def pub_date_pretty(self):
        return self.pub_date.strftime("%d-%m-%Y")

    def __str__(self):
        return self.title

