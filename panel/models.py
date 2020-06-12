from django.db import models


#Storing all key_link 
class Key_Link_List(models.Model):
    key_link = models.CharField(max_length=500, unique=True, primary_key = True)

    def __str__(self):
        return self.key_link

    def delete(self):
        return Key_Link_List.objects.all().delete()


#Storing url and domanin_rank of an key_link
class Profile(models.Model):
    key_link = models.ForeignKey(Key_Link_List, on_delete=models.CASCADE)
    url = models.CharField(max_length=500, default="")
    domanin_rank = models.IntegerField()


#Storing all other informations of a key_link
class Profile_Extended(models.Model):
    key_link = models.ForeignKey(Key_Link_List, on_delete=models.CASCADE)
    domanin_rank = models.CharField(max_length=500, default="")
    domanin_auth = models.CharField(max_length=500, default="")
    traffic = models.IntegerField(blank=False)
    spam_score = models.IntegerField(blank=False)
    existing_cost = models.IntegerField(blank=False)
    new_cost = models.IntegerField(blank=False)
    email = models.EmailField()
    niche = models.CharField(max_length=500)


#Storing all about matching with two key_link url
class Link_Counter(models.Model):
    key_link = models.ForeignKey(Key_Link_List, on_delete=models.CASCADE)
    compare_key_link = models.CharField(max_length=500)
    no_of_data_matched = models.IntegerField(default=0)
    compare_key_link_no_of_data = models.IntegerField(default=0)


#Storing directory name
class DirectoryName(models.Model):
    directory_name = models.CharField(max_length=500, unique=True, primary_key = True)

    def __str__(self):
        return self.directory_name

    def delete(self):
        return DirectoryName.objects.all().delete()


#Storing directory name with key_link
class DirectoryItem(models.Model):
    directory_name = models.ForeignKey(DirectoryName, on_delete=models.CASCADE)
    key_link = models.CharField(max_length=500, default="")


#Storing nothing now
class Niche(models.Model):
    niche_ID = models.IntegerField(primary_key=True, unique=True)
    tag = models.CharField(max_length=500)


#Storing nothing now
class Column_Set(models.Model):
    column_id = models.IntegerField(primary_key=True, unique=True)
    column_name = models.CharField(max_length=500)