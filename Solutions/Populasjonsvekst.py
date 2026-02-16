# By Mateusz
# proposed solution to the task "Oppgave 1: Populasjonsvekst":


import matplotlib.pyplot as plt
import numpy as np

def population_logistic(area, r, start_year, end_year, P0, K):
    years = np.arange(start_year, end_year + 1)
    years_list = years - start_year

    A = (K - P0) / P0

    population = []
    for t in years_list:
        P_t = K / (1 + A * np.exp(-r * t))
        population.append(P_t)

    P_end = population[-1]
    absolute_growth = P_end - P0
    relative_growth = (absolute_growth / P0) * 100

    print(f"Area: {area}")
    print(f"Start year: {start_year}")
    print(f"End year: {end_year}")
    print(f"Start population: {P0}")
    print(f"Population in {end_year}: {P_end:.0f}")
    print(f"Absolute growth: {absolute_growth:.0f}")
    print(f"Relative growth: {relative_growth:.2f}%")

    plt.figure(figsize=(10, 6))
    plt.plot(years, population, label="Population")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title(f"Population growth in {area}")
    plt.legend()
    plt.grid()
    plt.show()
proceed = 'y'

while proceed != 'n':
    area = input("Name of the area: ")
    r = float(input("Growth rate r (such as 0.02): "))

    while True:
        start_year = int(input("Start year: "))
        end_year = int(input("End year: "))

        if end_year > start_year:
            break
        else:
            print("End year must be greater than start year. Try again.")

    while True:
        P0 = float(input("Population at the start year: "))
        K = float(input("Maximum population K: "))

        if K > P0:
            break
        else:
            print("Maximum population K must be greater than start population. Try again.")


    population_logistic(area, r, start_year, end_year, P0, K)

    proceed = input("Do you wish to control population change for another area or time period? (y/n): ").lower()
