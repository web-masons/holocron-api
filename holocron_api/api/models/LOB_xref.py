from django.db import models
from django.utils.translation import string_concat
from standard import Placement
from LOB import LOB

class LOB_xref(models.Model):
    lob_key = models.ForeignKey(LOB)
    p_key = models.OneToOneField(Placement)

    def __str__(self):
        return string_concat(self.lob_key, " - ", self.p_key)