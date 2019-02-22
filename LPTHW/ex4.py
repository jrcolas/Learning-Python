# cars - Defines the number of cars
# space_in_a_car - Defines how much people a car can hold
# drivers - Defines how many drivers are available to drive today
# passengers - Defines the number of passengers wanting to ride today
# cars_not_driven - Defines the number of cars that won't have a driver
# cars_driven - Defines the number of cars that will have a driver
# carpool_capacity - Defines the number of people a car can hold
# average_passengers_per_car - Defines the average number of people needing
#       to be in a car today
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
