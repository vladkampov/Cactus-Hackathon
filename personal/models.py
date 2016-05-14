from django.db import models
from django.contrib.auth.models import AbstractUser


TYPE_CHOICES = (
    ("Teacher", "Teacher"),
    ("Student", "Student"),
    ("Stranger", "Stranger")
)


class Group(models.Model):
    name = models.CharField(max_length=16)
    teachers = models.ManyToManyField('Profile')

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.name


class StudentCard(models.Model):
    card_id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=50, required=True)
    surname = models.CharField(max_length=50, required=True)
    group = models.ForeignKey(Group)

    def __str__(self):
        return "%s - %s %s (%s)" % (self.card_id, self.name, self.surname, self.group.name)


class Profile(AbstractUser):
    type = models.CharField(choices=TYPE_CHOICES, required=True)

    avatar = models.ImageField(ubpload_to="avatar/", blank=True)
    student_info = models.ForeignKey(StudentCard, blank=True)

    def __init__(self, login, email, _type, **kwargs):
        self.login = login
        self.email = email
        self.type = _type

        if _type == "Student":
            self.avatar = 
