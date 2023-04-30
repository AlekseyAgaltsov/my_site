from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    url = models.CharField(max_length=40, default='/')


class Gost(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=225, default='-')
    url = models.CharField(max_length=225, default='gost')
    size = models.IntegerField(max_length=100, default='0')
    file_type = models.CharField(max_length=100, default='pdf')

    def __str__(self):
        return f'{self.name} {self.description}'


class Iso(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=225, default='-')
    size = models.IntegerField(max_length=100, default='0')
    file_type = models.CharField(max_length=100, default='pdf')

    def __str__(self):
        return f'{self.name}'


class Ansi(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=225, default='-')
    size = models.IntegerField(max_length=100, default='0')
    file_type = models.CharField(max_length=100, default='pdf')

    def __str__(self):
        return f'{self.name}'


class Api(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=225, default='-')
    size = models.IntegerField(max_length=100, default='0')
    file_type = models.CharField(max_length=100, default='pdf')

    def __str__(self):
        return f'{self.name}'


class Asme(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=225, default='-')
    size = models.IntegerField(max_length=100, default='0')
    file_type = models.CharField(max_length=100, default='pdf')

    def __str__(self):
        return f'{self.name}'


class Astm(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=225, default='-')
    size = models.IntegerField(max_length=100, default='0')
    file_type = models.CharField(max_length=100, default='pdf')

    def __str__(self):
        return f'{self.name}'


class Bs(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=225, default='-')
    size = models.IntegerField(max_length=100, default='0')
    file_type = models.CharField(max_length=100, default='pdf')

    def __str__(self):
        return f'{self.name}'


class Din(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=225, default='-')
    size = models.IntegerField(max_length=100, default='0')
    file_type = models.CharField(max_length=100, default='pdf')

    def __str__(self):
        return f'{self.name}'


class Dd(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=225, default='-')
    size = models.IntegerField(max_length=100, default='0')
    file_type = models.CharField(max_length=100, default='pdf')

    def __str__(self):
        return f'{self.name}'


class Dvs(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=225, default='-')
    size = models.IntegerField(max_length=100, default='0')
    file_type = models.CharField(max_length=100, default='pdf')

    def __str__(self):
        return f'{self.name}'


class En(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=225, default='-')
    size = models.IntegerField(max_length=100, default='0')
    file_type = models.CharField(max_length=100, default='pdf')

    def __str__(self):
        return f'{self.name}'


class Iec(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=225, default='-')
    size = models.IntegerField(max_length=100, default='0')
    file_type = models.CharField(max_length=100, default='pdf')

    def __str__(self):
        return f'{self.name}'


class Vdi(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=225, default='-')
    size = models.IntegerField(max_length=100, default='0')
    file_type = models.CharField(max_length=100, default='pdf')

    def __str__(self):
        return f'{self.name}'


class Pd(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=225, default='-')
    size = models.IntegerField(max_length=100, default='0')
    file_type = models.CharField(max_length=100, default='pdf')

    def __str__(self):
        return f'{self.name}'
