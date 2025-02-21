from django.db import models

# User Model
class User(models.Model):
    name = models.CharField(max_length=255, default="")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

# Account Model
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

# Transaction Model
class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

# Budget Model
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    budget_type = models.CharField(max_length=255, default="Income")

# Investment Model
class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    investment_type = models.CharField(max_length=255, default="Stocks")

# Debt Model
class Debt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    debt_type = models.CharField(max_length=255, default="Credit Card")

# Credit Score Model
class CreditScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    credit_score = models.IntegerField()

# Financial Goal Model
class FinancialGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    goal_type = models.CharField(max_length=255, default="Saving")

# Bill Reminder Model
class BillReminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bill_name = models.CharField(max_length=100)
    due_date = models.DateField()

# Report Model
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    data = models.TextField()
    report_type = models.CharField(max_length=255, default="Monthly")

# Image Model
class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

# Video Model
class VideoModel(models.Model):
    video = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

# Audio Model
class AudioModel(models.Model):
    audio = models.FileField(upload_to='audios/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

# Document Model
class DocumentModel(models.Model):
    document = models.FileField(upload_to='documents/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    