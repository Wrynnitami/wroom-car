# Давай дам тебе простую задачку
# , сделай мне машину, которая делает «врум врум» в консоль, когда ты вызываешь функцию move
# Типа класс car, у него есть функция move


# Ну и сразу следующее задание, на завтра так сказать.
#
# 1. Давай добавим машине переменные объем бензобака, остаток топлива (машина создается с пустым баком) и расход топлива
# 2. Каждый врум врум будет стоить нам какого-то количества топлива.
# 3. Если топлива не хватает, в консольку выводится “out of fuel”.
# 4. Машину надо как-то заправлять. Ты можешь залить чуток, а можешь залить до полного.
# 5. Хочу чтобы была функция вывода в консоль остатка топлива

# нужжно прописать параметр делающий все элементы написанными с заглавной буквы
# -----------------

Cars = []


class Car:

    def move(self):

        if self.current_fuel <= 0:
            print("can't move cause - out of fuel")

        else:
            self.current_fuel -= self.consumption
            print(f"{self.color} {self.make} {self.model} does wroom-wroom")
            print(f"{self.current_fuel} gallons of fuel is remains")

    def fill_up(self):

        try:
            filled_gas = int(input("if you want fill up the tank to full, please press 1 \n""if you want fill up the "
                                   "tank to certain amount, please press 2 \n------------------->"))

            if filled_gas == 1:
                self.current_fuel = 50
                print("the tank is full")
                print("че там с деньгами?")

            else:
                filled_gas = int(input("how much fuel do you want to fill :"))
                self.current_fuel += filled_gas
                print(f"the tank is full of {self.current_fuel} of 50 gallons")

        except ValueError:
            print("try again, asshole")

    def make(self):
        pass

    def get_make(self):
        return self.make

    def model(self):
        pass

    def color(self):
        print(f"the color of car is {self.color}")

    def get_сolor(self):
        return self.color

    def fuel(self):

        print(f"current fuel is {self.current_fuel}")

    def get_fuel(self):
        return self.current_fuel

    def gas_tank(self):
        pass

    def get_gas_tank(self):
        return self.gas_tank

    def consumption(self):
        print(f"current consumption of fuel is {self.consumption}")

    def get_consumption(self):
        return self.consumption

    def __repr__(self):
        return repr(self.make)

    def __str__(self):
        return str(self.color)

    def __init__(self, make=None, model=None, color="grey", gas_tank=50, current_fuel=0, consumption=5):
        self.make = make
        self.model = model
        self.color = color
        self.gas_tank = gas_tank
        self.current_fuel = current_fuel
        self.consumption = consumption


try:
    while True:
        to_cars = int(input("Create new vehicle or pick up one from the list \n""for create vehicle, type 1\n""for "
                            "choose existing, type 2 \n""type here: "))

        if to_cars == 1:
            makeAndModel = input("Enter make and model of car : ")

            create_car = int(input("0 - default car, 1 - custom car : "))

            if create_car == 0:
                Cars.append(Car(makeAndModel))

            if create_car == 1:
                print("you can add a several attributes, like a : color of car, volume of tank, current amount of "
                      "fuel and fuel consumption")
                custom_car = int(input("for indicate a color of the car press - 1 \n""for indicate a volume of tank "
                                       "press - 2 for indicate a current amount of fuel press - 3 \n""for indicate a "
                                       "fuel consumption press - 4 "))

                if custom_car == 1:

                if custom_car == 2:

                if custom_car == 3:

                if custom_car == 4:




        if to_cars == 2:
            if not Cars:
                print("There is not cars what a you looking for")

                continue
            print("All cars:")

            for i in range(len(Cars)):
                print(f"{i} - {Cars[i].get_make()}")

            selected_car = int(input("Write a car number : "))

            print(f"you are chose {Cars[i].get_make()}, how do you want to interact?")

            options = int(input(f"available function is : \n1 - to print color of car \n""2 - to print volume of tank "
                                "\n""3 - to print of current fuel \n""4 - to print consumption of fuel \n: "))

            if options == 1:
                print(f"color of selected car is {Cars[i].get_сolor()}\n")

            if options == 2:
                print(f"tank volume of selected car is {Cars[i].get_gas_tank()}\n")

            if options == 3:
                print(f"current fuel of selected car is {Cars[i].get_fuel()}\n")

            if options == 4:
                print(f"consumption of fuel of selected car is {Cars[i].get_consumption()}\n")


        # else:
        #     break - на будущее, для выхода из цикла


except ValueError:
    print("screw you guys, i'm going home")

# Prius = Car("Toyota", "Prius","gray", 50,0,1)

