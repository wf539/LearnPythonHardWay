# Set number of cars to 100
cars = 100

# Set available places in a car to 4
space_in_a_car = 4

# Set drivers count to 30
drivers = 30

# Set passengers count to 90
passengers = 90

# Set cars_not_driven count to the difference between cars count and drivers count
cars_not_driven = cars - drivers

# Set cars_driven count to the drivers count
cars_driven = drivers

# Set carpool_capacity to the product of cars_driven and space_in_a_car
carpool_capacity = cars_driven * space_in_a_car

# Set average_passenger_per_car to the passengers count divided by the cars_driven count
average_passenger_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passenger_per_car, "in each car."
