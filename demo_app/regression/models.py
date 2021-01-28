from django.db import models
import csv
from io import StringIO
import pandas as pd
import math

# Create your models here.
class csvInput(models.Model):
    def __str__(self):
        return self.task
    task = models.CharField(max_length=20)
    csv_file = models.FileField(upload_to="csv_file")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)
    def get_data(self):
        file = self.csv_file.read().decode('utf-8')
        data = csv.reader(StringIO(file), delimiter=',')
        data=pd.DataFrame(list(data))
        return(data.to_html())

            
