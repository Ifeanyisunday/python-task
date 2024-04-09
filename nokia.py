prompt = """\tList of menu functions

	1. Phone book
	2. Messages
	3. Chat
	4. Call register
	5. Tones
	6. Settings
	7. Call divert
	8. Games
	9. Calculator
	10. Reminders
	11. Clock
	12. profiles
	13. Sim services"""

print(prompt)

menu = int(input("Press number: "))
match menu:
	case 1:	
		phonebookp = ("""\t\tPhoneboook

		1. Search
		2. Services Nos
		3. Add name
		4. Erase
		5. Edit
		6. Assign Tone
		7. Send b'card
		8. Options
		9. Speed dials
		10.Voice tags
		0.back""")	
		print(phonebookp)
		
		phonebook = int(input("Press number: "))
		match phonebook:
			case 1:
				print("Search")
			case 2:
				print("Service Nos")
			case 3:
				print("Add name")
			case 4:
				print("Erase")
			case 5:
				print("Edit")
			case 6:
				print("Assign tone")
			case 7:
				print("Send b'card")
			case 8:
				optionsp = """\t\t\t\toptions
				1. Type of view
				2. Memory status
				0. Back""";
				print(optionsp)
		
				options = int(input("Press number: "))
				match options:
					case 1:
						print("Type of view")
					case 2:
						print("Memory status")
					case 0:
						print(prompt)
			case 9:
				print("Speed dials")
			case 10:
				print("Voice tags")
			case 0:
				print(prompt)
	
	case 2: messagesp = ("""\t\tmessages

		1. Write messages
		2. Onbox
		3. Outbox
		4. Picture messages
		5. Templates
		6. Smileys
		7. Message settings
		8. Info service
		9. Voice mailbox number
		10.Service command editor
		0.Back""")
		print(messagesp)
		
		messages = int(input("Press number: "))
		match messages:
			case 1:
				print("Write messages")
			case 2:
				print("Inbox")
			case 3:
				print("Outbox")
			case 4:
				print("Picture messages")
			case 5:
				print("Templates")
			case 6:
				print("Smileys")			 
        	
	case 3:
        	print("chat")
	case 4:
        	print("call register")
	case 5:
        	print("tone")
	case 6:
        	print("settings")
	case 7:
        	print("call divert")
	case 8:
        	print("games")
	case 9:
        	print("caculator")
	case 10:
        	print("reminders")
	case 11:
        	print("clock")
	case 12:
        	print("profiles")
	case 13:
        	print("sim services")