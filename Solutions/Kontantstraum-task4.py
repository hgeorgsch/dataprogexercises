# By Mateusz
# Simulering av Kontantstraum 

# oppgave 4

import matplotlib.pyplot as plt
import random

years = range(2025, 2055)
loan_start = 1_000_000
interest = 0.04
payment = 70_000

loan = loan_start
loan_over_time = []
interest_over_time = []

terskel_opp = 30
terskel_ned = 30
max_slump = 100

for year in years:
    slump = random.randint(1, max_slump)

    if slump <= terskel_opp:
        interest += 0.005
        terskel_opp += 5
        terskel_ned -= 5
    elif slump >= max_slump - terskel_ned:
        interest -= 0.005
        terskel_opp -= 5
        terskel_ned += 5

    terskel_opp = max(5, min(terskel_opp, 90))
    terskel_ned = max(5, min(terskel_ned, 90))
    loan += loan * interest
    loan -= payment
    loan_over_time.append(loan)
    interest_over_time.append(interest)

plt.figure()
plt.subplot(2,1,1)
plt.plot(years, loan_over_time)
plt.subplot(2,1,2)
plt.plot(years, interest_over_time)
plt.show()
