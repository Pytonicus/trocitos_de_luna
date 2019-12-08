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
# Categoria

# Acabado

# Diseño

# Productos

# Carrito

# Compras
