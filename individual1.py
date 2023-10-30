def print_exams(n):
    if n == 1:
        word = "экзамен"
    elif 1 < n < 5:
        word = "экзамена"
    else:
        word = "экзаменов"

    print(f"Мы успешно сдали {n} {word}")

n = int(input("Введите число экзаменов: "))
if n <= 20:
    print_exams(n)
else:
    print("Число экзаменов должно быть меньше или равно 20.")
