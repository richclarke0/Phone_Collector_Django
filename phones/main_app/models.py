from django.db import models

# Create your models here.
class Phone(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    def __str__(self):
        return f"{manufacturer} {model}"

# phones = [
#     # Phone("HTC", "G1", "https://o.aolcdn.com/images/dims?image_uri=https%3A%2F%2Fs3.amazonaws.com%2Fengadget-public-production%2Fproduct%2F1%2F15p%2Fdream-2vr.jpg&thumbnail=640%2C&client=49kdj93ncb8s938hkdo&signature=e02dbe47fd64583e40425f6df79e4ff9223073ec"),
#     # Phone("Motorola", "Razr","https://motorolacaen.vtexassets.com/arquivos/ids/155395/155395.png?v=637203243806100000"),
#     # Phone("OnePlus", "Nord N10 5G", "data:image/jpeg;base64,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"),
#     # Phone("Dixie", "Two Cups and a String", "https://media.istockphoto.com/photos/string-telephone-cups-picture-id1190214378?k=20&m=1190214378&s=612x612&w=0&h=i9IAOxXy6jRwK6H2ZQYhoekLKRl6nzgTz3vEgMnnN9g=")
#     ("HTC", "G1", "https://o.aolcdn.com/images/dims?image_uri=https%3A%2F%2Fs3.amazonaws.com%2Fengadget-public-production%2Fproduct%2F1%2F15p%2Fdream-2vr.jpg&thumbnail=640%2C&client=49kdj93ncb8s938hkdo&signature=e02dbe47fd64583e40425f6df79e4ff9223073ec"),
#     ("Motorola", "Razr","https://motorolacaen.vtexassets.com/arquivos/ids/155395/155395.png?v=637203243806100000"),
#     ("OnePlus", "Nord N10 5G", "data:image/jpeg;base64,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"),
#     ("Dixie", "Two Cups and a String", "https://media.istockphoto.com/photos/string-telephone-cups-picture-id1190214378?k=20&m=1190214378&s=612x612&w=0&h=i9IAOxXy6jRwK6H2ZQYhoekLKRl6nzgTz3vEgMnnN9g=")
# ]
# for phone in phones:
#     Phone(manufacturer=phone[0], model=phone[1], img=phone[2]).save()

