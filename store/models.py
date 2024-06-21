from django.db import migrations, models

# Table categories
class Category (models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

# Table products
class Product (models.Model):
    product_id = models.AutoField(
                     auto_created= True,
                     primary_key= True,
                     serialize=False,
                     verbose_name= 'ID'
                 )
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=300)
    product_description = models.TextField()
    product_price = models.PositiveIntegerField()
    product_img = models.ImageField(upload_to= 'store/static/media/products')
    product_category = models.CharField(max_length=200, default='General')
    product_brand = models.CharField(max_length=200, default='general')
    product_stock = models.PositiveSmallIntegerField(default=100)


    def get_format_price(self):
        return "${:,.0f}".format(self.product_price)
    
    def __str__(self):
        return self.product_name

# Table of processors

class Processor (models.Model):
    # Relation one to one 
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    processor_name = models.CharField(max_length=100)
    processor_brand = models.CharField(max_length=200)
    processor_description = models.TextField(null= True)
    processor_img = models.ImageField(upload_to='store/static/media/products/processors')
    processor_price = models.PositiveIntegerField()
    processor_stock = models.IntegerField(default = 0)
    processor_date_created = models.DateTimeField(auto_now_add=True)
    processor_date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.processor_price)
    
    def __str__(self):
        return self.processor_name

# Table of graphics cards
class Graphics_card (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=100)
    card_brand = models.CharField(max_length=200)
    card_description = models.TextField(null= True)
    card_img = models.ImageField(upload_to='store/static/media/products/graphics')
    card_price = models.PositiveIntegerField()
    card_stock = models.IntegerField(default = 0)
    card_date_created = models.DateTimeField(auto_now_add=True)
    card_date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.card_price)
    
    def __str__(self):
        return self.card_name

# Table of ram
class Ram (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    ram_name = models.CharField(max_length=100)
    ram_brand = models.CharField(max_length=200)
    ram_description = models.TextField(null= True)
    ram_img = models.ImageField(upload_to='store/static/media/products/rams')
    ram_price = models.PositiveIntegerField()
    ram_stock = models.IntegerField(default = 0)
    ram_date_created = models.DateTimeField(auto_now_add=True)
    ram_date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.ram_price)
    
    def __str__(self):
        return self.ram_name

# Table of motherboards
class MotherBoard (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    motherBoard_name = models.CharField(max_length=100)
    motherBoard_brand = models.CharField(max_length=200)
    motherBoard_description = models.TextField(null= True)
    motherBoard_img = models.ImageField(upload_to='store/static/media/products/motherBoards')
    motherBoard_price = models.PositiveIntegerField()
    motherBoard_stock = models.IntegerField(default = 0)
    motherBoard_date_created = models.DateTimeField(auto_now_add=True)
    motherBoard_date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.MotherBoard_price)
    
    def __str__(self):
        return self.motherBoard_name

# Table of storage (sdd, hdd, ,nvme, m.2)
class Storage (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    storage_name = models.CharField(max_length=100)
    storage_brand = models.CharField(max_length=200)
    storage_description = models.TextField(null= True)
    storage_img = models.ImageField(upload_to='store/static/media/products/storages')
    storage_price = models.PositiveIntegerField()
    storage_stock = models.IntegerField(default = 0)
    storage_date_created = models.DateTimeField(auto_now_add=True)
    storage_date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.storage_price)
    
    def __str__(self):
        return self.storage_name

# Table of powersupply
class Power_supply (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    power_name = models.CharField(max_length=100)
    power_brand = models.CharField(max_length=200)
    power_description = models.TextField(null= True)
    power_img = models.ImageField(upload_to='store/static/media/products/powerSuplies')
    power_price = models.PositiveIntegerField()
    power_stock = models.IntegerField(default = 0)
    power_date_created = models.DateTimeField(auto_now_add=True)
    power_date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.power_price)
    
    def __str__(self):
        return self.power_name

# Table of cases 
class Case (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    case_name = models.CharField(max_length=100)
    case_brand = models.CharField(max_length=200)
    case_description = models.TextField(null= True)
    case_img = models.ImageField(upload_to='store/static/media/products/cases')
    case_price = models.PositiveIntegerField()
    case_stock = models.IntegerField(default = 0)
    case_date_created = models.DateTimeField(auto_now_add=True)
    case_date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.Case_price)
    
    def __str__(self):
        return self.case_name

