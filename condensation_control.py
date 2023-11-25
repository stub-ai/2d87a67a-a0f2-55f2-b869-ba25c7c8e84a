import time

class RefrigerationSystem:
    def __init__(self):
        self.condensation_level = 0
        self.condensation_limit = 50  # Set your desired limit

    def read_sensor(self):
        """
        Function to simulate reading the condensation level from a sensor.
        In a real-world application, this method should interface with the sensor and return its current reading.
        """
        # Simulate a change in condensation level
        self.condensation_level += 10
        return self.condensation_level

    def control_device(self, action):
        """
        Function to simulate controlling the condensation.
        In a real-world application, this method should interface with the device that controls condensation.
        """
        if action == "increase":
            print("Increasing condensation...")
            self.condensation_level += 10
        elif action == "decrease":
            print("Decreasing condensation...")
            self.condensation_level -= 10

    def control_condensation(self):
        while True:
            current_level = self.read_sensor()
            print(f"Current condensation level: {current_level}")

            if current_level > self.condensation_limit:
                self.control_device("decrease")
            elif current_level < self.condensation_limit:
                self.control_device("increase")

            time.sleep(1)  # Wait for 1 second

if __name__ == "__main__":
    system = RefrigerationSystem()
    system.control_condensation()