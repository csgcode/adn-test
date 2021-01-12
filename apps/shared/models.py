from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class TimeStamp(models.Model):
    """
    Abstract model to extend timestamp fields for models
    """
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    """
    To save Tags used in the system
    """
    # TODO add a timestamp?
    title = models.CharField(_('Title'), max_length=120, unique=True)
