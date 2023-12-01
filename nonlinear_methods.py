def regula_falsi_method(fnc, x0, x1, tolerance=0.0005, iterations=10):
    current_iteration = 1
    while True:
        x2 = x1 - ((fnc(x1) * (x1 - x0)) / (fnc(x1) - fnc(x0)))
        if fnc(x2) is 0:
            print("Root found.")
            return x2
        elif fnc(x0) * fnc(x2) > 0:
            x0 = x2
        elif fnc(x1) * fnc(x2) > 0:
            x1 = x2
        error = abs(x1 - x0)
        current_iteration += 1
        if error < tolerance:
            print("Converges.")
            return x2
        if current_iteration > iterations:
            print("The maximum number of iterations has been reached.")
            return x2


def bisection_method(fnc, x_left, x_right, tolerance=0.0005, iterations=10):
    current_iteration = 1
    while True:
        x_middle = (x_left + x_right) / 2
        if fnc(x_middle) == 0:
            print("Root found.")
            return x_middle
        elif fnc(x_middle) * fnc(x_left) > 0:
            x_left = x_middle
        elif fnc(x_middle) * fnc(x_right) > 0:
            x_right = x_middle
        error = (x_right - x_left) / 2
        current_iteration += 1
        if error < tolerance:
            print("Converges.")
            return x_middle
        if current_iteration > iterations:
            print("The maximum number of iterations has been reached.")
            return x_middle


def secant_method(fnc, x0, x1, tolerance=0.0005, iterations=10):
    current_iteration = 1
    while True:
        if fnc(x1) == fnc(x0):
            print("Divide by zero.")
            break
        x2 = x1 - fnc(x1) * ((x1 - x0) / (fnc(x1) - fnc(x0)))
        x0 = x1
        x1 = x2
        error = abs((x1 - x0) / x1)
        current_iteration += 1
        if error < tolerance:
            print("Converges.")
            return x2
        if current_iteration > iterations:
            print("The maximum number of iterations has been reached. Could diverge.")
            return x2


def newton_method(fnc, x0, root_multiplicity=1, tolerance=0.0005, iterations=10):
    x_prev = x0
    current_iteration = 1
    while True:
        if derive(fnc, x_prev) is 0:
            print("Divide by zero.")
            break
        x_next = x_prev - root_multiplicity * (fnc(x_prev) / derive(fnc, x_prev))
        error = abs((x_next - x_prev) / x_next)
        x_prev = x_next
        current_iteration += 1
        if error < tolerance:
            print("Converges.")
            return x_prev
        if current_iteration > iterations:
            print("The maximum number of iterations has been reached. Could diverge.")
            return x_prev


def derive(fnc, x):
    h = 0.00001
    return (fnc(x + h) - fnc(x)) / h
