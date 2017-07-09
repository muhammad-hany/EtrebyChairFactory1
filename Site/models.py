from django.db import models


class Chair(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500)


    def __str__(self):
        return self.name



class ChairImages(models.Model):
    image=models.ImageField(upload_to='chairs')
    chair=models.ForeignKey(Chair,on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name+' of chair-'+str(self.chair.id)

    def photo_tag(self):
        return '<img src="%s"/>' %(self.image.url)
    photo_tag.short_description='Image'
    photo_tag.allow_tags=True