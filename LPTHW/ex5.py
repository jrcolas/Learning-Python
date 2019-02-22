# Exercise 5: More Variables and Printing

name = 'Franck J. Colas'
age = 26
height = 76.0      # inches
weight = 204.0    # lbs
eyes = 'Dark Brown'
teeth = 'White'
hair = 'Black'

# Quick maths
lbsToKg = weight / 2.205
inToCm = height * 2.54

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That's %d cm." % inToCm
print "He's %d pounds light." % weight
print "That's %d kg." % lbsToKg
print "Actually that's not too light."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# Extra tricky line
print "If I add %d, %d, and %d, I get %d." % (
    age, height, weight, age + height + weight
)
