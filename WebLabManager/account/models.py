from django.db import models
from django.conf import settings
import datetime

# from django.contrib.auth.models import User


USER_RANK_CHOICES=(
    ('UG', 'Under graduate'),
    ('MSc', 'MSC student'),
    ('PhD', 'PhD student'),
    ('RA/RF', 'Postdocs'),
    ('PI', 'PI'),
    ('Other', 'Other'),

)

USER_TYPE_CHOICES=(
    ('U', 'User'),
    ('A', 'Lab admin'),
)
STATUS_CHOICES=(
    ('NA', 'Non Active'),
    ('Active', 'Active'),
    ('New User', 'New'),
)
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    # photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    supervisor=models.CharField(max_length = 30)
    user_type = models.CharField(max_length = 10, choices = USER_TYPE_CHOICES, default = 'Non Active')
    position = models.CharField(max_length = 10, choices = USER_RANK_CHOICES, default = 'Other')
    CID=models.IntegerField(null=True, blank=True)
    join_date = models.DateField(default=datetime.date(1977,7,25))
    status=models.CharField(max_length=8, choices=STATUS_CHOICES, default='Active')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
