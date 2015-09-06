formatter = "%r %r %r %r"
non_r = "%s %s %s %s"

print formatter % (2, 2, 2, 2)
print formatter % (True, 2, 2, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("Check this out", "Formatters", "Like percent r", "Gives you Raw Data")
print non_r % ("Check this out", "Formatters", "Like percent s", "Does NOT gives you Raw Data")