from django.db import models

#this is a django Model
# Models are used to perform CRUD in the database
# Create your models here.
class Phone(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.manufacturer} {self.model}"

# phones = [
#     ("HTC", "G1", "https://o.aolcdn.com/images/dims?image_uri=https%3A%2F%2Fs3.amazonaws.com%2Fengadget-public-production%2Fproduct%2F1%2F15p%2Fdream-2vr.jpg&thumbnail=640%2C&client=49kdj93ncb8s938hkdo&signature=e02dbe47fd64583e40425f6df79e4ff9223073ec"),
#     ("Motorola", "Razr","https://motorolacaen.vtexassets.com/arquivos/ids/155395/155395.png?v=637203243806100000"),
#     ("OnePlus", "Nord N10 5G", "https://oasis.opstatics.com/content/dam/oasis/page/billie/N10-Frame.png"),
#     ("Dixie", "Two Cups and a String", "https://media.istockphoto.com/photos/string-telephone-cups-picture-id1190214378?k=20&m=1190214378&s=612x612&w=0&h=i9IAOxXy6jRwK6H2ZQYhoekLKRl6nzgTz3vEgMnnN9g=")
# ]
# for phone in phones:
#     Phone(manufacturer=phone[0], model=phone[1], img=phone[2]).save()

