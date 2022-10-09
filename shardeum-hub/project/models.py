from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class ShardeumProjects(models.Model):
    project_name       = models.CharField(max_length = 50)
    ticker             = models.CharField(max_length = 50)
    email_address      = models.CharField(max_length = 50)
    website            = models.CharField(max_length = 50)
    description        = models.CharField(max_length = 300)
    logo_relative_path = models.CharField(max_length = 50)
    twitter_handle     = models.CharField(max_length = 50)
    discord_username   = models.CharField(max_length = 50)
    cat_defi           = models.BooleanField()
    cat_nft            = models.BooleanField()
    cat_gamefi         = models.BooleanField()
    #registered_date    = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.project_name
    class Meta:
        ordering = ['-project_name']