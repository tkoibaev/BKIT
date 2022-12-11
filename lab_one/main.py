import math
import sys


def get_coef(index, prompt):
    try:
        coef_str = float(sys.argv[index])
    except:
        print(prompt)
        coef_str = input()
        while type(coef_str) != float:
            try:
                coef_str = float(coef_str)
            except:
                print(prompt)
                coef_str = input()
    return coef_str


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    result_x = []
    if a == 0 and b == 0:
        print('Корней нет')
        sys.exit()
    elif a == 0:
        root = (-c / b)
        if root > 0:
            result_x.append(-(root ** 0.5))
            result_x.append(root ** 0.5)
            for i in range(len(result_x)):
                print(result_x[i])
        else:
            print('Корней нет')
            sys.exit()
    else:
        result_t = []

        d = b * b - 4 * a * c
        if (d < 0.0):
            print('Корней нет')
            sys.exit()
        elif d == 0.0:
            root = -b / (2.0 * a)
            result_t.append(root)

        elif d > 0.0:
            sqd = d ** 0.5
            root1 = (-b + sqd) / (2.0 * a)
            root2 = (-b - sqd) / (2.0 * a)
            result_t.append(root1)
            result_t.append(root2)

        result_x = []
        for i in range(len(result_t)):
            if (result_t[i] == 0):
                root1 = 0
                result_x.append(root1)
            elif (result_t[i] > 0):
                root1 = -(result_t[i] ** 0.5)
                root2 = (result_t[i] ** 0.5)
                result_x.append(root1)
                result_x.append(root2)

        for i in range(len(result_x)):
            print(result_x[i])


if __name__ == "__main__":
    main()
