from django.db import models

class HeritagePlace(models.Model):
    title = models.CharField(
        max_length=255,
        help_text="Example: Mahakal Mandir"
    )

    description = models.TextField(
        help_text="Example: Ujjain ka prasiddh Jyotirling Mahakal Mandir."
    )

    image = models.ImageField(
        upload_to="heritage_images/",
        help_text="Card header image"
    )

    slug = models.SlugField(
        unique=True,
        help_text="URL friendly name (e.g., mahakal-mandir)"
    )

    google_map_url = models.URLField(
        blank=True,
        null=True,
        help_text="Google Maps Embed URL"
    )

    live_darshan_url = models.URLField(
        blank=True,
        null=True,
        help_text="YouTube Live Embed URL"
    )

    class Meta:
        verbose_name = "Heritage Place"
        verbose_name_plural = "Heritage Places"

    def __str__(self):
        return self.title