while True:
	print("""Menu:
1. Print 'Hello World'
2. Multiply letters of word by 2
3. Make word reversed
4. Calculator
5. Caesar code
6. Exit""")
	choice = int(input("Please choose: "))
	if choice == 1:
		print("Hello World")
	elif choice == 2:
		text = list(str(input("Enter text: ")))
		text1 = list()
		for i in range(len(text)):
			text1.append(text[0+i])
			text1.append(text[0+i])
		print(text1)
	elif choice == 3:
		text = input("Enter some text: ")
		ttext = text[::-1]
		text1 = input("Enter sum numbers: ")
		ttext1 = text1[::-1]
		print(ttext,ttext1)
	elif choice == 4:
		while True:
			a = float(input("First number: "))
			b = float(input("Second number: "))
			do = str(input("Operation: "))
			if do == "+":
				print(a + b)
			elif do == "-":
				print(a - b)
			elif do == "*":
				print(a * b)
			elif do == "/":
				if b == 0:
					print("Impossible operation")
				else:
					print(a / b)
			else:
				print("Invalid operation")
			break
	elif choice == 5:
		text = list(input("Enter some text here: "))
		a = 'abcdefghijklmnopqrstuvwxyza01234567890'
		for i in range(len(text)):
			for j in range(len(a) - 1):
				if text[i] == a[j]:
					text[i] = a[j + 1]
					break
				else:
					pass
		print(text)
	elif choice == 6:
		break
	else:
		pass	