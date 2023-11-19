from .product_comparison import ProductComparison

from django.db import models


class Band(models.Model):
    """A model of a rock band."""
    name = models.CharField(max_length=200)
    can_rock = models.BooleanField(default=True)

# class LG...
#
# class Samsung...


"""
POSTGRESQL
DB: versus
 - user
 - Band
 - Computer
 - LG_computer
 - Samsung_computer...
 - ASUS
    * 노트북 1
    * 노트북 2
    * 노트북 3


laptop = ASUS(name="노트북 3", ...)
laptop.save()

ASUS.objects.filter(name__contains='3') -> list of ASUS


df = ....


band_list = []
for ri, row in  df.itterrows():
    band = Band(name=row.band_name, can_rock=row....)
    band_list.append(band)
Band.objects.bulk_create(band_list)


res = Band.objects.filter(name='윤도현')
res = [a, b, c, ....]
print(res[0].name)
>>> "윤도현"


python manage.py migrate

"""