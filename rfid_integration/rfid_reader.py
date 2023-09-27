def read_chip():
    # Mock-Implementierung: gibt eine zufällige Chip-ID zurück
    import random
    return f"CHIP-{random.randint(1000, 9999)}"

def get_chip_location():
    # Mock-Implementierung: gibt einen zufälligen Standort zurück
    import random
    locations = ["Eingang", "Ausgang", "Bahnhof", "Bahnsteig"]
    return random.choice(locations)


