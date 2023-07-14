class Manufacturer:
    """Represents a car manufacturer."""

    def __init__(self, name, location):
        """Initializes a new manufacturer object."""
        self.name = name
        self.location = location
        self.brands = []

    def add_brand(self, brand):
        """Adds a new brand of car to the manufacturer's list of brands."""
        self.brands.append(brand)

    def get_brands(self):
        """Returns the list of brands produced by the manufacturer."""
        return self.brands


class Car:
    """Represents a car object."""

    def __init__(self, brand, model, year):
        """Initializes a new car object."""
        self.brand = brand
        self.model = model
        self.year = year

    def get_details(self):
        """Prints the details of the car (brand, model, and year)."""
        print(f"{self.brand} {self.model} ({self.year})")


def main():
    """Demonstrates the relationship between the Manufacturer and Car classes."""

    # Create two manufacturer objects.
    toyota = Manufacturer("Toyota", "Japan")
    ford = Manufacturer("Ford", "United States")

    # Add different brands of cars to each manufacturer.
    toyota.add_brand("Corolla")
    toyota.add_brand("Camry")
    ford.add_brand("Mustang")
    ford.add_brand("Explorer")

    # Create multiple car objects for each manufacturer.
    corolla = Car("Toyota", "Corolla", 2023)
    camry = Car("Toyota", "Camry", 2022)
    mustang = Car("Ford", "Mustang", 2021)
    explorer = Car("Ford", "Explorer", 2020)

    # Print the details of the cars.
    print("Toyota cars:")
    corolla.get_details()
    camry.get_details()
    print("\nFord cars:")
    mustang.get_details()
    explorer.get_details()


if __name__ == "__main__":
    main()
