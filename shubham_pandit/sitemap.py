from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        # अपनी URLs के 'name' यहाँ लिखें (जैसे: home, about, contact, service)
        return ['home', 'about', 'contact', 'service', 'gallery', 'heritage']

    def location(self, item):
        return reverse(item)