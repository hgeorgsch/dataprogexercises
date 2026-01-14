# By Mateusz
# Simulering av Kontantstraum 
# Oppgåve 1

import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025,2035)
loan_start = 1_000_000
interest = 0.10
const_payment = 1000
principal_payment = loan_start/len(years)

annual_loan = []
serial_loan =[]

def loan_payment( type_loan, payment, loan_list_over_time, loan_amount = loan_start, interest = interest,):
    for _ in years :
        interest_payment = loan_amount * interest
        loan_amount += interest_payment

        if type_loan == "A":
            loan_amount -= payment

        elif type_loan == "S":
            loan_amount -= payment + interest_payment
        loan_list_over_time.append(loan_amount)

    return loan_list_over_time

annual_payments = loan_payment("A", const_payment, annual_loan)
serial_payments = loan_payment("S", principal_payment, serial_loan)

plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(years, annual_loan, label = "Annual Loan")
plt.legend()

plt.subplot(2,1,2)
plt.plot(years, serial_loan, label = "Serial Loan")
plt.legend()
plt.show()
