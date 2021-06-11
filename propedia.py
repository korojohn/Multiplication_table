number = input("Ήρθε η ώρα να μάθουμε την προπαίδεια του ")
for n in range(11):
	wrong = True
	while wrong:
		question = f"{n} x {number} = "
		answer = input(question)
		if answer == "γεια": exit()
		if answer == "ΓΕΙΑ": exit()
		if answer == "γειά": exit()
		if answer == "Γειά": exit()
		if int(answer) == (n * int(number)):
			print('Μπράβο!!')
			wrong = False
		else:
			print('Δοκίμασε ξανά!')