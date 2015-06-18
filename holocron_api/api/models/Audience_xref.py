from django.db import models
from django.utils.translation import string_concat
from standard import Placement
from Audience import Audience

class Audience_xref(models.Model):
    a_key = models.ForeignKey(Audience)
    p_key = models.OneToOneField(Placement)

    def __str__(self):
        return string_concat(self.a_key, " - ", self.p_key)