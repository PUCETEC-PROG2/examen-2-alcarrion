from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50, null=False)
    genre = models.CharField(max_length=30, null= False)
    direct = models.CharField(max_length=30, null= False)
    year = models.IntegerField()
    synopsis = models.TextField(max_length=1000, null= False)
    
    def __srt__(self) -> str:
        return self.title
    
    

