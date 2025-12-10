def engine_power(hp, torque):
    return f"Engine Power: {hp} HP, Torque: {torque} Nm"

def fuel_consumption(distance_km, liters_used):
    return liters_used / distance_km * 100

def oil_change_needed(km_driven):
    return km_driven >= 10000
