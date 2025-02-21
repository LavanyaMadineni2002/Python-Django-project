from rest_framework import viewsets
from django.contrib import admin
from .models import *
from .serializers import *

class UserAdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
admin.site.register(User)

class AccountAdminViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
admin.site.register(Account)

class TransactionAdminViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
admin.site.register(Transaction)

class BudgetAdminViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
admin.site.register(Budget)

class InvestmentAdminViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
admin.site.register(Investment)

class DebtAdminViewSet(viewsets.ModelViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
admin.site.register(Debt)

class CreditScoreAdminViewSet(viewsets.ModelViewSet):
    queryset = CreditScore.objects.all()
    serializer_class = CreditScoreSerializer
admin.site.register(CreditScore)

class FinancialGoalAdminViewSet(viewsets.ModelViewSet):
    queryset = FinancialGoal.objects.all()
    serializer_class = FinancialGoalSerializer
admin.site.register(FinancialGoal)

class BillReminderAdminViewSet(viewsets.ModelViewSet):
    queryset = BillReminder.objects.all()
    serializer_class = BillReminderSerializer
admin.site.register(BillReminder)

class ReportAdminViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
admin.site.register(Report)

class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
admin.site.register(ImageModel)

class VideoViewSet(viewsets.ModelViewSet):
    queryset = VideoModel.objects.all()
    serializer_class = VideoSerializer
admin.site.register(VideoModel)

class AudioViewSet(viewsets.ModelViewSet):
    queryset = AudioModel.objects.all()
    serializer_class = AudioSerializer
admin.site.register(AudioModel)

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = DocumentModel.objects.all()
    serializer_class = DocumentSerializer
admin.site.register(DocumentModel)