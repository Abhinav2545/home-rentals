import random

class Property:
    def __init__(self, property_id, name, location, price, size, availability=True):
        self.property_id = property_id
        self.name = name
        self.location = location
        self.price = price
        self.size = size
        self.availability = availability

    def book(self):
        if self.availability:
            self.availability = False
            return f"{self.name} has been successfully booked."
        return f"{self.name} is not available."

    def __str__(self):
        return f"{self.name} - {self.location} - ${self.price} - {self.size} sqft - {'Available' if self.availability else 'Booked'}"

class HomeRentalSystem:
    def __init__(self):
        self.properties = []

    def add_property(self, property_id, name, location, price, size):
        new_property = Property(property_id, name, location, price, size)
        self.properties.append(new_property)

    def generate_big_data(self, num_entries=1000):
        locations = ["Hyderabad", "Secundrabad", "Kompally", "Jeedimetla", "Miyapur", "Alwal", "Kukatpally"]
        for i in range(1, num_entries + 1):
            name = f"Property {i}"
            location = random.choice(locations)
            price = random.randint(500, 5000)
            size = random.randint(300, 5000)
            self.add_property(i, name, location, price, size)

    def search_by_location(self, location):
        return [prop for prop in self.properties if prop.location.lower() == location.lower()]

    def book_property(self, property_id):
        for prop in self.properties:
            if prop.property_id == property_id:
                return prop.book()
        return "Property not found."

    def list_properties(self, properties, limit=10):
        return '\n'.join(str(prop) for prop in properties[:limit])

    def user_select_property(self):
        locations = ["Hyderabad", "Secundrabad", "Kompally", "Jeedimetla", "Miyapur", "Alwal", "Kukatpally"]
        print("Available Locations:")
        for i, loc in enumerate(locations, 1):
            print(f"{i}. {loc}")
        loc_choice = int(input("Select a location by entering the corresponding number: "))
        selected_location = locations[loc_choice - 1]

        available_properties = self.search_by_location(selected_location)
        if not available_properties:
            print("No properties available in this location.")
            return

        print(f"\nAvailable Properties in {selected_location}:")
        print(self.list_properties(available_properties, 10))
        property_id = int(input("Enter the Property ID to book: "))
        confirmation = self.book_property(property_id)
        print(confirmation)

# Execution
if __name__ == "__main__":
    rental_system = HomeRentalSystem()
    rental_system.generate_big_data(1000)
    print("User selects a property by first choosing a location:")
    rental_system.user_select_property()
    print("\nAll Properties After Booking:")
    print(rental_system.list_properties(rental_system.properties, 80))
