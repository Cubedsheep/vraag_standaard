import numpy as np
import matplotlib.pyplot as plt

# genereer dit voor 100 kansen in het interval [0, 1]
P = np.linspace(0.01,1,100)
P_regen = []

for p in P:
    # de kans op regen
    r = p

    # genereer een array met steeds 3 random waardes tussen 0 en 1
    a = np.random.random((1_000_000,3))
    # indien groter dan 1/3 spreekt de persoon de waarheid: verander naar True, anders false
    antwoorden = (a > 1/3)
    # we willen de kans berekenen dat wanneer ze alle 3 zeggen dat het regent, dat het regent. 
    # genereer een random array met True/False of het regent
    a = np.random.random((1_000_000, 1))
    regen = (a < r)
    # het aantal keer dat ze alle 3 zeggen dat het regent is als (regen = False AND antwoorden = [False, False, False])
    # OR (regen = True AND antwoorden = [True, True, True])
    VAR = np.concatenate((regen, antwoorden), axis=1)
    count_antw = 0
    arr_anw1 = np.array([False, False, False, False])
    arr_anw2 = np.array([True, True, True, True])
    count_regen = 0

    for i in range(1_000_000):
        if np.array_equal(VAR[i], arr_anw1):
            count_antw += 1
        if np.array_equal(VAR[i], arr_anw2):
            count_antw += 1
            count_regen += 1
    P_regen.append(count_regen/count_antw)

# kijk de ruwe data na
P_r = np.array(P_regen)
print(P_r)

# functie om de theoretische kans op regen uit te rekenen
def theoretical_chance(p_regen):
    return 8*p_regen/(1+7*p_regen)

# maak de plot
fig, ax = plt.subplots(1,1, figsize=(12, 8))

P2 = np.linspace(0, 1, 1000)
ax.plot(P2, theoretical_chance(P2), label='theoretische curve')
ax.plot(P, P_r, '.', label='resultaat simulatie (1.000.000 iteraties)')

ax.set_xlabel("kans op regen (onvoorwaardelijk)")
ax.set_ylabel("kans op regen onder voorwaarde dat ze alle 3 zeggen dat het regent")

plt.legend()

plt.show()
