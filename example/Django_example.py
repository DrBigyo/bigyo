from django.db import models

class reporter(model.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline


$ python manage.py makemigrations
$ python manage.py migrate



from news.models import Article, Reporter

Reporter.objects.all()
r = Reporter(full_name='John Smith')
r.save()
r.id

Reporter.objects.all()
r.full_name

