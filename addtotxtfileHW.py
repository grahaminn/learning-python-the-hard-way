from sys import argv
script, file = argv

target = open(file, 'a+')

n =raw_input("How often do you want to print this? ")

for x in range(1, (int(n)+1)):
	target.write("I must do my homework. print this " + str(n) + " times this is number %d" % (x) + "\n")	

target.close()
