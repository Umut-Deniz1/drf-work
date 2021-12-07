from django.db import models

# Create your models here.

class Organizations(models.Model):
    org_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, max_length=50)

    def __str__(self):
        return self.org_name

class Users(models.Model):
    user_name = models.CharField(max_length=200)
    user_surname = models.CharField(max_length=200)
    user_balance = models.IntegerField()
    user_token = models.CharField(max_length=200, blank=True)
    organizations = models.ManyToManyField(Organizations)

    def __str__(self):
        return self.user_name 


class Transactions(models.Model):
    transaction_type = models.CharField(max_length=200)
    transaction_amount = models.IntegerField()
    transaction_status = models.CharField(default="Waiting..",max_length=200)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="transactions")
    #organization_id = models.ForeignKey(Organizations, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.transaction_type
