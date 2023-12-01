def regula_falsi_method(fnc, x0, x1, iterations, tolerance):
    current_iteration = 1
    error = 1
    while error > tolerance and current_iteration < iterations:
        x2 = x1 - ((fnc(x1) * (x1 - x0)) / (fnc(x1) - fnc(x0)))
        error = abs(x1 - x0)
        if fnc(x0) * fnc(x2) > 0:
            x0 = x2
        elif fnc(x1) * fnc(x2) > 0:
            x1 = x2
        current_iteration += 1


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
        return (x_left + x_right) / 2


def secant_method(fnc, x0, x1, iterations, tolerance):
    current_iteration = 1
    error = 1
    while error > tolerance and current_iteration < iterations:
        x2 = x1 - fnc(x1) * ((x1 - x0) / (fnc(x1) - fnc(x0)))
        x0 = x1
        x1 = x2
        error = abs((x1 - x0) / x1)
        current_iteration += 1
    return x1


def newton_method(fnc, x0, iterations, tolerance):
    x_prev = x0
    current_iteration = 1
    error = 1
    while (error > tolerance) and (current_iteration < iterations) and (derive(fnc, x_prev) != 0):
        x_next = x_prev - (fnc(x_prev) / derive(fnc, x_prev))
        error = abs((x_next - x_prev) / x_next)
        x_prev = x_next
        current_iteration += 1
    return x_prev


def derive(fnc, x):
    h = 0.00001
    return (fnc(x + h) - fnc(x)) / h
