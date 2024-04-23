def nokia():
	prompt = """\tList of menu functions

	1 -> Phone book
	2 -> Messages
	3 -> Chat
	4 -> Call register
	5 -> Tones
	6 -> Settings
	7 -> Call divert
	8 -> Games
	9 -> Calculator
	10 -> Reminders
	11 -> Clock
	12 -> profiles
	13 -> Sim services"""

	print(prompt)

	menu = int(input("Press number: "))
	match menu:
		case 1:	
			phonebookp = """\t\tPhoneboook

			1 -> Search
			2 -> Services Nos
			3 -> Add name
			4 -> Erase
			5 -> Edit
			6 -> Assign Tone
			7 -> Send b'card
			8 -> Options
			9 -> Speed dials
			10 -> Voice tags
			0 -> back"""	
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
					optionsp = """\t\t\toptions
					1. Type of view
					2. Memory status
					0. Back"""
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

	case 2:
		messagesP = """
 		1 -> Write messages
 		2 -> Inbox
 		3 -> Outbox
 		4 -> Pictures messages
		5 -> Templates
 		6 -> Simleys
 		7 -> Message settings
 		8 -> Info service
 		9 -> Voice mailbox number
 		10 -> Service command editor
		0 -> Back"""
		print(messagesP)
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
			case 7:
				messagesettingsp = """\t\t\t\tMessage settings
				1 -> Set1
				2 -> Common"""
				print(messagesettingsp)
				messagesetting = int(input("Press number: "))
				match messagesetting:
					case 1:
						Set1p = """\t\t\tSet1
						1 -> Message centre number
						2 -> Message sent as
						3 -> Message validity
						0 -> back"""
						Set1 = int(input("Press number: "))
						match Set:
							case 1:
								print("Message centre number")
							case 2:
								print("Message sent as")
							case 3:
								print("Message validity")
							case 0:
								print(prompt)
					case 2:
						Commonp = """\t\t\t\t\t\tcommon
						1 -> Message centre number
						2 -> Message sent as
						3 -> Message validity
						0 -> back"""
						print(Commonp)
						common = int(input("Press number: "))
						match common:
							case 1: 
								print("Delivery report")
							case 2: 
								print("Reply via same centre")
							case 3: 
								print("Character support")
							case 0: 
								print(prompt)
			case 8:
				print("Info service")
			case 9:
				print("Voice mailbox number")
			case 10:
				print("Service command editor")
			case 0:
				print(prompt)

	case 3:
		print("Chat")
	
	case 4:
		callregisterp = """\t\tCall register
		1 -> Missed calls
		2 -> Received calls
		3 -> Dialled numbers
		4 -> Erase recent call lists
		5 -> Show call duration
		6 -> Show call costs
		7 -> Call cost settings
		8 -> Prepaid credit
		0 -> Back"""
		print(callregisterp)
		callregister = int(input("Press number: "))
		match callregister:
			case 1:
				print("Missed calls")
			case 2:
				print("Received calls")
			case 3:
				print("Dialled numbers")
			case 4:
				print("Erase recent call lists")
			case 5:
				calldurationp ="""\t\t\tShow call duration
				1 -> Last call duration
				2 -> All calls duration
				3 -> Recevived calls duration
				4 -> Dialled calls duration
				5 -> Clear timers
				0 -> Back"""
				print(calldurationp)
				callduration = int(input("Press number: "))
				match callduration:
					case 1: 
						print("Last call duration")
					case 2: 
						print("All calls duration")
					case 3: 
						print("Recevived calls duration")
					case 4: 
						print("Dialled calls duration")
					case 5: 
						print("Clear timers")
					case 0: 
						print(prompt)
			case 6:
				showcostsp ="""\t\t\tShow call costs
				1 -> Last call cost
				2 -> All calls cost
				3 -> Clear counters
				0 -> Back"""
				print(showcostsp)
				showcost = int(input("Press number: "))
				match showcost:
					case 1:
						print("Last call cost")
					case 2:
						print("All calls cost")
					case 3:
						print("Clear counters")
					case 0:
						print(prompt)
			case 7:
				callcostp ="""\t\t\tcall cost settings
				1 -> Call cost limit
				2 -> Show costs in
				0 -> Back"""
				print(callcostp)
				callcost = int(input("Press number: "))
				match callcost:
					case 1:
						print("Call cost limit")
					case 2:
						print("Show costs in")
					case 0:
						print(prompt)
			case 8:
				print("Prepaid credit")
	case 5:
		tonesp = """\t\tTones
		1 -> Ringing tone
		2 -> Ringing volume
		3 -> Incoming call alert
		4 -> Composer
		5 -> Message alert tone
		6 -> Keypad tones
		7 -> Warning and games tones
		8 -> Viberating alert
		9 -> Screen saver
		0 -> Back"""
		print(tonesp)
		tones = int(input("Press number: "))
		match tones:
			case 1:
				print("Ringing tone")
			case 2:
				print("Ringing volume")
			case 3:
				print("Incoming call alert")	
			case 4:
				print("Composer")	
			case 5:
				print("Message alert tone")	
			case 6:
				print("Keypad tones")	
			case 7:
				print("Warning and games tones")	
			case 8:
				print("Viberating alert")	
			case 9:
				print("Screen saver")	
			case 0:
				print(prompt)
	case 6:
		settingsp = """\t\tSetings
		1 -> Call settings
		2 -> Phone settings
		3 -> Security settings
		4 -> Restore factory settings
		0 -> Back"""
		print(settingsp)
		settings = int(input("Press number: "))
		match settings:
			case 1:
				callsettingsp = """\t\tcallsettings
				1 -> Automatic redial
				2 -> Speed dialling
				3 -> Call waiting options
				4 -> Own number sending
				5 -> Phone line in use
				6 -> Automatic answer
				0 -> Back"""
				print(callsettingsp)
				callsettings = int(input("Press number: "))
				match settings:
					case 1:
						print("Automatic redial")
					case 2:
						print("Speed dialling")
					case 3:
						print("Call waiting options")	
					case 4:
						print("Own number sending")	
					case 5:
						print("Phone line in use")	
					case 6:
						print("Automatic answer")
					case 0:
						print(prompt)
			case 2:
				phonesettingsp = """\t\tphonesettings
				1 -> Language
				2 -> Cell info display
				3 -> Welcome note
				4 -> Network selection
				5 -> Lights
				6 -> Confirm sim service actions
				0 -> Back"""
				print(phonesettingsp)
				phonesettings = int(input("Press number: "))
				match phonesettings:
					case 1:
						print("Language")
					case 2:
						print("Cell info display")
					case 3:
						print("Welcome note")	
					case 4:
						print("Network selection")	
					case 5:
						print("Lights")	
					case 6:
						print("Confirm sim service actions")
					case 0:
						print(prompt)
			case 3:
				securitysettingsp = """\t\tsecuritysettings
				1 -> Pin code request
				2 -> Call barring service
				3 -> Fixed dialling
				4 -> Closed user group
				5 -> Phone security
				6 -> Change access codes
				0 -> Back"""
				print(securitysettingsp)
				securitysettings = int(input("Press number: "))
				match securitysettings:
					case 1:
						print("Pin code request")
					case 2:
						print("Call barring service")
					case 3:
						print("Fixed dialling")	
					case 4:
						print("Closed user group")	
					case 5:
						print("Phone security")	
					case 6:
						print("Change access codes")
					case 0:
						print(prompt)	
			case 4:
				print("Restore factory settings")
	case 7:
		print("Call divert")
	case 8:
		print("Games")
	case 9:
		print("Calculator")
	case 10:
		print("Reminders")
	case 11:
		clockp = """\t\tClock
		1 -> Alarm clock
		2 -> Clock settings
		3 -> Date settings
		4 -> Stopwatch
		5 -> Countdown timer
		6 -> Auto update of date and time
		0 -> Back"""
		print(clockp)
		clock = int(input("Press number: "))
		match clock:
			case 1:
				print("Alarm clock")
			case 2:
				print("Clock settings")
			case 3:
				print("Date settings")	
			case 4:
				print("Stopwatch")	
			case 5:
				print("Countdown timer")	
			case 6:
				print("Auto update of date and time")
			case 0:
				print(prompt)
	case 12:
		print("Profile")
	case 13:
		print("Sim services")































