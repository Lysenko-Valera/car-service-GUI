from admin.create_car.descriptor_car import CarDescriptor


class Car:
    """Класс для инициализации авто и дальнейшей работы с ним.

Класс который содержит атрибуты
brand: str,
model: str,
year: int,
mileage: int,
vin: str
,fuel_type: str,
engine_capacity: float,
gas_tank_capacity: int.
 Атрибуты отбираются по параментрам
которые описанны в на docstrings класса CarDescriptor файла descriptor_car.py
"""
    vin = CarDescriptor() # Создаем экземляры класса дескриптора для применения его
    year = CarDescriptor()
    fuel_type = CarDescriptor()
    engine_capacity = CarDescriptor()
    gas_tank_capacity = CarDescriptor()

    def __init__(self, id:int,  brand: str, model: str, year: int, mileage: int, vin: str
                 ,fuel_type: int, engine_capacity: float, gas_tank_capacity: int, service_id: str, id_mechanic: int):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.vin = vin
        self.fuel_type = fuel_type
        self.engine_capacity = engine_capacity
        self.gas_tank_capacity = gas_tank_capacity
        self.service_id = service_id
        self.id_mechanic = id_mechanic

    def __repr__(self):
        return f'''Класс Car.
        brand: str {self.brand}, model: str {self.model}, year: int {self.year}
        mileage: int {self.mileage}, vin: str {self.vin}'''

    def __str__(self):
        return f'''Приветсвую вас) Брэнд авто - {self.brand}
        Модель авто - {self.model}. Год авто {self.year}. Пробег - {self.mileage}.
        ВИН номер авто - {self.vin}'''

    def __eq__(self, other):
        if not isinstance(other, (int, Car)):
            raise TypeError('Ошибка сравнения. Справа должен быть тип int или Cloak')

        sc = other if isinstance(other, int) else other.mileage
        return self.mileage == sc

    def __hash__(self):
        return hash((self.brand, self.model))

    __age = 0 #Инкапсулируем атрибут где в дальнейшем через property добавляет get & set
    @property
    def set_or_get_age(self):
        self.__age = 2025 - self.year
        return self.__age

    @set_or_get_age.setter
    def set_or_get_age(self, new_age) -> int:
        self.__age = new_age