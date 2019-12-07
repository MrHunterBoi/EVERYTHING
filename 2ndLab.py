while True:
	print('''1. Calculate quantity of letters in word
2. Make words in alphabetical order
3. Make word reversed
4. Exit''')
	choice = input("Please choose something: ")
	if choice == "1":
		word = input("Enter some text for calculation: ")
		a='abcdefghijklmnopqrstuvwxyz'
		for i in range(len(a)):
			word.count(a[i])
			if word.count(a[i]) == 0:
				pass
			else:
				print(a[i], '=', word.count(a[i]))
	if choice == "2":
		text = input("Enter sum text here: ")
		a = text.split(" ")
		a = list(set(a))
		a.sort()
		print("Your words are: ")
		for i in range(len(a)):
			print(a[i])
		print()
	if choice == "3":
		text = input("Plese enter some text for le reverse: ")
		ttext = text[::-1]
		print(ttext)
	elif choice == "4":
		print("Stopping...")
		break
	else:
		pass
input()

