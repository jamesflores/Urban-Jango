from django.db import models


class SearchLog(models.Model):
    query = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    referrer = models.URLField(max_length=1024, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.timestamp}] {self.query} from {self.ip_address} via {self.referrer}"
