from homework_6_module.Road import Road
from homework_6_module.TrafficLight import TrafficLight
from homework_6_module.task_num_3.Position import Position
from homework_6_module.task_num_4.PoliceCar import PoliceCar
from homework_6_module.task_num_4.SportCar import SportCar
from homework_6_module.task_num_4.TownCar import TownCar
from homework_6_module.task_num_4.WorkCar import WorkCar
from homework_6_module.task_num_5.Handle import Handle
from homework_6_module.task_num_5.Pen import Pen
from homework_6_module.task_num_5.Pencil import Pencil
from homework_6_module.task_num_5.Stationery import Stationery

# 1. Создать класс TrafficLight (светофор).

trafficLight = TrafficLight()
trafficLight.running()

# 2. Реализовать класс Road (дорога).

road = Road(5000, 20)
road.asphalt_mass_calc()

# 3. Реализовать базовый класс Worker (работник).

position = Position("Name1", "Surname1", "Data Scientist", {"wage": 100000, "bonus": 2000000})
print(position.get_full_name())
print(position.get_total_income())

# 4. Реализуйте базовый класс Car.

town_car1 = TownCar(70, "Color1", "TownCar1", False)
town_car1.show_speed()
town_car1.go()
town_car1.turn("right")
town_car1.stop()

town_car2 = TownCar(40, "Color2", "TownCar2", False)
town_car2.show_speed()

work_car = WorkCar(40, "Color2", "WorkCar", False)
work_car.show_speed()

police_car = PoliceCar(120, "Color1", "PoliceCar", True)
police_car.show_speed()

sport_car = SportCar(200, "Color1", "SportCar", False)
sport_car.show_speed()

# 5. Реализовать класс Stationery (канцелярская принадлежность).

stationery = Stationery("Stationery")
pen = Pen("Pen")
pencil = Pencil("Pencil")
handle = Handle("Handle")

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
