from rest_framework import status ,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework import serializers
from plotly.offline import plot
from plotly.graph_objs import Bar

def dashboard_view(request):
    users = User.objects.all()
    accounts = Account.objects.all()
    transactions = Transaction.objects.all()
    budgets = Budget.objects.all()
    investments = Investment.objects.all()
    debts = Debt.objects.all()
    credit_scores = CreditScore.objects.all()
    financial_goals = FinancialGoal.objects.all()
    bill_reminders = BillReminder.objects.all()
    reports = Report.objects.all()
    images = ImageModel.objects.all()
    videos = VideoModel.objects.all()
    documents = DocumentModel.objects.all()
    audios = AudioModel.objects.all()
    

    context = {
        'users': users,
        'accounts': accounts,
        'transactions': transactions,
        'budgets': budgets,
        'investments': investments,
        'debts': debts,
        'credit_scores': credit_scores,
        'financial_goals': financial_goals,
        'bill_reminders': bill_reminders,
        'reports': reports,
        'images' : images,
        'videos' : videos,
        'documents' : documents,
        'audios' : audios,
        }
    return render(request, 'dashboard.html', context)

def Dashboard(request):
    return render(request, 'dashboard.html')


# User View

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Account View

class AccountView(APIView):
    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        account = Account.objects.get(pk=pk)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        account = Account.objects.get(pk=pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Transaction View

class TransactionView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        transaction = Transaction.objects.get(pk=pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        transaction = Transaction.objects.get(pk=pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Budget View

class BudgetView(APIView):
    def get(self, request):
        budgets = Budget.objects.all()
        serializer = BudgetSerializer(budgets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        budget = Budget.objects.get(pk=pk)
        serializer = BudgetSerializer(budget, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        budget = Budget.objects.get(pk=pk)
        budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Investment View

class InvestmentView(APIView):
    def get(self, request):
        investments = Investment.objects.all()
        serializer = InvestmentSerializer(investments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InvestmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        investment = Investment.objects.get(pk=pk)
        serializer = InvestmentSerializer(investment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        investment = Investment.objects.get(pk=pk)
        investment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Debt View

class DebtView(APIView):
    def get(self, request):
        debts = Debt.objects.all()
        serializer = DebtSerializer(debts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DebtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        debt = Debt.objects.get(pk=pk)
        serializer = DebtSerializer(debt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        debt = Debt.objects.get(pk=pk)
        debt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CreditScore View

class CreditScoreView(APIView):
    def get(self, request):
        credit_scores = CreditScore.objects.all()
        serializer = CreditScoreSerializer(credit_scores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreditScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        credit_score = CreditScore.objects.get(pk=pk)
        serializer = CreditScoreSerializer(credit_score, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        credit_score = CreditScore.objects.get(pk=pk)
        credit_score.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# FinancialGoal View

class FinancialGoalView(APIView):
    def get(self, request):
        financial_goals = FinancialGoal.objects.all()
        serializer = FinancialGoalSerializer(financial_goals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FinancialGoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        financial_goal = FinancialGoal.objects.get(pk=pk)
        serializer = FinancialGoalSerializer(financial_goal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        financial_goal = FinancialGoal.objects.get(pk=pk)
        financial_goal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# BillReminder View

class BillReminderView(APIView):
    def get(self, request):
        bill_reminders = BillReminder.objects.all()
        serializer = BillReminderSerializer(bill_reminders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BillReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        bill_reminder = BillReminder.objects.get(pk=pk)
        serializer = BillReminderSerializer(bill_reminder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bill_reminder = BillReminder.objects.get(pk=pk)
        bill_reminder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Report View

class ReportView(APIView):
    def get(self, request):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        report = Report.objects.get(pk=pk)
        serializer = ReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        report = Report.objects.get(pk=pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

# User List
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# Acoount List
class AccountList(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
# Transaction List
class TransactionList(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# Budget List
class BudgetList(generics.ListAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    
# Investment List
class InvestmentList(generics.ListAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    
# Debt List
class DebtList(generics.ListAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    
# Credit score List
class CreditScoreList(generics.ListAPIView):
    queryset = CreditScore.objects.all()
    serializer_class = CreditScoreSerializer
    
# Financial goal List
class FinancialGoalList(generics.ListAPIView):
    queryset = FinancialGoal.objects.all()
    serializer_class = FinancialGoalSerializer
    
# Bill reminder list
class BillReminderList(generics.ListAPIView):
    queryset = BillReminder.objects.all()
    serializer_class = BillReminderSerializer
    
#Report List
class ReportList(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer





# User Details
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Account Details
class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# Transaction Details
class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# Budget Details
class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

# Investment Details
class InvestmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

# Debt Details
class DebtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer

# Credit score Details
class CreditScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CreditScore.objects.all()
    serializer_class = CreditScoreSerializer

# Finanacial goal Details
class FinancialGoalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FinancialGoal.objects.all()
    serializer_class = FinancialGoalSerializer

#Bill reminder Details
class BillReminderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillReminder.objects.all()
    serializer_class = BillReminderSerializer

#Report Details
class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer




# Importing serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'user', 'account_type', 'balance']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'account', 'date', 'description', 'amount']

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'user', 'budget_type', 'amount']

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = ['id', 'user', 'investment_type', 'amount']

class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ['id', 'user', 'debt_type', 'amount']

class CreditScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditScore
        fields = ['id', 'user', 'credit_score']

class FinancialGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialGoal
        fields = ['id', 'user', 'goal_type', 'amount']

class BillReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillReminder
        fields = ['id', 'user', 'bill_name', 'due_date']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'user', 'report_type', 'data']


# Here are the views for create, update, and delete 

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class AccountCreate(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountUpdate(generics.UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDelete(generics.DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    

class TransactionCreate(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionUpdate(generics.UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDelete(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    

class BudgetCreate(generics.CreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

class BudgetUpdate(generics.UpdateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

class BudgetDelete(generics.DestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    

class InvestmentCreate(generics.CreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class InvestmentUpdate(generics.UpdateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class InvestmentDelete(generics.DestroyAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    

class DebtCreate(generics.CreateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer

class DebtUpdate(generics.UpdateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer

class DebtDelete(generics.DestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    

class CreditScoreCreate(generics.CreateAPIView):
    queryset = CreditScore.objects.all()
    serializer_class = CreditScoreSerializer

class CreditScoreUpdate(generics.UpdateAPIView):
    queryset = CreditScore.objects.all()
    serializer_class = CreditScoreSerializer

class CreditScoreDelete(generics.DestroyAPIView):
    queryset = CreditScore.objects.all()
    serializer_class = CreditScoreSerializer
    

class FinancialGoalCreate(generics.CreateAPIView):
    queryset = FinancialGoal.objects.all()
    serializer_class = FinancialGoalSerializer

class FinancialGoalUpdate(generics.UpdateAPIView):
    queryset = FinancialGoal.objects.all()
    serializer_class = FinancialGoalSerializer

class FinancialGoalDelete(generics.DestroyAPIView):
    queryset = FinancialGoal.objects.all()
    serializer_class = FinancialGoalSerializer
    

class BillReminderCreate(generics.CreateAPIView):
    queryset = BillReminder.objects.all()
    serializer_class = BillReminderSerializer

class BillReminderUpdate(generics.UpdateAPIView):
    queryset = BillReminder.objects.all()
    serializer_class = BillReminderSerializer

class BillReminderDelete(generics.DestroyAPIView):
    queryset = BillReminder.objects.all()
    serializer_class = BillReminderSerializer


class ReportCreate(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportUpdate(generics.UpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportDelete(generics.DestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


# Image view
class ImageView(APIView):
    def get(self, request):
        images = ImageModel.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ImageAPIView(APIView):
    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        image = ImageModel.objects.get(pk=pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    def put(self, request, pk):
        image = ImageModel.objects.get(pk=pk)
        serializer = ImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        image = ImageModel.objects.get(pk=pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Video view
class VideoView(APIView):
    def get(self, request):
        videos = VideoModel.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VideoAPIView(APIView):
    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        video = VideoModel.objects.get(pk=pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)

    def put(self, request, pk):
        video = VideoModel.objects.get(pk=pk)
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        video = VideoModel.objects.get(pk=pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Audio view
class AudioView(APIView):
    def get(self, request):
        audios = AudioModel.objects.all()
        serializer = AudioSerializer(audios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AudioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AudioAPIView(APIView):
    def post(self, request):
        serializer = AudioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        audio = AudioModel.objects.get(pk=pk)
        serializer = AudioSerializer(audio)
        return Response(serializer.data)

    def put(self, request, pk):
        audio = AudioModel.objects.get(pk=pk)
        serializer = AudioSerializer(audio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        audio = AudioModel.objects.get(pk=pk)
        audio.delete()
        return Response(status=status)
    

# Document view
class DocumentView(APIView):
    def get(self, request):
        documents = DocumentModel.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentAPIView(APIView):
    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        document = DocumentModel.objects.get(pk=pk)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    def put(self, request, pk):
        document = DocumentModel.objects.get(pk=pk)
        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        document = DocumentModel.objects.get(pk=pk)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)