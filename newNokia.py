while True:
    print("\n")
    print("\n******************")
    print(":WELCOME NEW USER:")
    print("******************")
    print("ABIDO-SHAKERS NOKIA PHONE MENU")

    print(" 1. PHONEBOOK\t2. MESSAGES\t3. CHAT\t4. CALL REGISTER\n5. TONES\t6. SETTINGS\t7. CALL DIVERTS\t8. GAMES\t9.CALCULATOR\n10. REMINDERS\t11.CLOCK\t12.PROFILES\t13.SIM SERVICES\t14. EXIT  ")
    option = int(input("Enter an option: "))

    if option == 14:
        print("Exiting the menu.")
        break

    match option:
        case 1:
            print("1. Search\n 2. Service Nos.'\n 3. Add name\n 4. Erase\n 5. Edit\n 6. Assign tone\n 7. Send b'card\n 8. Options\n 9. Speed dials\n 10. Voice tags\n")
            print()
            sub_option = int(input("Enter your sub-Option: "))
            print()
            
            match sub_option:
                case 1:
                    print("Searching...")
                case 2:
                    print("Service Nos.'...")
                case 3:
                    print("Adding name...")
                case 4:
                    print("Erasing...")
                case 5:
                    print("Editing...")
                case 6:
                    print("Assigning Tone...")
                case 7:
                    print("Sending b'card...")
                case 8:
                    print("Available options...")
                    print(" a. type of view")
                    print(" b. memory status")
                case 9:
                    print("Speed dialing...")
                case 10:
                    print("Opening Voice tags...")
                case _:
                    print("Choose again or getat!!")

        case 2:
            print("1. Write messages\n 2. Inbox\n 3. Outbox\n 4. Picture messages\n 5. Templates\n 6. Smileys\n 7. Message settings\n 8. Info service\n 9. Voice Mailbox Number\n 10. Service command Editor")
            sub_choice = int(input("Enter your sub-choice: "))
            print()
            
            match sub_choice:
                case 1:
                    print("Writing messages...")
                case 2:
                    print("Viewing inbox...")
                case 3:
                    print("Viewing outbox...")
                case 4:
                    print("Viewing picture messages...")
                case 5:
                    print("Viewing templates...")
                case 6:
                    print("Viewing smileys...")
                case 7:
                    print("Message Settings Menu:")
                    print("a. SET")
                    print("   i. Message Centre Number")
                    print("   ii. Message Sent As")
                    print("   iii. Message Validity")
                    print("b. Common")
                    print("   i. Delivery Reports")
                    print("   ii. Reply via Same Centre")
                    print("   iii. Character Support")
                case 8:
                    print("Accessing info service...")
                case 9:
                    print("Setting voice mailbox number...")
                case 10:
                    print("Editing service commands...")
                case _:
                    print("abg exit!!!.")
                    
        case 3:
            print("CHAT")
            chatzone = int(input("input your chatzone: "))
            
            match chatzone:
                case 1:
                    print("let's chat...")
                case _:
                    print("abg commot!!!")
                    
        case 4:
            print("1. missed calls\n 2. recieved calls\n 3. dialled numbers\n 4. erase recent calls lists\n 5. show calls duration\n a. last call duration\n b. all calls duration\n c.recieved calls duration\n 6. Dialled calls' duration\n 7. call timers\n 8. Show call costs\n a. a. Last call cost\n b. all call cost  c.  Clear counters\n 9. 9. Call cost settings\n a.Call cost limit\n b. Show costs in\n 10. Prepaid credit\n")
            call_register = int(input("enter your callRegister: "))
            
            match call_register:
                case 1:
                    print("1. missed calls...")
                case 2:
                    print("2. recieved...")
                case 3:
                    print("3. dialled...")
                case 4:
                    print("4. erasing...")
                case 5:
                    print("5. call durations...")
                    print(" a. last call\n b. all calls duration\n c.recieved calls duration\n")
                case 6:
                    print("6.dailled calls duration...")
                case 7:
                    print("call timers...")
                case 8:
                    print("8. Showing call costs......")
                    print("a. Last call cost...\n b. all call cost...\n  c.  Clearing counters...\n ")
                case 9:
                    print("Call cost settings...")
                    print("a. call cost limit...\n b. showing call cost\n")
                case 10:
                    print("1.prepaid credit...")
                case _:
                    print("wetin u dey find wey no lost")

        case 5:
            print("1. Ringing tone\n 2. Ringing volume\n 3. Incoming call alert\n 4. Composer\n 5. Message alert tone\n 6. Keypad tones\n 7. Warning and game tones\n 8. Vibrating alert\n 9. Screen saver\n")
            
        case 6:
            print("1. Call settings\n 2. Phone settings\n 3. Security settings\n 4. Restore factory")
            settings = int(input("enter your settings: "))
            
            match settings:
                case 1:
                    print("1. call settings....")
                    print(" 1. Automatic redial\n 2. Speed dialling\n 3. Call waiting options\n 4. Own number sending\n 5. Phone line in use\n 6. Automatic answer")
                case 2:
                    print("2. phone settings...")
                    print("1. Language\n 2. Cell info display\n 3. Welcome note\n 4. Network selection\n 5. Lights\n 6. Confirm SIM service actions")
                case 3:
                    print("security settings...")
                    print("1. PIN code request\n 2. Call barring service\n 3. Fixed dialling\n 4. Closed user group\n 5. Phone security\n 6. Change access codes")
                case 4:
                    print("Restoring factory settings..........")
                case _:
                    print("wetin again!!!")
                    
        case 7:
            print("call diverted........")
            print("**********************")
            
        case 8:
            print("games loading........")
            print("**********************")
            
        case 9:
            print("loading Calculator........")
            print("**********************")
            
        case 10:
            print("Setting up reminders........")
            print("**********************")

        case 11:
            print("Clock settings........")
            print("**********************")
            clock_settings = int(input("enter your clockSettings: "))
            
            match clock_settings:
                case 1:
                    print("Clock setup")
                    print("1. Alarm clock\n 2. Clock settings\n 3. Date setting\n 4. Stopwatch\n 5. Countdown timer\n 6. Auto update of date and time")
                    
        case 12:
            print("Creating profiles........")
            print("**********************")
            
        case 13:
            print("loading sim services........")
            print("**********************")
            
        case 14:
            print("Exiting... thank you for using the abidoShaker phone menu")




