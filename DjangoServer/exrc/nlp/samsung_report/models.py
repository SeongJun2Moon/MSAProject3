from django.db import models

class SamsungReport(models.Model):
    use_in_migrations = True

    id = models.IntegerField(primary_key=True)
    rank = models.TextField()
    word = models.TextField()
    count = models.TextField()

    class Meta:
        db_table = "samsung_report"

    def __str__(self):
        return f"{self.id} {self.rank} {self.word} {self.count}"
