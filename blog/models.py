from django.db import models

# Create your models here.
# https://azinkin.ru/orm.html

class Category(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'


class Post(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    content = models.TextField(
        verbose_name='контент',
        blank=True,
    )
    picture = models.ImageField(
        verbose_name='картинка',
        blank=True,
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=False,
    )
    category = models.ForeignKey(
        verbose_name='категория',
        to='Category',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'публикации'
        unique_together = ('category', 'slug')
    class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['user', 'post']]

    def __str__(self):  # Исправлено на __str__
        return f"{self.user} likes {self.post}"


class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):  # Исправлено на __str__
        return f"Donation by {self.user.username}: ${self.amount}"
