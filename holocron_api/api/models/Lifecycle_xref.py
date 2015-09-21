from django.db import models
from django.utils.translation import string_concat
from standard import Placement
from Lifecycle import LifeCycle


class Lifecycle_xref(models.Model):
    lc_key = models.ForeignKey(LifeCycle, on_delete=models.PROTECT)
    p_key = models.OneToOneField(Placement)

    def __str__(self):
        return string_concat(self.lc_key, " - ", self.p_key)
