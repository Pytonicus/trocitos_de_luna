from django.db import models

class Cliente(models.Model):
    CIUDADES = [
        ('ac', 'A Coruña'),
        ('al', 'Álava'),
        ('ab', 'Albacete'),
        ('ali', 'Alicante'),
        ('alm', 'Almería'),
        ('as', 'Asturias'),
        ('av', 'Ávila'),
        ('ba', 'Badajoz'),
        ('bal', 'Baleares'),
        ('bar', 'Barcelona'),
        ('bu', 'Burgos'),
        ('ca', 'Cáceres'),
        ('cad', 'Cádiz'),
        ('can', 'Cantabria'),
        ('cas', 'Castellón'),
        ('cr', 'Ciudad Real'),
        ('co', 'Córdoba'),
        ('cu', 'Cuenca'),
        ('gi', 'Girona'),
        ('gr', 'Granada'),
        ('gu', 'Guadalajara'),
        ('gp', 'Gipuzkoa'),
        ('hu', 'Huelva'),
        ('hues', 'Huesca'),
        ('ja', 'Jaén'),
        ('lr', 'La Rioja'),
        ('lp', 'Las Palmas'),
        ('le', 'León'),
        ('ler', 'Lérida'),
        ('lu', 'Lugo'),
        ('ma', 'Madrid'),
        ('mal', 'Málaga'),
        ('mu', 'Murcia'),
        ('na', 'Navarra'),
        ('ou', 'Ourense'),
        ('pa', 'Palencia'),
        ('po', 'Pontevedra'),
        ('sa', 'Salamanca'),
        ('se', 'Segovia'),
        ('so', 'Soria'),
        ('ta', 'Tarragona'),
        ('te', 'Santa Cruz de Tenerife'),
        ('ter', 'Teruel'),
        ('to', 'Toledo'),
        ('va', 'Valencia'),
        ('val', 'Valladolid'),
        ('vi', 'Vizcaya'),
        ('za', 'Zamora'),
        ('zar', 'Zaragoza')
    ]
    
    username = models.ForeignKey('auth.User', on_delete = models.CASCADE, verbose_name = 'Usuario')
    # Email
    name = models.CharField(max_length = 100, verbose_name = 'Nombre')
    second_name = models.CharField(max_length = 200, verbose_name = 'Apellidos')
    address = models.CharField(max_length = 200, verbose_name = 'Dirección')
    cp = models.IntegerField(verbose_name = 'Código Postal')
    city = models.CharField(max_length = 30, choices = CIUDADES, verbose_name = 'Ciudad')
    phone = models.IntegerField(verbose_name = 'Número de teléfono')

    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de actualización')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Listado de Clientes'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Nombre de la categoría')
    image = models.ImageField(upload_to = 'categorias/', blank = True, verbose_name = 'Imagen de la categoría')

    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de edición')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Listado de Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Tipo de material')
    image = models.ImageField(upload_to = 'material/', blank = True, verbose_name = 'Imagen del material')

    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de edición')

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Listado de Materiales'
        ordering = ['name']

    def __str__(self):
        return self.name

class Design(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Diseño')
    image = models.ImageField(upload_to = 'design/', blank = True, verbose_name = 'Imagen del diseño')

    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de edición')

    class Meta:
        verbose_name = 'Diseño'
        verbose_name_plural = 'Listado de Diseños'
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'Nombre del producto')
    ref = models.IntegerField(verbose_name = 'Referencia')
    image = models.ImageField(upload_to = 'product/', blank = True, verbose_name = 'Imagen del producto')
    description = models.TextField(blank = True, verbose_name = 'Descripción del producto')
    price = models.FloatField(verbose_name = 'Precio')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = 'Categoría')
    material = models.ForeignKey(Material, on_delete = models.CASCADE, verbose_name = 'Tipo de material')
    design = models.ForeignKey(Design, on_delete = models.CASCADE, blank = True, null = True, verbose_name = 'Diseño')

    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de edición')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Listado de Productos'
        ordering = ['title']

    def __str__(self):
        return self.title

class Delivery(models.Model):
    name = models.CharField(max_length = 150, verbose_name = 'Nombre de la empresa')
    logo = models.ImageField(upload_to = 'delivery', blank = True, verbose_name = 'Logo de la empresa')
    price = models.FloatField(verbose_name = 'Precio de envío')
    time = models.IntegerField(verbose_name = 'Plazo de envío')

    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de edición')

    class Meta:
        verbose_name = 'Envio'
        verbose_name_plural = 'Empresas de Envío'
        ordering = ['name']

    def __str__(self):
        return self.name

class Cart(models.Model):
    client = models.ForeignKey(Cliente, on_delete = models.CASCADE, verbose_name = 'Cliente')
    product = models.ForeignKey(Product, on_delete = models.CASCADE, verbose_name = 'Producto')
    lot = models.IntegerField(verbose_name = 'Cantidad')

    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de edición')

    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carrito de la compra'
        ordering = ['client']

    def __str__(self):
        return self.client

class Billing(models.Model):
    client = models.CharField(max_length = 150, verbose_name = 'Cliente')
    products = models.TextField(max_length = 250, verbose_name = 'Artículos')
    send = models.CharField(max_length = 100, verbose_name = 'Método de Envío')
    total = models.FloatField(verbose_name = 'Total')
    date_buy = models.DateTimeField(auto_now_add = True, verbose_name = 'Fecha de pedido')

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
        ordering = ['client']

    def __str__(self):
        return self.client