from django.db import models

# Create your models here.

#모델
#모델의 이름은 단수, 첫글자는 대문자로 쓴다
class Candidate(models.Model):
    name = models.CharField(max_length=10)
    introduction = models.TextField()
    area = models.CharField(max_length=15)
    party_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name
        
