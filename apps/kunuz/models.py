from django.db import models



class Managers(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='managers/')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'


class Categories(models.Model):
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tags(models.Model):
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    views = models.PositiveIntegerField(default=0)
    video_url = models.URLField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True, upload_to="posts/")
    area = models.CharField(max_length=255)
    tags = models.ManyToManyField(
        Tags,
        related_name='posts'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

class PostCategory(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = "Post category"
        verbose_name_plural = "Post categories"