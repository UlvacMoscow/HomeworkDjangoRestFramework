from django.db import models



class Category(models.Model):
    #Ring, Earrings, NEcklase
    type = models.CharField(verbose_name="тип украшения", max_length=150)

    def __str__(self):
        return self.type

class Metal(models.Model):
    type_metal = models.CharField(verbose_name="металл", max_length=200)

    def __str__(self):
        return self.type_metal

class Stone(models.Model):
    type_stone = models.CharField(verbose_name="камень", max_length=200)

class Item(models.Model):
    title = models.CharField(verbose_name="название украшения", max_length=255)
    category = models.ForeignKey(Category, verbose_name="тип украшения", on_delete=models.CASCADE)
    metal = models.ForeignKey(Metal, verbose_name="тип металла", on_delete=models.CASCADE)
    stone = models.ForeignKey(Stone, verbose_name="тип камня", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Decoration():
    pass

class Ring():
    pass

class Earrings():
    pass

class Necklace():
    pass
