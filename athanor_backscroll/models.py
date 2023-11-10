from django.db import models


class BackscrollRecord(models.Model):
    character = models.ForeignKey(
        "objects.ObjectDB", related_name="backscroll_records", on_delete=models.CASCADE
    )
    text = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
