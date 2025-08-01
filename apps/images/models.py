from django.db import models
from django.contrib.auth.models import User

class PathologyImage(models.Model):
    STAIN_CHOICES = [
        ('H&E', 'Hematoxylin and Eosin'),
        ('IHC', 'Immunohistochemistry'),
        ('SPECIAL', 'Special Stain'),
    ]
    
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pathology_images/')
    stain_type = models.CharField(max_length=10, choices=STAIN_CHOICES)
    magnification = models.CharField(max_length=10)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    case_id = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.title} - {self.case_id}"
    
    class Meta:
        ordering = ['-upload_date']
