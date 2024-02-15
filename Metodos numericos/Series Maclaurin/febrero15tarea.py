import math

def maclaurin_arctan(x, n):
    sum = 0
    for i in range(n):
        term = ((-1)**i) / (2*i + 1) * x**(2*i + 1)
        sum += term
    return sum

# a) Primeros cuatro términos
for i in range(4):
    print(f"Term {i}: {maclaurin_arctan(1, i+1)}")

# b) Estimación de arctan(1/6)
x = 1/6
true_value = math.atan(x)
approx_value = 0
n = 0
error_threshold = 0.001  # Criterio de error

while True:
    n += 1
    approx_value_old = approx_value
    approx_value = maclaurin_arctan(x, n)
    true_error = true_value - approx_value
    approx_error = approx_value - approx_value_old

    if approx_value != 0:
        true_error_percent = true_error / true_value * 100
        approx_error_percent = approx_error / approx_value * 100
    else:
        true_error_percent = 100
        approx_error_percent = 100

    print(f"n={n}, True error={true_error_percent}%, Approx. error={approx_error_percent}%")

    if abs(approx_error_percent) < error_threshold:
        break