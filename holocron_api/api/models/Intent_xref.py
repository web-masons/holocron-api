from django.db import models
from django.utils.translation import string_concat
from standard import Placement
from Intent import Intent

class Intent_xref(models.Model):
    i_key = models.ForeignKey(Intent)
    p_key = models.OneToOneField(Placement)

    def __str__(self):
        return string_concat(self.i_key, " - ", self.p_key)