from django.db import models

# Create your models here.
class csvInput(models.Model):
    task = models.CharField(max_length=20)
    csv_file = models.FileField(upload_to="csv_file")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)
   