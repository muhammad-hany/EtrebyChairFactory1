from django.db import models


class Chair(models.Model):
    name = models.CharField(max_length=50, blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=False)
    description = models.TextField(max_length=800, blank=False)
    price = models.CharField(max_length=50, blank=False, default="price")
    fcl = models.CharField(max_length=50, blank=False, default="fcl")
    height = models.CharField(max_length=50, blank=False, default="height")
    seat_height = models.CharField(max_length=50, blank=False, default="seat height")
    width = models.CharField(max_length=50, blank=False, default="width")
    depth = models.CharField(max_length=50, blank=False, default="depth")

    def __str__(self):
        return self.name


class ChairImages(models.Model):
    image = models.ImageField(upload_to='chairs', blank=False, null=False)
    chair = models.ForeignKey(Chair, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name + ' of chair-' + str(self.chair.id)

    def photo_tag(self):
        return '<img src="%s"/>' % (self.image.url)

    photo_tag.short_description = 'Image'
    photo_tag.allow_tags = True
