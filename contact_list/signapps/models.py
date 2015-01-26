from django.db import models

class Info(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    #last_name = models.CharField(max_length=128, null=True, blank=True)
    if last_name == 'null' or last_name == 'blank':
        last_name = ""
    email = models.EmailField(null=True, blank=True)
    if email == 'null' or email == 'blank':
        email = ""
    def __unicode__(self):
        return self.first_name