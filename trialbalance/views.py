from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from trialbalance.models import TrialBalance
from trialbalance.serializers import TrialBalanceSerializers

from expense.models import Expense
from income.models import Income
import json


class TrialBalanceList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        company = request.META['HTTP_COMPANY']
        trialbalance = TrialBalance.objects.filter(company_id=company)
        serializer = TrialBalanceSerializers(trialbalance, many=True)
        return Response(serializer.data)


class ProfitLoss(APIView):
    def get(self, request, format=None):
        company = request.META['HTTP_COMPANY']
        expense = Expense.objects.filter(company_id=company)
        income = Income.objects.filter(company_id=company)
        incomes = []
        expenses = []
        income_data = {}
        expense_data = {}

        for i in income:
            if i.secondAccount.name in income_data:
                income_data[i.secondAccount.name] += i.amount
            else:
                income_data[i.secondAccount.name] = i.amount
        incomes.append(income_data)

        for i in expense:
            if i.secondAccount.name in expense_data:
                expense_data[i.secondAccount.name] += i.amount
            else:
                expense_data[i.secondAccount.name] = i.amount
        expenses.append(expense_data)
        data = dict()
        data['income'] = incomes
        data['expense'] = expenses
        return JsonResponse(data, safe=False)
