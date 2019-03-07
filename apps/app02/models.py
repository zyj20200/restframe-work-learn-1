from django.db import models


class ProjectSet(models.Model):
    p_set = models.CharField(max_length=128, verbose_name='项目集')

    class META:
        #db_table = 'project_set'
        verbose_name = "项目集"
        verbose_name_plural = verbose_name


class City(models.Model):
    city = models.CharField(max_length=32, verbose_name='城市')

    class META:
        #db_table = 'city'
        verbose_name = "城市"
        verbose_name_plural = verbose_name


class Department(models.Model):
    department = models.CharField(max_length=32, verbose_name='部室')

    class META:
        #db_table = 'department'
        verbose_name = "部室"
        verbose_name_plural = verbose_name


class Profession(models.Model):
    profession = models.CharField(max_length=32, verbose_name='专业')

    class META:
        #db_table = 'profession'
        verbose_name = "专业"
        verbose_name_plural = verbose_name


class Projects(models.Model):
    '''项目基本信息'''
    name = models.CharField(max_length=128, verbose_name='投资项目名称')
    p_id = models.CharField(max_length=32, unique=True, verbose_name='投资项目编码')
    year = models.IntegerField(verbose_name='年份')
    money = models.BigIntegerField(verbose_name='投资项目金额')
    p_set = models.ForeignKey('ProjectSet')
    city = models.ForeignKey('City')
    department = models.ForeignKey('Department')
    profession = models.ForeignKey('Profession')

    class META:
        #db_table = 'projects'
        verbose_name = "投资项目基本信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
