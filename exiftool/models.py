from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Batch(models.Model):
    uuid = models.CharField(_("UUID"), max_length=100)
    excel = models.FileField(_("Excel File"))

    class Meta:
        verbose_name = _("batch")
        verbose_name_plural = _("batches")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("batch_detail", kwargs={"pk": self.pk})


# Create your models here.
class Picture(models.Model):
    STATUSES = (
        ('PENDING','PENDING'),
        ('PROCESSING','PROCESSING'),
        ('SUCCESS','SUCCESS'),
        ('FAILURE','FAILURE')
    )
    image = models.ImageField(_("Image"))
    batch = models.ForeignKey(Batch, verbose_name=_("Batch"), on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUSES, default="PENDING")

    class Meta:
        verbose_name = _("picture")
        verbose_name_plural = _("pictures")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("picture_detail", kwargs={"pk": self.pk})