prompt = """\tList of menu functions

	1 -> Phone book
	2 -> Messages
	3 -> Chat
	4 -> Call register
	5 -> Tones
	6 -> Settings
	7 -> Call divert
	8 -> Games
	9 -> Calculator
	10 -> Reminders
	11 -> Clock
	12 -> profiles
	13 -> Sim services"""

print(prompt)

menu = int(input("Press number: "))
match menu:
	case 1:	
		phonebookp = """\t\tPhoneboook

		1 -> Search
		2 -> Services Nos
		3 -> Add name
		4 -> Erase
		5 -> Edit
		6 -> Assign Tone
		7 -> Send b'card
		8 -> Options
		9 -> Speed dials
		10 -> Voice tags
		0 -> back"""	
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
				optionsp = """\t\t\toptions
			1. Type of view
			2. Memory status
			0. Back"""
				print(optionsp)
		
				options = int(input("Press number: "))
				match options:
					case 1:
						print("Type of view")
					case 2:
						print("Memory status")
					case 0:
						def nokia()
			case 9:
				print("Speed dials")
			case 10:
				print("Voice tags")
			case 0:
				def nokia()

	case 2:
		messagesP = """
 		1 -> Write messages
 		2 -> Inbox
 		3 -> Outbox
 		4 -> Pictures messages
		5 -> Templates
 		6 -> Simleys
 		7 -> Message settings
 		8 -> Info service
 		9 -> Voice mailbox number
 		10 -> Service command editor
		0 -> Back"""
		print(messagesP)
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
			case 7:
				messagesettingsp = """\t\t\t\tMessage settings
				1 -> Set1
				2 -> Common"""
				print(messagesettingsp)
				messagesetting = int(input("Press number: "))
				match messagesetting:
					case 1:
						Set1p = """\t\t\tSet1
						1 -> Message centre number
						2 -> Message sent as
						3 -> Message validity
						0 -> back"""
						Set1 = int(input("Press number: "))
						match Set:
							case 1:
								print("Message centre number")
							case 2:
								print("Message sent as")
							case 3:
								print("Message validity")
							case 0:
								print(prompt)
					case 2:
						Commonp = """\t\t\t\t\t\tcommon
						1 -> Message centre number
						2 -> Message sent as
						3 -> Message validity
						0 -> back"""
						print(Commonp)
						common = int(input("Press number: "))
						match common:
							case 1: 
								print("Delivery report")
							case 2: 
								print("Reply via same centre")
							case 3: 
								print("Character support")
							case 0: 
								print(prompt)
			case 8:
				print("Info service")
			case 9:
				print("Voice mailbox number")
			case 10:
				print("Service command editor")
			case 0:
				print(prompt)

	case 3:
		print("Chat")
	
	case 4:
		callregisterp = """\t\tCall register
		1 -> Missed calls
		2 -> Received calls
		3 -> Dialled numbers
		4 -> Erase recent call lists
		5 -> Show call duration
		6 -> Show call costs
		7 -> Call cost settings
		8 -> Prepaid credit
		0 -> Back"""
		print(callregisterp)
		callregister = int(input("Press number: "))
		match callregister:
			case 1:
				print("Missed calls")
			case 2:
				print("Received calls")
			case 3:
				print("Dialled numbers")
			case 4:
				print("Erase recent call lists")
			case 5:
				calldurationp ="""\t\t\tShow call duration
				1 -> Last call duration
				2 -> All calls duration
				3 -> Recevived calls duration
				4 -> Dialled calls duration
				5 -> Clear timers
				0 -> Back"""
				print(calldurationp)
				callduration = int(input("Press number: "))
				match callduration:
					case 1: 
						print("Last call duration")
					case 2: 
						print("All calls duration")
					case 3: 
						print("Recevived calls duration")
					case 4: 
						print("Dialled calls duration")
					case 5: 
						print("Clear timers")
					case 0: 
						print(prompt)
			case 6:
				showcostsp ="""\t\t\tShow call costs
				1 -> Last call cost
				2 -> All calls cost
				3 -> Clear counters
				0 -> Back"""
				print(showcostsp)
				showcost = int(input("Press number: "))
				match showcost:
					case 1:
						print("Last call cost")
					case 2:
						print("All calls cost")
					case 3:
						print("Clear counters")
					case 0:
						print(prompt)
			case 7:
				callcostp ="""\t\t\tcall cost settings
				1 -> Call cost limit
				2 -> Show costs in
				0 -> Back"""
				print(callcostp)
				callcost = int(input("Press number: "))
				match callcost:
					case 1:
						print("Call cost limit")
					case 2:
						print("Show costs in")
					case 0:
						print(prompt)
			case 8:
				print("Prepaid credit")
	case 5:
		tonesp = """\t\tTones
		1 -> Ringing tone
		2 -> Ringing volume
		3 -> Incoming call alert
		4 -> Composer
		5 -> Message alert tone
		6 -> Keypad tones
		7 -> Warning and games tones
		8 -> Viberating alert
		9 -> Screen saver
		0 -> Back"""
		print(tonesp)
		tones = int(input("Press number: "))
		match tones:
			case 1:
				print("Ringing tone")
			case 2:
				print("Ringing volume")
			case 3:
				print("Incoming call alert")	
			case 4:
				print("Composer")	
			case 5:
				print("Message alert tone")	
			case 6:
				print("Keypad tones")	
			case 7:
				print("Warning and games tones")	
			case 8:
				print("Viberating alert")	
			case 9:
				print("Screen saver")	
			case 0:
				print(prompt)
	case 6:
		settingsp = """\t\tSetings
		1 -> Call settings
		2 -> Phone settings
		3 -> Security settings
		4 -> Restore factory settings
		0 -> Back"""
		print(settingsp)
		settings = int(input("Press number: "))
		match settings:
			case 1:
				callsettingsp = """\t\tcallsettings
				1 -> Automatic redial
				2 -> Speed dialling
				3 -> Call waiting options
				4 -> Own number sending
				5 -> Phone line in use
				6 -> Automatic answer
				0 -> Back"""
				print(callsettingsp)
				callsettings = int(input("Press number: "))
				match settings:
					case 1:
						print("Automatic redial")
					case 2:
						print("Speed dialling")
					case 3:
						print("Call waiting options")	
					case 4:
						print("Own number sending")	
					case 5:
						print("Phone line in use")	
					case 6:
						print("Automatic answer")
					case 0:
						print(prompt)
			case 2:
				phonesettingsp = """\t\tphonesettings
				1 -> Language
				2 -> Cell info display
				3 -> Welcome note
				4 -> Network selection
				5 -> Lights
				6 -> Confirm sim service actions
				0 -> Back"""
				print(phonesettingsp)
				phonesettings = int(input("Press number: "))
				match phonesettings:
					case 1:
						print("Language")
					case 2:
						print("Cell info display")
					case 3:
						print("Welcome note")	
					case 4:
						print("Network selection")	
					case 5:
						print("Lights")	
					case 6:
						print("Confirm sim service actions")
					case 0:
						print(prompt)
			case 3:
				securitysettingsp = """\t\tsecuritysettings
				1 -> Pin code request
				2 -> Call barring service
				3 -> Fixed dialling
				4 -> Closed user group
				5 -> Phone security
				6 -> Change access codes
				0 -> Back"""
				print(securitysettingsp)
				securitysettings = int(input("Press number: "))
				match securitysettings:
					case 1:
						print("Pin code request")
					case 2:
						print("Call barring service")
					case 3:
						print("Fixed dialling")	
					case 4:
						print("Closed user group")	
					case 5:
						print("Phone security")	
					case 6:
						print("Change access codes")
					case 0:
						print(prompt)	
			case 4:
				print("Restore factory settings")
	case 7:
		print("Call divert")
	case 8:
		print("Games")
	case 9:
		print("Calculator")
	case 10:
		print("Reminders")
	case 11:
		clockp = """\t\tClock
		1 -> Alarm clock
		2 -> Clock settings
		3 -> Date settings
		4 -> Stopwatch
		5 -> Countdown timer
		6 -> Auto update of date and time
		0 -> Back"""
		print(clockp)
		clock = int(input("Press number: "))
		match clock:
			case 1:
				print("Alarm clock")
			case 2:
				print("Clock settings")
			case 3:
				print("Date settings")	
			case 4:
				print("Stopwatch")	
			case 5:
				print("Countdown timer")	
			case 6:
				print("Auto update of date and time")
			case 0:
				print(prompt)
	case 12:
		print("Profile")
	case 13:
		print("Sim services")