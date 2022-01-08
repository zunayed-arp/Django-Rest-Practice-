from django.db import models
from django_resized import ResizedImageField
from PIL import Image



def productFile(instance, filename):
    return '/'.join( ['products', str(instance.id), filename] )

class Profile(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to=productFile,
        max_length=254, blank=True, null=True
    )
    
    # def save(self,*args,**kwargs):
    #     super(Profile,self).save(*args,**kwargs)
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width >300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image)
    
class UserProfile(models.Model):
    picture = models.ImageField(upload_to=productFile,)
    email = models.EmailField()
    
