def read_chip():
    # Mock implementation: returns a random chip ID
    import random
    return f"CHIP-{random.randint(1000, 9999)}"

def get_chip_location():
    # Mock implementation: returns a random location
    import random
    locations = ["Entrance", "Exit", "Station", "Platform"]
    return random.choice(locations)

