# Difference between format strings %r vs %s.
# %r is used for debugging to see the actual raw data. %s is used to display to users.
print "I said: %r" % "There are %d types of people" % 10
print "I said: %s" % "There are %d types of people" % 10