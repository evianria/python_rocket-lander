# Python homework 2- rocket-lander game (Jane)


position = 100
velocity = 0
fuel = 100
gravity = -10
thrusters = 0
acceleration = gravity + thrusters

while True:
    print "P:   ", position, "V:   ", velocity, "F: ", fuel
    thrusters = input("Set thrusters(0-20) : ")
    if fuel < thrusters:
        print "Out of fuel! Thrusters at ", fuel
        thrusters = fuel
        fuel = fuel - thrusters
        acceleration = gravity + thrusters
        position = position + velocity + acceleration * 0.5
        velocity = velocity + acceleration
        break
    if thrusters < 0:
        thrusters = 0
        print "No thrusters(thrusters) !"
    if thrusters >= 20:
        thrusters = 20
        print "Thrusters at max(20) !"
    if fuel == 0:
        break

    fuel = fuel - thrusters
    acceleration = gravity + thrusters
    position = position + velocity + acceleration * 0.5
    velocity = velocity + acceleration

    if position <= 0:
        position = 0
        break

if position == 0:
    while True:
        if position <= 0 & abs(velocity) >= 3:
            print "P:   ", position, "V:   ", velocity, "F: ", fuel
            print "Rocket crashed! Velocity was ", velocity, "  m/s"
            break
        elif position <= 0 & abs(velocity) < 3:
            print "P:   ", position, "V:   ", velocity, "F: ", fuel
            print "Landing successful!"
            break

        print "P:   ", position, "V:   ", velocity, "F: ", fuel
        print "No fuel -- rocket is in free-fall!"

        acceleration = gravity
        position = position + velocity + acceleration * 0.5
        velocity = velocity + acceleration

elif fuel == 0:
    while True:
        if position <= 0:
            position = 0
            if abs(velocity) >= 3:
                print "P:   ", position, "V:   ", velocity, "F: ", fuel
                print "Rocket crashed! Velocity was ", velocity, "  m/s"
                break
            else:
                print "P:   ", position, "V:   ", velocity, "F: ", fuel
                print "Landing successful!"
                break

        print "P:   ", position, "V:   ", velocity, "F: ", fuel
        print "No fuel -- rocket is in free-fall!"

        acceleration = gravity
        position = position + velocity + acceleration * 0.5
        velocity = velocity + acceleration