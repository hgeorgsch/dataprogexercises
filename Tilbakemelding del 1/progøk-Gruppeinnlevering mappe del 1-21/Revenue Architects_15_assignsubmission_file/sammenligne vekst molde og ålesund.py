import matplotlib.pyplot as plt

def simuler_befolkningsvekst(startbefolkning_molde, vekstrate_molde, startbefolkning_alesund, vekstrate_alesund, antall_år):
    befolkning_molde = [startbefolkning_molde]
    befolkning_alesund = [startbefolkning_alesund]

    for i in range(antall_år):
        ny_befolkning_molde = befolkning_molde[-1] * (1 + vekstrate_molde)
        ny_befolkning_alesund = befolkning_alesund[-1] * (1 + vekstrate_alesund)
        befolkning_molde.append(ny_befolkning_molde)
        befolkning_alesund.append(ny_befolkning_alesund)

    return befolkning_molde, befolkning_alesund

def lag_plot(befolkning_molde, befolkning_alesund, antall_år):
    år = list(range(antall_år + 1))
    plt.plot(år, befolkning_molde, label='Molde')
    plt.plot(år, befolkning_alesund, label='Ålesund')
    plt.xlabel('År')
    plt.ylabel('Befolkning')
    plt.title('Befolkningsvekst i Molde og Ålesund over tid')
    plt.legend()
    plt.grid(True)
    plt.show()

def skriv_ut_informasjon(befolkning_molde, befolkning_alesund):
    total_vekst_molde = befolkning_molde[-1] - befolkning_molde[0]
    total_vekst_alesund = befolkning_alesund[-1] - befolkning_alesund[0]
    relativ_vekst_molde = (total_vekst_molde / befolkning_molde[0]) * 100
    relativ_vekst_alesund = (total_vekst_alesund / befolkning_alesund[0]) * 100

    print("Molde total vekst: " + str(round(total_vekst_molde, 2)) + " (" + str(round(relativ_vekst_molde, 2)) + "%)")
    print("Ålesund total vekst: " + str(round(total_vekst_alesund, 2)) + " (" + str(round(relativ_vekst_alesund, 2)) + "%)")

    if total_vekst_molde > total_vekst_alesund:
        print("Molde har vokst mest.")
    else:
        print("Ålesund har vokst mest.")

    if befolkning_molde[-1] > befolkning_alesund[-1]:
        print("Molde er størst.")
    else:
        print("Ålesund er størst.")

startbefolkning_molde = 26048
vekstrate_molde = 0.01
startbefolkning_alesund = 45747
vekstrate_alesund = 0.015
antall_år = 10

befolkning_molde, befolkning_alesund = simuler_befolkningsvekst(startbefolkning_molde, vekstrate_molde, startbefolkning_alesund, vekstrate_alesund, antall_år)
lag_plot(befolkning_molde, befolkning_alesund, antall_år)
skriv_ut_informasjon(befolkning_molde, befolkning_alesund)
