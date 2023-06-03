class Foo:
    def __init__(self):
        self.called = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        while self.called != 0:
            continue
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.called = 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.called != 1:
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.called = 2


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.called != 2:
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()