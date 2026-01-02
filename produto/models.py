from django.db import models
from django.conf import settings
from PIL import Image
import os

class Produto(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    nome = models.CharField(max_length=255)
    short_description = models.TextField(
        max_length=255, 
        blank=True, 
        null=True,
    )
    long_description = models.TextField(blank=True, null=True,)
    image = models.ImageField(
        upload_to='produto_imagems/%Y/%m', 
        blank=True, 
        null=True,
        )
    slug = models.SlugField(unique=True)
    marketing_price = models.FloatField()
    promotional_price = models.FloatField(default=0)
    category = models.CharField(
        default='V', max_length=1, 
        choices=[
            ('V', 'Variação'), ('S', 'Simples'),
        ]
    )

    @staticmethod
    def resize_image(img, size=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pill = Image.open(img_full_path)
        original_width, original_height = img_pill.size

        if original_width <= size:
            img_pill.close()
            return

        new_height = round((size * original_width) / original_width)
        new_img = img_pill.resize((size, new_height), Image.LANCZOS)

        new_img.save(
            img_full_path,
            optimize=True,
            quality=50,
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.image:
            self.resize_image(self.image, max_image_size)

    def __str__(self):
        return self.nome
    
class Variacao(models.Model):
    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'

    product = models.ForeignKey(Produto, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField()
    promotional_price = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.name or self.proctud.name