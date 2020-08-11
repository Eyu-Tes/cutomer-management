from django.db import models
from django.urls import reverse


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'acc-customer'


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'acc-tag'


class Product(models.Model):
    # (actual value to be set on the model, the human-readable name)
    CATEGORIES = [
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    ]

    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES, default=CATEGORIES[1][0])
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'acc-product'


class Order(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    ]
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return f'{self.customer.name}, {self.product.name}'

    # def get_absolute_url(self):
    #     return reverse('accounts-customer', kwargs={'pk': self.customer.pk})

    class Meta:
        db_table = 'acc-order'
