def generate_series(a):
    if a % 2 == 0:
        a -= 1  # Use the previous odd number
    series = [2 * i + 1 for i in range(a)]
    return series
