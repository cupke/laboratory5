a1, b1, c1 = map(float, input("Введите коэффициенты первой прямой (a1, b1, c1): ").split())
a2, b2, c2 = map(float, input("Введите коэффициенты второй прямой (a2, b2, c2): ").split())

det = a1*b2 - a2*b1

if det == 0:
    print("Прямые параллельны или совпадают")
else:
    x = (b2*c1 - b1*c2) / det
    y = (a1*c2 - a2*c1) / det
    print(f"Точка пересечения: ({x}, {y})")
