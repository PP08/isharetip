import io
from PIL import Image
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.files.base import ContentFile
# Create your models here.
from io import BytesIO
from django.core.files.base import ContentFile


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Category"

class Author(models.Model):
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.author

    class Meta:
        db_table = "Author"

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    intro = models.CharField(max_length=200)
    image = models.ImageField()
    body = RichTextUploadingField(config_name='awesome_ckeditor')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if self.image:
    #         img_io = io.StringIO()
    #         image = Image.open(self.image)
    #         image = crop(image)
    #         image.save(img_io, format='PNG', quality=100)
    #         img_content = ContentFile(img_io.getvalue(), 'img5.jpg')
    #         self.image = img_content
    #
    #         super(Post, self).save(*args, **kwargs)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        img = Image.open(self.image)
        resized = crop(img)
        new_image_io = BytesIO()

        if img.format == 'JPEG':
            resized.save(new_image_io, format='JPEG')
        elif img.format == 'PNG':
            resized.save(new_image_io, format='PNG')

        temp_name = self.image.name
        self.image.delete(save=False)

        self.image.save(
            temp_name,
            content=ContentFile(new_image_io.getvalue()),
            save=False
        )
        super(Post, self).save()

    class Meta:
        db_table = "Post"

def crop(im,aspect_ratio=1):
    try:
        imagex = int(im.size[0])
        imagey = int(im.size[1])
        width = min(imagex, imagey*aspect_ratio)
        height = min(imagex/aspect_ratio, imagey)
        left =(imagex - width)/2
        top = (imagey - height)/2
        box = (left,top,left+width,top+height)
        im = im.crop(box)
    except:
        pass
    return im