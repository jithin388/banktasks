
from django.db import models
from django.urls import reverse
# Create your models here.
class Gold(models.Model):
    gram=models.IntegerField()
    carat=models.IntegerField()

    def __str__(self):
        return self.name
class loan(models.Model):
    loanChoice=(("M","male"),("F","female"),("O","other"))
    LOAN_CHOICES=(("h","housing"),("p","personal"),("g","gold"))
    name=models.CharField(max_length=30,unique=True)
    email=models.EmailField(max_length=30)
    phone=models.IntegerField()
    gender=models.CharField(max_length=30,choices=loanChoice)
    address=models.CharField(max_length=30)
    aadhar=models.CharField(max_length=30,)
    adhar_img=models.ImageField(upload_to='loan')
    pan=models.CharField(max_length=30,)
    pan_img=models.ImageField(upload_to='loan')
    loan_type=models.CharField(max_length=30,choices=LOAN_CHOICES)
    amount=models.CharField(max_length=30,)
    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    # def get_url(self):
    #     return reverse('bankapp:service_category',args=[self.slug])
    def __str__(self) :
        return '{}'.format(self.name)

#########################################################################################

class State(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class material(models.Model):
    material=models.CharField(max_length=50)
    def __str__(self):
        return self.material

class Person(models.Model):
    #MATERIAL_CHOICES=(("d","debitcard"),("c","creditcard"),("p","prepaidcard"),("q","cheque"))
    #boolChoice=(("male","male"),("female","female"),("other","other"))
    ACCOUNT_CHOICES=(("S","savings"),("C","current"))
    username=models.CharField(max_length=30,unique=True)
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=30)
    phone=models.IntegerField()
    gender=models.CharField(max_length=30)
    address=models.CharField(max_length=30,)
    account=models.CharField(max_length=30,choices=ACCOUNT_CHOICES)
    material=models.CharField(max_length=200)
    
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

