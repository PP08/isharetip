from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

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
    images = models.ImageField()
    body = RichTextUploadingField(config_name='awesome_ckeditor')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #

    class Meta:
        db_table = "Post"

