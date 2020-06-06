from django.db import models

class Key_Link_List(models.Model):
    key_link = models.CharField(max_length=500, unique=True, primary_key = True)

    def __str__(self):
        return self.key_link


class Link_Counter(models.Model):
    key_link = models.ForeignKey(Key_Link_List, on_delete=models.CASCADE)
    compare_key_link = models.CharField(max_length=500)
    no_of_data_matched = models.IntegerField(default=0)
    compare_key_link_no_of_data = models.IntegerField(default=0)


class Niche(models.Model):
    niche_ID = models.IntegerField(primary_key=True, unique=True)
    tag = models.CharField(max_length=500)


class Column_Set(models.Model):
    column_id = models.IntegerField(primary_key=True, unique=True)
    column_name = models.CharField(max_length=500)


class Profile(models.Model):
    key_link = models.ForeignKey(Key_Link_List, on_delete=models.CASCADE)
    url = models.URLField()
    domanin_rank = models.IntegerField()


class Profile_Extended(models.Model):
    key_link = models.ForeignKey(Key_Link_List, on_delete=models.CASCADE)
    domanin_auth = models.CharField(max_length=500)
    traffic = models.IntegerField(blank=False)
    spam_score = models.IntegerField(blank=False)
    existing_cost = models.IntegerField(blank=False)
    new_cost = models.IntegerField(blank=False)
    email = models.EmailField()
    niche = models.CharField(max_length=500)

