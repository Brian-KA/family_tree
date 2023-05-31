from django.db import models

# one model for uploading member data // admin.
class FamilyMember(models.Model):
    name        = models.CharField(max_length=100)
    photo       = models.ImageField(upload_to='family_photos/')
    parent      = models.CharField(max_length=100)
    siblings    = models.CharField(max_length=100)
    children    = models.CharField(max_length=100)
    dead        = models.BooleanField(default=False)
