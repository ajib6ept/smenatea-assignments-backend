from django.db import models

CHECK_TYPES = (("kitchen", "kitchen"), ("client", "client"))
CHECK_STATUSES = (
    ("new", "new"),
    ("rendered", "rendered"),
    ("printed", "printed"),
)


class Printer(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100, unique=True)
    check_type = models.CharField(choices=CHECK_TYPES, max_length=7)
    point_id = models.IntegerField()

    def __str__(self):
        return self.name


class Check(models.Model):
    printer_id = models.ForeignKey(Printer, on_delete=models.PROTECT)
    type = models.CharField(choices=CHECK_TYPES, max_length=7)
    order = models.JSONField()
    status = models.CharField(choices=CHECK_STATUSES, max_length=8)
    pdf_file = models.FileField()
