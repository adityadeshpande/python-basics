class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False  # Track the car's state

    def start(self):
        if self.is_running:
            print(f"{self.brand} {self.model} is already running.")
        else:
            self.is_running = True
            print(f"{self.brand} {self.model} is starting.")

    def stop(self):
        if not self.is_running:
            print(f"{self.brand} {self.model} is already stopped.")
        else:
            self.is_running = False
            print(f"{self.brand} {self.model} is stopping.")

mustang = Car("Ford", "Mustang", 2022, "Red")
bmw = Car("BMW", "M3", 2023, "Black")

mustang.start()  # Starts the Mustang
bmw.stop()  # Should print "BMW M3 is already stopped."
mustang.start()  # Should print "Ford Mustang is already running."
bmw.start()  # Starts the BMW
bmw.stop()  # Stops the BMW
