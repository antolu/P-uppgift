from queueADT import *
import classes
import time
import random

def noErrands():
	errands = 1
	while random.randrange(0,2) == 1:
		errands += 1
	return errands

def newCustomer():
	if random.randrange(0,6) == 5:
		return True

def enterCustomer():
	global beingServed
	global kundnr
	global customer
	if newCustomer() and storeOpen:														# kollar varje minut om en nu kund kommer in
		if queue.isEmpty() and not beingServed:
			customer = classes.person(kundnr)
			beingServed = True
			print(time.get() , " kommer kund " , customer.kundnr , " in och blir genast betjänad.")
			kundnr += 1
			beingServed = True
#			return queue, beingServed, customer, kundnr
		else:												# annars ställs personen i kön
			queue.put(classes.person(kundnr))
			kundnr += 1
			print(time.get() , " kommer kund " , kundnr-1 , " in och ställer sig i kön som nr." , queue.length)
#			return queue, beingServed, None, kundnr
#			funktionsargument: storeOpen, queue, beingServed, kundnr, time

def updateCheck():
	global beingServed
	global consumedTime
	global time
	global customer
	if beingServed is True:									# om en kund betjänas så ökas tiden det har tagit för ärendena
		if consumedTime == 2*customer.errands:				# om den konsumerade tiden nått 2 * ärenden minuter lämnar kunden disken och en kund hämtas från kön.
			if not queue.isEmpty():
				print(time.get() , " går kund " , customer.kundnr , " och kund " , (customer.kundnr+1) , "blir betjänad.")
				customer = queue.get()
				consumedTime = 0
			else:
				print(time.get() , " går kund ", customer.kundnr)
				beingServed = False

		consumedTime += 1
	#return queue, beingServed, customer, consumedTime
	#funktionsargument: queue, beingServed, customer, time, consumedTime

def timeCheck():
	global time
	if time.current == 1080:
		print("Dörren stängdes 18:00")
		storeOpen = False

time = classes.time() # kl 9:00
kundnr = 1
consumedTime = 0
storeOpen = True
beingServed = False

queue = queue()


while True:
	enterCustomer()

	updateCheck()

	timeCheck()

	if time.current >= 1080 and queue.isEmpty():
		break

	time += 1

print("STATISTIK: " , kundnr , "kunder betjänades.")