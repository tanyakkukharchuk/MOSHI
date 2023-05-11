import random
import matplotlib.pyplot as plt
import numpy as np


def exact_value(x, state=1):
    if state == 1:
        return np.exp(x ** 2)
    elif state == 2:
        return x ** 2 - 2 * x + 3
    else:
        raise ValueError('Func Error')


def generate_random_point(a, b, f, state):
    x = random.uniform(a, b)
    y = random.uniform(0, max(f(np.array([a, b]), state=state)))
    return x, y


def monte_carlo_integration(f, a, b, num_samples=1000000, state=1):
    total_area = (b - a) * max(f(np.array([a, b]), state=state))
    num_points_inside = 0
    points_inside = []

    for i in range(num_samples):
        x, y = generate_random_point(a, b, f, state)
        if y <= f(x, state=state):
            num_points_inside += 1
            points_inside.append((x, y))

    integral = total_area * (num_points_inside / num_samples)
    return integral, points_inside, total_area


a = 1
b = 2

exact_integral1 = monte_carlo_integration(exact_value, a, b, num_samples=1000000)[0]
exact_integral2 = monte_carlo_integration(exact_value, a, b, num_samples=1000000, state=2)[0]

x = np.linspace(a, b, 1000)
y = exact_value(x, state=1)

num_samples = 10000
integral, points_inside, total_area = monte_carlo_integration(exact_value, a, b, num_samples=num_samples, state=1)
print(f"Monte Carlo approximation of the main integral: {integral}")

integral_test, points_inside_test, total_area_test = monte_carlo_integration(exact_value, a, b, num_samples=num_samples, state=2)
print(f"Monte Carlo approximation of the test integral: {integral_test}")

print(f"Exact integral value 1: {exact_integral1}")
print(f"Exact integral value 2: {exact_integral2}")


def errors(integral, state=1):
    if state == 1:
        if integral != 0:
            error_abs = abs(exact_integral1 - integral)
            if exact_integral1 == 0:
                error_rel = 0
            else:
                error_rel = error_abs / abs(exact_integral1)
            print(f"Absolute error 1: {error_abs}")
            print(f"Relative error 1: {error_rel}")
        else:
            print("The approximation is zero. The relative error is undefined.")
    else:
        if integral != 0:
            error_abs = abs(exact_integral2 - integral)
            if exact_integral2 == 0:
                error_rel = 0
            else:
                error_rel = error_abs / abs(exact_integral2)
            print(f"Absolute error 2: {error_abs}")
            print(f"Relative error 2: {error_rel}")
        else:
            print("The approximation is zero. The relative error is undefined.")


errors(integral)
errors(integral_test, state=2)

points_outside = [(x, y) for x, y in zip([random.uniform(a, b) for _ in range(num_samples)], [random.uniform(0, total_area) for _ in range(num_samples)]) if y > exact_value(x, state=1)]

plt.plot(x, y, label='Exact function')
plt.fill_between(x, y, color='gray', alpha=0.2, label='Area')
plt.scatter([p[0] for p in points_outside], [p[1] for p in points_outside], s=1, color='green', label='Points outside')
plt.scatter([p[0] for p in points_inside], [p[1] for p in points_inside], s=1, label='Points inside')
plt.legend()
plt.show()

x_test = np.linspace(a, b, 1000)
y_test = exact_value(x_test, state=2)

integral_test, points_inside_test, total_area_test = monte_carlo_integration(exact_value, a, b, num_samples=num_samples, state=2)


points_outside_test = [(x, y) for x, y in zip([random.uniform(a, b) for _ in range(num_samples)], [random.uniform(0, total_area_test) for _ in range(num_samples)]) if y > exact_value(x, state=2)]

plt.plot(x_test, y_test, label='Exact function (test)')
plt.fill_between(x_test, y_test, color='gray', alpha=0.2, label='Area (test)')
plt.scatter([p[0] for p in points_outside_test], [p[1] for p in points_outside_test], s=1, color='green', label='Points outside (test)')
plt.scatter([p[0] for p in points_inside_test], [p[1] for p in points_inside_test],color='red', s=1, label='Points inside (test)')
plt.legend()
plt.show()