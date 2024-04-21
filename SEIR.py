import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Function that returns dy/dt
def model(y, t, beta, gamma, delta):
    S, E, I, R = y
    dSdt = -beta * S * I
    dEdt = beta * S * I - delta * E
    dIdt = delta * E - gamma * I
    dRdt = gamma * I
    return [dSdt, dEdt, dIdt, dRdt]

# Initial conditions
S0 = 0.80  # Initial susceptible population
E0 = 0.10  # Initial exposed population
I0 = 0.10  # Initial infected population
R0 = 0.00  # Initial recovered population
y0 = [S0, E0, I0, R0]

# Parameters
beta = 1.3   # Infection rate
gamma = 0.6  # Recovery rate
delta = 2.5  # Incubation rate

# Time grid (in days)
t = np.linspace(0, 160, 160)

# Solve the differential equations using odeint
solution = odeint(model, y0, t, args=(beta, gamma, delta))

# Extracting the results
S, E, I, R = solution.T

plt.plot(t, S, label='Susceptible')
plt.plot(t, E, label='Exposed')
plt.plot(t, I, label='Infected')
plt.plot(t, R, label='Recovered')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('SEIR Model')
plt.legend()
plt.show()
