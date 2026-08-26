from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        return ['home', 'about', 'contact', 'service', 'gallery', 'heritage']

    def location(self, item):
        return reverse(item)

    # 🌟 डेटाबेस (django_site) की 500 एरर को रोकने के लिए यह override करें
    def get_urls(self, page=1, site=None, protocol=None):
        class DummySite:
            domain = 'shubham-pandit-website.vercel.app'
            name = 'Shubham Pandit'
        return super().get_urls(page=page, site=DummySite(), protocol='https')