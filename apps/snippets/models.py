from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from apps.shared.models import TimeStamp, Tag


# Create your models here.


class Snippet(models.Model):
    """
    Model to save short snippets for a user
    """
    title = models.CharField(_('Title'), max_length=120)
    code = models.CharField(_('Snippet Description'), max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snip_user')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True, related_name='snip_tag')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self._state.adding:
            #TODO logic on create - condition check for check the title
            pass
        super().save(*args, **kwargs)
