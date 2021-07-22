from time import sleep

class TrafficLight:
    __color = ['red', 'yello', 'green']
    def running(self):
        i = 0
        while i != 3:
            print(f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(9)
            i += 1

tl = TrafficLight()
tl.running()
