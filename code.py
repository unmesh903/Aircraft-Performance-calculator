#hi
fuel_capacity = float(input("Enter Fuel capacity in Gallons: "))
fuel_consumption = float(input("Enter Fuel consumption in Gallons per hour : "))
true_air_speed = float(input("Enter True Air Speed in Knots: "))
payload = float(input("Enter Payload in Pounds: "))
fuel_weight = float(input("Enter Fuel weight in Pounds: "))
moment_list = float(input("Enter Moment list in Pound-feets: "))
cl = float(input("Enter CL: "))
rho = float(input("Enter Rho: "))
v = float(input("Enter Velocity in m/s: "))
s = float(input("Enter Wing area in m^2: "))
cd = float(input("Enter CD: "))
mass = float(input("Enter Mass in kg: "))
g = 9.81
thrust = float(input("Enter Thrust in Newtons: "))
drag = float(input("Enter Drag in Newtons: "))
velocity = float(input("Enter initial Velocity in m/s: "))
acceleration = float(input("Enter Acceleration in m/s^2: "))
time = float(input("Enter Time in seconds: "))

# performance calculations code

def calcuate_range(fuel_capacity, fuel_consumption, true_air_speed):
    range = (fuel_capacity / fuel_consumption) * true_air_speed
    return range
def calculate_endurance(fuel_capacity, fuel_consumption):
        endurance = fuel_capacity / fuel_consumption
        return endurance
def calculate_total_weight(payload, fuel_weight):
    total_weight = payload + fuel_weight
    return total_weight
def calculate_cg_position(moment_list, total_weight):
    total_moment = sum(moment_list)
    cg_position = total_moment / total_weight
    return cg_position
def calculate_moment(weight, arm):
    moment = weight * arm
    return moment 
def calculate_lift(cl, rho, v, s):
    lift = 0.5 * cl * rho * v**2 * s
    return lift
def calculate_drag(cd, rho, v, s):
    drag = 0.5 * cd * rho * v**2 * s
    return drag
def calculate_weight(mass, g):
    weight = mass * g
    return weight
def calculate_acceleration(thrust, drag, weight):
    net_force = thrust - drag - weight
    acceleration = net_force / mass
    return acceleration
def calculate_velocity(initial_velocity, acceleration, time):
    final_velocity = initial_velocity + acceleration * time
    return final_velocity
def calculate_distance(velocity, time):
    distance = velocity * time
    return distance

#printing results
print("Range: ", calcuate_range(fuel_capacity, fuel_consumption, true_air_speed), "nautical miles")
print("Endurance: ", calculate_endurance(fuel_capacity, fuel_consumption), "hours")
print("Total Weight: ", calculate_total_weight(payload, fuel_weight), "pounds")
print("CG Position: ", calculate_cg_position(moment_list, calculate_total_weight(payload, fuel_weight)), "pounds")
print("Lift: ", calculate_lift(cl, rho, v, s), "Newtons")
print("Drag: ", calculate_drag(cd, rho, v, s), "Newtons")
print("Weight: ", calculate_weight(mass, g), "Newtons")
print("Acceleration: ", calculate_acceleration(thrust, calculate_drag(cd, rho, v, s), calculate_weight(mass, g)), "m/s^2")
print("Final Velocity: ", calculate_velocity(velocity, calculate_acceleration(thrust, calculate_drag(cd, rho, v, s), calculate_weight(mass, g)), time), "m/s")
print("Distance: ", calculate_distance(calculate_velocity(velocity, calculate_acceleration(thrust, calculate_drag(cd, rho, v, s), calculate_weight(mass, g)), time), time), "m")