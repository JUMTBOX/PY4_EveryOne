class Car:
    model = ""
    color = ""
    speed = 0

    def drive(self):
        print(f"{self.color} {self.model}가 주행합니다.")

    def park(self):
        print("주차합니다.")

    def speedUp(self, val):
        self.speed += val
        print(f"현재 속도는 {self.speed} 입니다.")

    def speedDown(self, val):
        self.speed -= val
        print(f"현재 속도는 {self.speed} 입니다.")


car1 = Car()

car1.color = "검정색"
car1.model = "벤츠 "
car1.drive()
car1.speedUp(80)
car1.speedDown(20)
