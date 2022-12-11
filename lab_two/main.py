import cowsay
#import emoji
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle("синего", 6.8, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)
    cowsay.trex('привет!')
    r.FIGURE_TYPE='cat'
    print(r.FIGURE_TYPE)
    print(emoji.emojize('Salam :thumbs_up:'))

if __name__ == "__main__":
    main()
