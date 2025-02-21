from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'user', 'account_name', 'account_type', 'balance']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'account', 'date', 'description', 'amount']

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'user', 'name', 'amount', 'budget_type']

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = ['id', 'user', 'name', 'amount', 'investment_type']

class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ['id', 'user', 'name', 'amount', 'debt_type']

class CreditScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditScore
        fields = ['id', 'user', 'credit_score']

class FinancialGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialGoal
        fields = ['id', 'user', 'name', 'amount', 'goal_type']

class BillReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillReminder
        fields = ['id', 'user', 'bill_name', 'due_date']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'user', 'name', 'data']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ['id', 'image', 'uploaded_at']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoModel
        fields = ['id','video', 'title', 'description', 'uploaded_at']

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioModel
        fields = ['id','audio', 'title', 'description', 'uploaded_at']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        fields = ['id', 'document', 'title', 'description', 'uploaded_at']