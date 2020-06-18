# https://leetcode-cn.com/problems/traffic-light-controlled-intersection/

from threading import Lock


class TrafficLight(object):
    def __init__(self):
        self.currentIsA = 1
        self.lock = Lock()

    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        """
        :type roadId: int --> // ID of the car
        :type carId: int --> // ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        :type direction: int --> // Direction of the car
        :type turnGreen: method --> // Use turnGreen() to turn light to green on current road
        :type crossCar: method --> // Use crossCar() to make car cross the intersection
        :rtype: void
        """
        if roadId != self.currentIsA:
            turnGreen()
            self.currentIsA = roadId
        try:
            self.lock.acquire()
            crossCar()
        finally:
            self.lock.release()
