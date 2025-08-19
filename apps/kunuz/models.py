from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    views = models.PositiveIntegerField(default=0)
    video_url = models.URLField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    area = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

class Categories(models.Model):
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class PostCategory(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = "Post category"
        verbose_name_plural = "Post categories"




