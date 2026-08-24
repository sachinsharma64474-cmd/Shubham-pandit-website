from django.db import models




class Gallery(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    subtitle = models.CharField(max_length=255)
    media = models.FileField(upload_to='gallery/')
    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_TYPE_CHOICES,
        default='image'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subtitle

# Create your models here.
