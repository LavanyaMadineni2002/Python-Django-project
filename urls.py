"""
URL configuration for pfmrestapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from myapp import views
from django.views.generic import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dashboard_view, name='dashboard'),
    
    # # Users
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('user/', UserView.as_view()),
    path('user/create/', UserCreate.as_view()),
    path('user/update/<int:pk>/', UserUpdate.as_view()),
    path('user/delete/<int:pk>/', UserDelete.as_view()),

    # Accounts
    path('account/', AccountList.as_view()),
    path('account/<int:pk>/', AccountDetail.as_view()),
    path('account/', AccountView.as_view()),
    path('account/create/', AccountCreate.as_view()),
    path('account/update/<int:pk>/', AccountUpdate.as_view()),
    path('account/delete/<int:pk>/', AccountDelete.as_view()),

    # Transactions
    path('transaction/', TransactionList.as_view()),
    path('transaction/<int:pk>/', TransactionDetail.as_view()),
    path('transaction/', TransactionView.as_view()),
    path('transaction/create/', TransactionCreate.as_view()),
    path('transaction/update/<int:pk>/', TransactionUpdate.as_view()),
    path('transaction/delete/<int:pk>/', TransactionDelete.as_view()),

    # Budgets
    path('budget/', BudgetList.as_view()),
    path('budget/<int:pk>/', BudgetDetail.as_view()),
    path('budget/', BudgetView.as_view()),
    path('budget/create/', BudgetCreate.as_view()),
    path('budget/update/<int:pk>/', BudgetUpdate.as_view()),
    path('budget/delete/<int:pk>/', BudgetDelete.as_view()),

    # Investments
    path('investment/', InvestmentList.as_view()),
    path('investment/<int:pk>/', InvestmentDetail.as_view()),
    path('investment/', InvestmentView.as_view()),
    path('investment/create/', InvestmentCreate.as_view()),
    path('investment/update/<int:pk>/', InvestmentUpdate.as_view()),
    path('investment/delete/<int:pk>/', InvestmentDelete.as_view()),

    # Debts
    path('debt/', DebtList.as_view()),
    path('debt/<int:pk>/', DebtDetail.as_view()),
    path('debt/', DebtView.as_view()),
    path('debt/create/', DebtCreate.as_view()),
    path('debt/update/<int:pk>/', DebtUpdate.as_view()),
    path('debt/delete/<int:pk>/', DebtDelete.as_view()),

    # Credit Scores
    path('creditscore/', CreditScoreList.as_view()),
    path('creditscore/<int:pk>/', CreditScoreDetail.as_view()),
    path('creditscore/', CreditScoreView.as_view()),
    path('creditscore/create/', CreditScoreCreate.as_view()),
    path('creditscore/update/<int:pk>/', CreditScoreUpdate.as_view()),
    path('creditscore/delete/<int:pk>/', CreditScoreDelete.as_view()),
    
    # Financial Goals
    path('financialgoal/', FinancialGoalList.as_view()),
    path('financialgoal/<int:pk>/', FinancialGoalDetail.as_view()),
    path('financialgoal/', FinancialGoalView.as_view()),
    path('financialgoal/create/', FinancialGoalCreate.as_view()),
    path('financialgoal/update/<int:pk>/', FinancialGoalUpdate.as_view()),
    path('financialgoal/delete/<int:pk>/', FinancialGoalDelete.as_view()),

    # Bill Reminders
    path('billreminder/', BillReminderList.as_view()),
    path('billreminder/<int:pk>/', BillReminderDetail.as_view()),
    path('billreminder/', BillReminderView.as_view()),
    path('billreminder/create/', BillReminderCreate.as_view()),
    path('billreminder/update/<int:pk>/', BillReminderUpdate.as_view()),
    path('billreminder/delete/<int:pk>/', BillReminderDelete.as_view()),

    # Reports
    path('report/', ReportList.as_view()),
    path('report/<int:pk>/', ReportDetail.as_view()),
    path('report/', ReportView.as_view()),
    path('report/create/', ReportCreate.as_view()),
    path('report/update/<int:pk>/', ReportUpdate.as_view()),
    path('report/delete/<int:pk>/', ReportDelete.as_view()),
    
    # Image 
    path('images/', ImageView.as_view()),
    path('images/', ImageAPIView.as_view()),  
    path('images/<int:pk>/', ImageAPIView.as_view()),  
    path('images/<int:pk>/update/', ImageAPIView.as_view()),  
    path('images/<int:pk>/delete/', ImageAPIView.as_view()),  

    # Audio 
    path('audios/', AudioView.as_view()),
    path('audios/', AudioAPIView.as_view()),  
    path('audios/<int:pk>/', AudioAPIView.as_view()),  
    path('audios/<int:pk>/update/', AudioAPIView.as_view()),  
    path('audios/<int:pk>/delete/', AudioAPIView.as_view()),  

    # Video 
    path('videos/', VideoView.as_view()),
    path('videos/', VideoAPIView.as_view()),  
    path('videos/<int:pk>/', VideoAPIView.as_view()),  
    path('videos/<int:pk>/update/', VideoAPIView.as_view()),  
    path('videos/<int:pk>/delete/', VideoAPIView.as_view()),  

    # Document 
    path('documents/', DocumentView.as_view()), 
    path('documents/', DocumentAPIView.as_view()), 
    path('documents/<int:pk>/', DocumentAPIView.as_view()),  
    path('documents/<int:pk>/update/', DocumentAPIView.as_view()),  
    path('documents/<int:pk>/delete/', DocumentAPIView.as_view()),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
