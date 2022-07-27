from django.db import models

class Kurs(models.Model):
    name = models.CharField(max_length=250)
    price =models.PositiveIntegerField()
    text = models.TextField()

    def __str__(self):
        return self.name

class Ustozlar(models.Model):
    name = models.CharField(max_length=250)
    text=models.TextField()
    img = models.ImageField(upload_to="images/")
    number = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Guruh(models.Model):
    kurs = models.ForeignKey(Kurs,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    ustoz = models.ForeignKey(Ustozlar, null=True, on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
        return self.name

class Oylar(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Talaba(models.Model):
    Qilingan = 1
    Qarzi_bor = 2
    Qilinmagan = 3

    guruh =models.ForeignKey(Guruh,null=True,on_delete=models.CASCADE)
    oy = models.ForeignKey(Oylar,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    text = models.TextField()
    number=models.CharField(max_length=250)
    age = models.IntegerField()
    price =models.SmallIntegerField(choices=(
        (Qilingan,"Tulov bo'ldi"),
        (Qarzi_bor,"Qarzi bor"),
        (Qilinmagan,"Qilinmagan")
    ))

    def __str__(self):
        return self.name
# class Product(models.Model):
#     STATUS_NEW = 0  # Bular saytda ko'rinadi
#     STATUS_PUBLISHED = 1  # bular saytda ko'rinadi
#     STATUS_REJECTED = 2  # saytda ko'rinmaydi
#
#     category = models.ForeignKey(Category, on_delete=models.RESTRICT)
#     user = models.ForeignKey("client.User", on_delete=models.RESTRICT)
#     unit = models.ForeignKey(Unit, on_delete=models.RESTRICT, null=True, default=None, blank=True)
#     currency = models.ForeignKey(Currency, on_delete=models.RESTRICT, null=True, default=None, blank=True)
#     name_uz = models.CharField(max_length=50)
#     name_ru = models.CharField(max_length=50)
#     price = models.BigIntegerField()  # tiyinda, currency_id = 1 ($, er=10500), price=55.88$, 5588
#     photo = models.ImageField(upload_to='images/')
#     anons_uz = models.CharField(max_length=50, blank=True, null=True)
#     anons_ru = models.CharField(max_length=50, null=True, blank=True)
#     status = models.SmallIntegerField(choices=(
#         (STATUS_NEW, "Yangi"),
#         (STATUS_PUBLISHED, "Ko'rinadi"),
#         (STATUS_REJECTED, "Maderator o'tkazmadi")
#     ), default=STATUS_NEW, db_index=True)
#
#     @property
#     def price_uzs(self):
#         return self.currency.exchange_rate * self.price
#
#     class Meta:
#         verbose_name = "Mahsulot"
#         verbose_name_plural = "Mahsulotlar"

