class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print(f'Рисуем {pen.title} ручкой')
class Pensil(Stationery):
    def draw(self):
        print(f'Рисуем {pensil.title} карандашом')
class Handle(Stationery):
    def draw(self):
        print(f'Рисуем {handle.title} маркером')

st = Stationery('Добрый день!')
print(st.title)
st.draw()
pen = Pen('синей')
pen.draw()
pensil = Pensil('простым')
pensil.draw()
handle = Handle('водостойким')
handle.draw()
