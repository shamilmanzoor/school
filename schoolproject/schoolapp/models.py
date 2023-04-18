from django.db import models

PURPOSE_CHOICES = [
    ('enquiry', 'Enquiry'),
    ('order placed', 'Order Placed'),
    ('returned ', 'Returned'),
]


class Purpose(models.Model):
    # MY_CHOICES = [
    #     ('enquiry', 'ENQUIRY'),
    #     ('place order', 'PLACE ORDER'),
    #     ('return', 'RETURN'),
    # ]
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    dob = models.DateField(auto_now=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    age = models.IntegerField()
    email = models.EmailField()
    number = models.IntegerField()
    address = models.TextField(blank=True)

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stream')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Course')
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    materials_required1 = models.BooleanField('Debit Note', default=False)
    materials_required2 = models.BooleanField('Pen', default=False)
    materials_required3 = models.BooleanField('Exam Paper', default=False)
    materials_required4 = models.BooleanField('Bag', default=False)

    def __str__(self):
        return self.name
