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

    # def __init__(self, *args, **kwargs):
    #     import ipdb; ipdb.set_trace()
    #     self.user = User.objects.create_user(username=kwargs['username'],
    #                                          email=kwargs['email'],
    #                                          password=kwargs['password'])
    #     self.type = kwargs['type']

    #     if kwargs['type'] == "Student":
    #         self.avatar = kwargs['avatar']
    #         try:
    #             self.student_info = StudentCard.objects.get(card_id=kwargs['student_card'])
    #         except StudentCard.DoesNotExists:
    #             raise Exception("No such student in base")
    #     elif kwargs['type'] == "Teacher":
    #         if 'avatar' in kwargs:
    #             self.avatar = kwargs['avatar']
