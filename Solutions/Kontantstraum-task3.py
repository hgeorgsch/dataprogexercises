# By Mateusz
# Simulering av Kontantstraum 


# oppgave 3

import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2035)
monthly_saving = 2000
interest_rate = 0.04

balance = 0
balance_over_time = []

for year in years:
    yearly_interest_base = 0

    # Monthly deposits
    for month in range(12):
        balance += monthly_saving
        fraction_of_year = (11 - month) / 12 # 11/12 jan, 10/12 feb, etc...
        yearly_interest_base += monthly_saving * fraction_of_year # each deposit earns interest for the fraction of the year it is in the account.
        #Amount placed in the account at the beginning of the year, will earn the most while the value placed in december will not earn any interest.
        # for jan
        # yearly_interest_base = 0 + 2000 * 11/12
        # for feb
        # yearly_interest_base = 1833 + 2000 * 10/12 ....

    # Credits the interest at the end of the year using the interest base found in the inner loop
    interest = yearly_interest_base * interest_rate
    balance += interest
    balance_over_time.append(balance)

plt.figure(figsize=(10, 6))
plt.plot(years, balance_over_time, label="Savings balance")
plt.xlabel("Year")
plt.ylabel("Balance (kr)")
plt.legend()
plt.show()

