from django.db import models
from django.contrib.auth.models import User
import random, string

def generate_random_id():
    return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(6))

# extends the User class to hold additional profile info
# access with u.hacker.github (where u is user object instance)
class Hacker(models.Model):
    user = models.OneToOneField(User)
    avatar_url  = models.CharField(max_length=400, blank=True)
    github      = models.CharField(max_length=200, blank=True)
    twitter     = models.CharField(max_length=200, blank=True)

class Blog(models.Model):

    def __unicode__(self):
        return self.feed_url

    user         = models.ForeignKey(User)
    url          = models.CharField(max_length=200)
    feed_url     = models.CharField(max_length=200)
    last_crawled = models.DateTimeField('last crawled', blank=True, null=True)
    created      = models.DateTimeField('date created')

class Post(models.Model):

    def __unicode__(self):
        return self.title

    blog         = models.ForeignKey(Blog)
    url          = models.CharField(max_length=400)
    title        = models.CharField(max_length=200, blank=True)
    content      = models.TextField()
    date_updated = models.DateTimeField('date updated')
    slug         = models.CharField(max_length=6, default=generate_random_id, unique=True)

class Comment(models.Model):

    def __unicode__(self):
        return self.content[:40]

    slug            = models.CharField(max_length=6, default=generate_random_id, unique=True)
    user            = models.ForeignKey(User)
    post            = models.ForeignKey(Post)
    parent          = models.ForeignKey('self', blank=True, null=True)
    date_modified   = models.DateTimeField('date modified')
    content         = models.TextField()