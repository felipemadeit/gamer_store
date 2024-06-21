from django.db import migrations, models

# Table categories
class Category (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Table products
class Product (models.Model):
    product_id = models.AutoField(
                     auto_created= True,
                     primary_key= True,
                     serialize=False,
                     verbose_name= 'ID'
                 )
    id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.PositiveIntegerField()
    img = models.ImageField(upload_to= 'store/static/media/products')
    category = models.CharField(max_length=200, default='General')
    brand = models.CharField(max_length=200, default='general')
    stock = models.PositiveSmallIntegerField(default=100)


    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name

# Table of processors

class Processor (models.Model):
    # Relation one to one 
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    description = models.TextField(null= True)
    img = models.ImageField(upload_to='store/static/media/products/processors')
    price = models.PositiveIntegerField()
    stock = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name

# Table of graphics cards
class Graphics_card (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    description = models.TextField(null= True)
    img = models.ImageField(upload_to='store/static/media/products/graphics')
    price = models.PositiveIntegerField()
    stock = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name

# Table of ram
class Ram (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    description = models.TextField(null= True)
    img = models.ImageField(upload_to='store/static/media/products/rams')
    price = models.PositiveIntegerField()
    stock = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name

# Table of motherboards
class MotherBoard (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    description = models.TextField(null= True)
    img = models.ImageField(upload_to='store/static/media/products/motherBoards')
    price = models.PositiveIntegerField()
    stock = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name

# Table of storage (sdd, hdd, ,nvme, m.2)
class Storage (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    description = models.TextField(null= True)
    img = models.ImageField(upload_to='store/static/media/products/storages')
    price = models.PositiveIntegerField()
    stock = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name

# Table of powersupply
class Power_supply (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    description = models.TextField(null= True)
    img = models.ImageField(upload_to='store/static/media/products/powerSuplies')
    price = models.PositiveIntegerField()
    stock = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name

# Table of cases 
class Case (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    description = models.TextField(null= True)
    img = models.ImageField(upload_to='store/static/media/products/cases')
    price = models.PositiveIntegerField()
    stock = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name

# Table of headphones
class HeadPhones (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    description = models.TextField(null= True)
    img = models.ImageField(upload_to='store/static/media/products/headPhones')
    price = models.PositiveIntegerField()
    stock = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name

# Table of keyboards
class Keyboard (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    description = models.TextField(null= True)
    img = models.ImageField(upload_to='store/static/media/products/keyBoards')
    price = models.PositiveIntegerField()
    stock = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.price)

    def __str__(self):
        return self.name     
    
# Table of refrigeration
class Refrigeration (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    description = models.TextField(null= True)
    img = models.ImageField(upload_to='store/static/media/products/refrigerations')
    price = models.PositiveIntegerField()
    stock = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name

# Table of monitors 
class Monitor (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    description = models.TextField(null= True)
    img = models.ImageField(upload_to='store/static/media/products/monitors')
    price = models.PositiveIntegerField()
    stock = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name

# Table of chairs
class Chair (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    description = models.TextField(null= True)
    img = models.ImageField(upload_to='store/static/media/products/chairs')
    price = models.PositiveIntegerField()
    stock = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name

# Table of accessory
class Accessory (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    description = models.TextField(null= True)
    img = models.ImageField(upload_to='store/static/media/products/accessories')
    price = models.PositiveIntegerField()
    stock = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name

class Laptop(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    description = models.TextField(null= True)
    img = models.ImageField(upload_to='store/static/media/products/laptops')
    price = models.PositiveIntegerField()
    stock = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name
    
class Mouse(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    description = models.TextField(null= True)
    img = models.ImageField(upload_to='store/static/media/products/mouses')
    price = models.PositiveIntegerField()
    stock = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name