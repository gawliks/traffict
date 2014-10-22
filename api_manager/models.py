import re
import simplejson as json
from django.core.validators import ValidationError
from django.db import models


def _validate_base_url(v):
    r = (re.compile("^http(s)?://.+$"))
    if not r.match(v):
        raise ValidationError(
            u'Invalid ULR format: %(value)s',
            code="url:invalid",
            params={'value': v}
        )

class Api(models.Model):

    name = models.CharField(max_length=32)
    base_url = models.CharField(max_length=64, validators=[_validate_base_url])

    def __unicode__(self):
        return self.name


def _validate_body(v):
    try:
        json.loads(v)
    except json.JSONDecodeError as e:
        raise ValidationError(
            u'Body: %(value)s is not a proper json object',
            code="body:invalid",
            params={'value': v}
        )

class Query(models.Model):

    api = models.ForeignKey(Api)
    method = models.CharField(
        max_length=6,
        choices=(
            ('GET', 'GET'),
            ('POST', 'POST'),
            ('PUT', 'PUT'),
            ('DELETE', 'DELETE')
        ),
        default='GET'
    )
    url = models.CharField(max_length=64, null=True, blank=True)
    body = models.TextField(validators=[_validate_body], null=True, blank=True)

    def __unicode__(self):
        return "{0}:{1}/{2}".format(self.id, self.api.base_url, self.url)
