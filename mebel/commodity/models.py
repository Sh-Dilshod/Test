from django.db import models

class Contact(models.Model):
    numbers = models.CharField(max_length=20)
    gmail = models.EmailField()
    discriptions = models.TextField()

    def __str__(self):
        return self.numbers


class Product(models.Model):
    title = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='product', null=True, blank=True, default='media/product/2022-01-05_01-58-38.png')
    prise = models.CharField(max_length=20)
    desciption = models.CharField(max_length=10000)

    def __str__(self):
        return self.title


class Crocekry(models.Model):
    title = models.CharField(max_length=500)
    photo = models.ImageField()
    prise = models.CharField(max_length=20)
    desciption = models.CharField(max_length=10000)

    def __str__(self):
        return self.title




# from vendor.models import VendorModel
#
#
# class CategoryModel(models.Model):
#     title = models.CharField(max_length=200)
#     slug = models.CharField(max_length=200, unique=True)
#     preview = models.ImageField(upload_to='categories/previews', null=True, blank=True)
#     banner1 = models.ImageField(upload_to='categories', null=True, blank=True)
#     banner2 = models.ImageField(upload_to='categories', null=True, blank=True)
#
#
# class SubCategoryModel(models.Model):
#     title = models.CharField(max_length=200)
#     slug = models.CharField(max_length=200, unique=True)
#     category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='subcategories')
#
#
# class ManufacturerModel(models.Model):
#     title = models.CharField(max_length=200)
#     subcategory = models.ForeignKey(SubCategoryModel, on_delete=models.PROTECT, related_name='manufacturers')
#     category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='manufacturers')
#
#     slug = models.CharField(max_length=200, unique=True)
#     preview = models.ImageField(upload_to='manufacturer/avatar/%Y/%m/%d', null=True, blank=True)
#     banner1 = models.ImageField(upload_to='manufacturer/landing/%Y/%m/%d', null=True, blank=True)
#     banner2 = models.ImageField(upload_to='manufacturer/landing/%Y/%m/%d', null=True, blank=True)
#
#
# class ProductTypeModel(models.Model):
#     title = models.CharField(max_length=200)
#     slug = models.CharField(max_length=200, unique=True)
#     subcategory = models.ForeignKey(SubCategoryModel, on_delete=models.PROTECT, related_name='product_types')
#
#
# class ProductModel(models.Model):
#     product_type = models.ForeignKey(ProductTypeModel, on_delete=models.PROTECT, related_name='product', null=True, blank=True)
#     category = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE, related_name='products')
#     manufacturer = models.ForeignKey(ManufacturerModel, on_delete=models.PROTECT, related_name='products', null=True, blank=True)
#     vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     slug = models.CharField(max_length=200, unique=True)
