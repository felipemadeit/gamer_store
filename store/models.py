from django.db import migrations, models



class Products (models.Model):
    product_id = models.AutoField(
                     auto_created= True,
                     primary_key= True,
                     serialize=False,
                     verbose_name= 'ID'
                 )
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_price = models.PositiveIntegerField()
    product_img = models.ImageField(upload_to= 'store/static/media/products')
    product_category = models.CharField(max_length=200, default='General')
    product_brand = models.CharField(max_length=200, default='general')
    product_stock = models.PositiveSmallIntegerField(default=100)


    def get_format_price(self):
        return "${:,.0f}".format(self.product_price)