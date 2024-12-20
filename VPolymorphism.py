class Car:
    def start_engine(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def stop_engine(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def drive(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class BMW(Car):
    def start_engine(self):
        return "BMW engine started."

    def stop_engine(self):
        return "BMW engine stopped."

    def drive(self):
        return "Driving the BMW."


class Ferrari(Car):
    def start_engine(self):
        return "Ferrari engine started."

    def stop_engine(self):
        return "Ferrari engine stopped."

    def drive(self):
        return "Driving the Ferrari."

def test_car(car: Car):
    print(car.start_engine())
    print(car.drive())
    print(car.stop_engine())

if __name__ == "__main__":
    bmw = BMW()
    ferrari = Ferrari()

    print("Testing BMW:")
    test_car(bmw)

    print("\nTesting Ferrari:")
    test_car(ferrari)