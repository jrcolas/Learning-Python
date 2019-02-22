# Exercise 6: String and text

# Declarations
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

nine_plus_ten = 9 + 10

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e

print "What's 9 + 10? %d" % (nine_plus_ten + 2)
