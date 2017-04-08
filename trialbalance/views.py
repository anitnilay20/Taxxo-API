from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from expense.models import Expense
from income.models import Income
from ledgers.models import Ledgers
from trialbalance.models import TrialBalance
from trialbalance.serializers import TrialBalanceSerializers


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
        print income_data
        for key, item in income_data.iteritems():
            final_income = {}
            final_income['particular'] = key
            final_income['amount'] = item
            incomes.append(final_income)

        for i in expense:
            if i.secondAccount.name in expense_data:
                expense_data[i.secondAccount.name] += i.amount
            else:
                expense_data[i.secondAccount.name] = i.amount

        for key, item in expense_data.iteritems():
            final_expense = {}
            final_expense['particular'] = key
            final_expense['amount'] = item
            expenses.append(final_expense)
        data = dict()
        data['income'] = incomes
        data['expense'] = expenses
        return JsonResponse(data, safe=False)


class Balancesheet(APIView):
    def get(self, request, format=None):
        current_assets = Ledgers.objects.filter(
            groups=['bank OCC AC', 'cash in hand', 'deposits assets', 'loans n advances assets', 'stock in hand',
                    'sundry debitors'])
        loans_liability = Ledgers.objects.filter(groups=['bank OD AC', 'secured loans', 'unsecured loans'])
        curent_liabilities = Ledgers.objects.filter(groups=['duties n taxes', 'provisions', 'sundry creditors'])
        capital_account = Ledgers.objects.filter(groups=['reserve n surpulus'])
        data = dict()
        data['current_assets'] = current_assets
        data['loans_liability'] = loans_liability
        data['curent_liabilities'] = curent_liabilities
        data['capital_account'] = capital_account
        return JsonResponse(data, safe=False)
