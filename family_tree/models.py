from django.db import models


# one model for uploading member data // admin.
class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='family_photos/')
    parent = models.CharField(max_length=100)
    siblings = models.ManyToManyField('self', blank=True)
    children = models.CharField(max_length=100)
    dob = models.DateField(default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100)
    dead = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# create many to many relationship between family members here
# class FamilyMember(models.Model):
#     name = models.CharField(max_length=100)
#     photo = models.ImageField(upload_to='family_photos/')
#     dob = models.DateField(default='')
#     email = models.EmailField(default='')
#     phone = models.CharField(max_length=100, default='')
#     dead = models.BooleanField(default=False)
#     parent = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='children')
#     siblings = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='related_siblings')
#
#     def __str__(self):
#         return self.name
#
#
# class Relationship(models.Model):
#     from_member = models.ForeignKey(FamilyMember, related_name='from_members', on_delete=models.CASCADE)
#     to_member = models.ForeignKey(FamilyMember, related_name='to_members', on_delete=models.CASCADE)
#     relationship_type = models.CharField(max_length=100)
#
#     def __str__(self):
#         return f"{self.from_member.name} - {self.relationship_type} - {self.to_member.name}"