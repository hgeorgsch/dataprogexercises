# By Mateusz
# Simulering av Kontantstraum 

# Oppgave 2

import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2035)
months = len(years) * 12

loan_start = 1_000_000
annual_interest = 0.10
monthly_interest = annual_interest / 12

monthly_payment = 3000

loan_balance = []
loan_amount = loan_start

for month in range(months):
    interest_payment = loan_amount * monthly_interest
    loan_amount += interest_payment
    loan_amount -= monthly_payment
    loan_balance.append(loan_amount)

time_months = np.linspace(years[0], years[-1], months)
plt.figure(figsize=(10, 5))
plt.plot(time_months, loan_balance, label="Monthly payments")
plt.xlabel("Year")
plt.ylabel("Remaining balance")
plt.legend()
plt.show()
