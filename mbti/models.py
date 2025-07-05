from django.db import models


from django.db import models

class MBTIType(models.Model):
    name = models.CharField(max_length=4)  # e.g., INFP, ESTJ
    description = models.TextField()
    logic = models.IntegerField()
    imagination = models.IntegerField()
    discipline = models.IntegerField()
    # Add other traits as needed

    def __str__(self):
        return self.name

