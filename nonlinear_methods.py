def regula_falsi_method():


def bisection_method():


def secant_method():


def newton_method(fnc, x0, iterations, tolerance):
    x_prev = x0
    current_iterations = 1
    error = 1
    while (error > tolerance) and (current_iterations < iterations) and (derive(fnc, x_prev) != 0):
        x_next = x_prev - (fnc(x_prev) / derive(fnc, x_prev))
        error = (x_next - x_prev) / x_next
        x_prev = x_next
    return x_prev


def derive(fnc, x):
    h = 0.00001
    return (fnc(x + h) - fnc(x)) / h