# Table of headphones
class HeadPhones (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    headPhones_name = models.CharField(max_length=100)
    headPhones_brand = models.CharField(max_length=200)
    headPhones_description = models.TextField(null= True)
    headPhones_img = models.ImageField(upload_to='store/static/media/products/headPhones')
    headPhones_price = models.PositiveIntegerField()
    headPhones_stock = models.IntegerField(default = 0)
    headPhones_date_created = models.DateTimeField(auto_now_add=True)
    headPhones_date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.HeadPhones_price)
    
    def __str__(self):
        return self.headPhones_name

# Table of keyboards
class Keyboard (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    keyboard_name = models.CharField(max_length=100)
    keyboard_brand = models.CharField(max_length=200)
    keyboard_description = models.TextField(null= True)
    keyboard_img = models.ImageField(upload_to='store/static/media/products/keyBoards')
    keyboard_price = models.PositiveIntegerField()
    keyboard_stock = models.IntegerField(default = 0)
    keyboard_date_created = models.DateTimeField(auto_now_add=True)
    keyboard_date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.keyboard_price)

    def __str__(self):
        return self.keyboard_name     
    
# Table of refrigeration
class Refrigeration (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    refrigeration_name = models.CharField(max_length=100)
    refrigeration_brand = models.CharField(max_length=200)
    refrigeration_description = models.TextField(null= True)
    refrigeration_img = models.ImageField(upload_to='store/static/media/products/refrigerations')
    refrigeration_price = models.PositiveIntegerField()
    refrigeration_stock = models.IntegerField(default = 0)
    refrigeration_date_created = models.DateTimeField(auto_now_add=True)
    refrigeration_date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.refrigeration_price)
    
    def __str__(self):
        return self.refrigeration_name

# Table of monitors 
class Monitor (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    monitor_name = models.CharField(max_length=100)
    monitor_brand = models.CharField(max_length=200)
    monitor_description = models.TextField(null= True)
    monitor_img = models.ImageField(upload_to='store/static/media/products/monitors')
    monitor_price = models.PositiveIntegerField()
    monitor_stock = models.IntegerField(default = 0)
    monitor_date_created = models.DateTimeField(auto_now_add=True)
    monitor_date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.monitor_price)
    
    def __str__(self):
        return self.monitor_name

# Table of chairs
class Chair (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    chair_name = models.CharField(max_length=100)
    chair_brand = models.CharField(max_length=200)
    chair_description = models.TextField(null= True)
    chair_img = models.ImageField(upload_to='store/static/media/products/chairs')
    chair_price = models.PositiveIntegerField()
    chair_stock = models.IntegerField(default = 0)
    chair_date_created = models.DateTimeField(auto_now_add=True)
    chair_date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.chair_price)
    
    def __str__(self):
        return self.chair_name

# Table of accessory
class Accessory (models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    accessory_name = models.CharField(max_length=100)
    accessory_brand = models.CharField(max_length=200)
    accessory_description = models.TextField(null= True)
    accessory_img = models.ImageField(upload_to='store/static/media/products/accessories')
    accessory_price = models.PositiveIntegerField()
    accessory_stock = models.IntegerField(default = 0)
    accessory_date_created = models.DateTimeField(auto_now_add=True)
    accessory_date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.accessory_price)
    
    def __str__(self):
        return self.accessory_name

class Laptop(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    laptop_name = models.CharField(max_length=100)
    laptop_brand = models.CharField(max_length=200)
    laptop_description = models.TextField(null= True)
    laptop_img = models.ImageField(upload_to='store/static/media/products/laptops')
    laptop_price = models.PositiveIntegerField()
    laptop_stock = models.IntegerField(default = 0)
    laptop_date_created = models.DateTimeField(auto_now_add=True)
    laptop_date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.laptop_price)
    
    def __str__(self):
        return self.laptop_name
    
class Mouse(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    mouse_name = models.CharField(max_length=100)
    mouse_brand = models.CharField(max_length=200)
    mouse_description = models.TextField(null= True)
    mouse_img = models.ImageField(upload_to='store/static/media/products/mouses')
    mouse_price = models.PositiveIntegerField()
    mouse_stock = models.IntegerField(default = 0)
    mouse_date_created = models.DateTimeField(auto_now_add=True)
    mouse_date_modified = models.DateTimeField(auto_now=True)

    def get_format_price(self):
        return "${:,.0f}".format(self.mouse_price)
    
    def __str__(self):
        return self.mouse_name