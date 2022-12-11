import unittest
from rk1re import Musician, Orchestra, MusOrch, A1, A2, A3


class test(unittest.TestCase):

    def setUp(self):
        self.orch = [
    Orchestra(1, 'оркестр 1'),
    Orchestra(2, 'оркестр 2'),
    Orchestra(3, 'оркестр 3'),
]
        self.mus = [
    Musician(1, 'Холмогоров', 25, 1),
    Musician(2, 'Пчелкин', 31, 1),
    Musician(3, 'Белый', 19, 2),
    Musician(4, 'Филатов', 44, 2),
    Musician(5, 'Лапшин', 50, 3),
    Musician(6, 'Шмидт', 22, 4)
]
        self.mus_orch = [
    MusOrch(1, 1),
    MusOrch(1, 2),
    MusOrch(2, 3),
    MusOrch(2, 4),
    MusOrch(3, 5),
    MusOrch(3, 6)
]

    def test_A1(self):
        expected_result = [('Холмогоров', 25, 'оркестр 1'),
                           ('Пчелкин', 31, 'оркестр 1'),
                           ('Белый', 19, 'оркестр 2'),
                           ('Филатов', 44, 'оркестр 2'),
                           ('Лапшин', 50, 'оркестр 3')]

        result = A1(self.orch, self.mus)
        self.assertEqual(result, expected_result)

    def test_A2(self):
        expected_result = [('оркестр 2', 63),
                           ('оркестр 1', 56),
                           ('оркестр 3', 50)]
        result = A2(self.orch, self.mus)
        self.assertEqual(result, expected_result)

    def test_A3(self):
        expected_result = {'оркестр 2': ['Белый', 'Филатов'], 'оркестр 3': ['Лапшин', 'Шмидт']}
        result = A3(self.orch, self.mus,'1')
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()