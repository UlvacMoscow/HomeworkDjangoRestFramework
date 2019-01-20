from django.db import models

class Category(models.Model):
    #Ring, Earrings, NEcklase
    type = models.CharField(verbose_name="тип украшения", max_length=150)

class Metal(models.Model):
    type_metal = models.CharField(verbosa_name="металл", max_length=200)

class Stone(models.Model):
    type_stone = models.CharField(verbose_name="камень", max_length=200)

class Item(models.Model):
    title = models.Charfield(verbose_name="название украшения", max_length=255)
    item_decoration = models.ForeignKey(Category)
    item_metal = models.ForeignKey(Metal)
    item_stone = models.ForeignKey(Stone)



class Decoration():
    pass

class Ring():
    pass

class Earrings():
    pass

class Necklace():
    pass
