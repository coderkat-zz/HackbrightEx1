import random

print "Hello! Kat and Kelley welcome you to this awesome game."
print "What is your name?", 
name = raw_input()

print "What do you want your range to be?"
low = int(raw_input("Low number: "))
high = int(raw_input("High number: "))

number = random.randint(low, high+1)

i = 0

print "Please guess a number between %d and %d." % (low, high)

while True:
	guess = int(raw_input("> "))
	i += 1
	if guess < number:
		print "Your guess is too low, try again"
		continue
	elif guess > number:
		print "Your guess is too high, try again"
		continue
	else:
		print "Well done, %s! You found my number in %d tries" % (
			name, i)
		break





