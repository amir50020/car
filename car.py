class Car:
    def __init__(self, engine, speed):
        self.__engine = engine
        self.__speed = speed

    def set_engine(self, engine):
        if type(engine) != bool:
            raise Exception("Engine is not true")
        else:
            self.__engine = engine

    def get_engine(self):
        return self.__engine

    def set_speed(self, speed):
        if type(speed) != int:
            raise Exception("speed is not true")
        if speed < 0:
            raise Exception("speed value is not valid")
        if self.__engine:
            self.__speed = speed
        else:
            raise Exception("Engine is Off")

    def get_speed(self):
        return self.__speed

    def cheek_engine(self):
        return f'Engine is {self.__engine}'

    def __str__(self):
        return f'Engine is {self.__engine}  and Speed is {self.__speed}'
