from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class MBTIType(models.Model):
    name = models.CharField(max_length=4, unique=True)  # e.g., INFP, ESTJ
    description = models.TextField()
    logic = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    imagination = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    discipline = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    # Add other traits as needed

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(logic__gte=0) & models.Q(logic__lte=100),
                name="mbti_logic_between_0_100",
            ),
            models.CheckConstraint(
                condition=models.Q(imagination__gte=0) & models.Q(imagination__lte=100),
                name="mbti_imagination_between_0_100",
            ),
            models.CheckConstraint(
                condition=models.Q(discipline__gte=0) & models.Q(discipline__lte=100),
                name="mbti_discipline_between_0_100",
            ),
        ]

    def __str__(self):
        return self.name
