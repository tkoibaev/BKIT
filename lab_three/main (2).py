from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.sort import sort_arr
from lab_python_fp.print_result import *
from lab_python_fp.cm_timer import *
import time
#from lab_python_fp.process_data import *

def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]


    #______________Задача 1

    # print(field(goods, 'title', 'price'))
    # print(field(goods, 'title', 'color'))
    # print(field(goods, 'color'))


    #______________Задача 2


    #gen_random(5, 1, 3)


    # ______________Задача 3
    # data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    # print(Unique(data))
    # data = gen_random(5, 1, 3)
    # print(Unique(data, ignore_case=True))
    # data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    # print(Unique(data, ignore_case=True))


    # data = [1, 1, 1, 1, 1, 2, 4, 7, 2, 2]
    # for i in Unique(data):
    #    print(i)
    # print('-------------------')
    # data = gen_random(5, 1, 3)
    # for i in Unique(data):
    #    print(i)
    # print('-------------------')
    # data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    # for i in Unique(data):
    #   print(i)



    #______________Задача 4

    # data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    # sort_arr(data)


    # ______________Задача 5
    # test_1()
    # test_2()
    # test_3()
    # test_4()



    # ______________Задача 6

    with cm_timer_1():
       time.sleep(5.5)

    with cm_timer_2():
       time.sleep(5.5)


if __name__ == '__main__':
    main()


