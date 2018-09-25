import numpy
import math

def month_min(balance):
    annualInterestRate = 0.2
    monthlyPaymentRate = 0.04
    mon_interest=annualInterestRate/12
    for i in range(12):
        min_month_pay=monthlyPaymentRate*balance
        unpaid_balance=balance-min_month_pay
        interest=mon_interest*unpaid_balance
        balance=unpaid_balance+interest
    return round(balance,2)

def monthly_pay():
    annualInterestRate=0.2
    balance=3329
    a=annualInterestRate/12
    r=numpy.pmt(a,12,balance)
    return r

def polysum(n,s):
    area=(0.25*n*s*s)/(math.tan(math.pi/n))
    perimeter=n*s
    s=round(area+perimeter**2,4)
    return s
