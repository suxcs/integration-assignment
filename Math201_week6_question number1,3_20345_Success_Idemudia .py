import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# 1. Definite integrals
# a. ∫₄⁹ 3√x dx
a = 3 * quad(lambda x: np.sqrt(x), 4, 9)[0]

# b. ∫₁ᵉ ln(x) dx
b = quad(lambda x: np.log(x), 1, np.e)[0]

# c. ∫₀¹ cos⁻¹(x) dx
c = quad(lambda x: np.arccos(x), 0, 1)[0]

# d. ∫₋₁¹ πcos(πx/2) dx
d = np.pi * quad(lambda x: np.cos(np.pi * x / 2), -1, 1)[0]

print("Question 1 - Definite Integrals:")
print(f"a: {a:.4f}")
print(f"b: {b:.4f}")
print(f"c: {c:.4f}")
print(f"d: {d:.4f}")

# 3. Elevation problem
def f(x):
    return x**3 - 5*x**2 + 30

# Find the definite integral for the elevation function
f_integral, _ = quad(f, 0, 4)

# Average value of the function
average_value = f_integral / (4 - 0)

print("\nQuestion 3 - Elevation Problem:")
print(f"Definite integral from 0 to 4: {f_integral:.4f}")
print(f"Average value over [0, 4]: {average_value:.4f}")

# Plotting the graph of the elevation function
x_values = np.linspace(0, 4, 100)
y_values = f(x_values)

plt.figure(figsize=(8,5))
plt.plot(x_values, y_values, label='Elevation function f(x)', color='blue')
plt.axhline(y=average_value, color='red', linestyle='--', label=f'Average value ≈ {average_value:.2f}')
plt.title('Graph of Elevation Function f(x)')
plt.xlabel('x (distance)')
plt.ylabel('f(x) (elevation)')
plt.legend()
plt.grid(True)
plt.show()
