from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Instrument(models.Model):
    CATEGORY_CHOICES = [
        ('Guitarras', 'Guitarras'),
        ('Violões', 'Violões'),
        ('Baixos', 'Baixos'),
        ('Baterias e pratos', 'Baterias e pratos'),
        ('Cavaquinhos', 'Cavaquinhos'),
        ('Teclados e pianos', 'Teclados e pianos'),
        ('Violinos e violoncellos', 'Violinos e violoncellos'),
        ('Instrumentos de sopro', 'Instrumentos de sopro'),
        ('Amplificadores e microfones', 'Amplificadores e microfones'),
        ('Outros instrumentos', 'Outros instrumentos'),
        ('Acessórios', 'Acessórios'),
    ]


    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name= 'instrument_brand', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Outros instrumentos')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    condition = models.CharField(max_length=20, choices=[('novo', 'Novo'), ('usado', 'Usado'), ('recondicionado', 'Recondicionado')])
    photo = models.ImageField(upload_to = 'instruments/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model
    
class InstrumentInventory(models.Model):
    instruments_count = models.IntegerField()
    instruments_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [ '-created_at']

    def __str__(self):
        return f'{self.instruments_count} - {self.instruments_value}'