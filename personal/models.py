from django.db import models
from django.contrib.auth.models import User


TYPE_CHOICES = (
    ("teacher", "teacher"),
    ("student", "student"),
    ("stranger", "stranger")
)


class Group(models.Model):
    name = models.CharField(max_length=16)
    teachers = models.ManyToManyField('Profile', blank=True)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.name


class StudentCard(models.Model):
    card_id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    group = models.ForeignKey(Group)

    def __str__(self):
        return "%s - %s %s (%s)" % (self.card_id, self.name, self.surname, self.group.name)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, blank=False)

    avatar = models.ImageField("avatar", upload_to="avatar/", blank=True)
    student_info = models.ForeignKey(StudentCard, blank=True)
