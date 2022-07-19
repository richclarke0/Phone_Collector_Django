from django.db import models
from django.urls import reverse

ACCESSORIES = (
    ('charger', 'Phone charger with cable'),
    ('phones', 'Headphones'),
    ('case', 'A hard plastic phone case'),
    ('screenprotector', 'A stick-on screen protector to prevent scratches')
)



#this is a django Model
# Models are used to perform CRUD in the database
# Create your models here.
class Phone(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    bands = models.ManyToManyField(Band)
    def __str__(self):
        return f"{self.manufacturer} {self.model}"
    def has_a_charger(self):
        return self.accessory_set.filter(item="charger").count() >= 1
    def has_a_case(self):
        return self.accessory_set.filter(item="case").count() >= 1

class Accessory(models.Model):
    date = models.DateField("Date purchased") #this is the actual label on the form
    item = models.CharField(
        max_length = 25,
        choices=ACCESSORIES,
        default=ACCESSORIES[0][0]
    )

    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_item_display()} on {self.date}"
    
    class Meta: ordering = ['-date']

    def get_absolute_url(self):
        return reverse("detail", kwargs={"phone_id": self.id})
    
class Band(models.Model):
    type = models.CharField(max_length = 20)
    def __str__(self):
        return self.type
    def get_absolute_url(self):
        return reverse("bands_detail", kwargs={"pk": self.id})
    
















# phones = [
#     ("HTC", "G1", "https://o.aolcdn.com/images/dims?image_uri=https%3A%2F%2Fs3.amazonaws.com%2Fengadget-public-production%2Fproduct%2F1%2F15p%2Fdream-2vr.jpg&thumbnail=640%2C&client=49kdj93ncb8s938hkdo&signature=e02dbe47fd64583e40425f6df79e4ff9223073ec"),
#     ("Motorola", "Razr","https://motorolacaen.vtexassets.com/arquivos/ids/155395/155395.png?v=637203243806100000"),
#     ("OnePlus", "Nord N10 5G", "https://oasis.opstatics.com/content/dam/oasis/page/billie/N10-Frame.png"),
#     ("Dixie", "Two Cups and a String", "https://media.istockphoto.com/photos/string-telephone-cups-picture-id1190214378?k=20&m=1190214378&s=612x612&w=0&h=i9IAOxXy6jRwK6H2ZQYhoekLKRl6nzgTz3vEgMnnN9g=")
# ]
# for phone in phones:
#     Phone(manufacturer=phone[0], model=phone[1], img=phone[2]).save()

