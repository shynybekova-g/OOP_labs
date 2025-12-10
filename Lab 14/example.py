from car_utils import (
    engine_power,
    fuel_consumption,
    oil_change_needed,
    max_speed,
    travel_time,
    speed_warning,
)
from car_utils.helpers import notify, car_tag

print(engine_power(180, 250))
print("Fuel:", fuel_consumption(150, 10))
print("Oil change:", oil_change_needed(12000))
print("Max speed:", max_speed([60, 90, 110, 130]))
print("Travel time:", travel_time(300, 100))
print("Overspeed:", speed_warning(140))
print(notify("Trip started"))
print(car_tag("Honda Civic"))
