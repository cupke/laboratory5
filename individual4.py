from math import fabs

if __name__=="__main__":
    eps = 1e-10
    x = float(input("Введите значение 0 <= x <= 2: "))
    s_ = 0
    k = 1
    while True:
        prev_s = s_
        s_ += (((-1) ** k) * ((x-1) ** k)) / k**2
        k += 1
        if fabs(prev_s - s_) < eps:
            break
    print(f"Дилогарифм f({x}): ", s_)