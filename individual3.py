for number in range(10, 100):
    digit_sum = sum(int(digit) for digit in str(number))
    if number == digit_sum + digit_sum**2:
        print(number)
