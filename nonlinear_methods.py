def regula_falsi_method():


def bisection_method(fnc, x_left, x_right, iterations, tolerance):
    if fnc(x_left) * fnc(x_right) < 0:
        current_iteration = 1
        error = 1
        while error > tolerance and current_iteration < iterations:
            x_middle = (x_left + x_right) / 2
            if fnc(x_middle) == 0:
                break
            elif fnc(x_middle) * fnc(x_left) > 0:
                x_left = x_middle
            elif fnc(x_middle) * fnc(x_right) > 0:
                x_right = x_middle
            error = (x_right - x_left) / 2
            current_iteration += 1
        return (x_left + x_right)/2


def secant_method():


def newton_method(fnc, x0, iterations, tolerance):
    x_prev = x0
    current_iterations = 1
    error = 1
    while (error > tolerance) and (current_iterations < iterations) and (derive(fnc, x_prev) != 0):
        x_next = x_prev - (fnc(x_prev) / derive(fnc, x_prev))
        error = (x_next - x_prev) / x_next
        x_prev = x_next
        current_iterations += 1
    return x_prev


def derive(fnc, x):
    h = 0.00001
    return (fnc(x + h) - fnc(x)) / h
