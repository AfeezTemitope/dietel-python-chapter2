while True:
    print("\n")
    print("\n******************")
    print(":WELCOME NEW USER:")
    print("******************")
    print("ABIDO-SHAKERS NOKIA PHONE MENU")

    print(" 1. PHONEBOOK\n 2. MESSAGES\n 3. CHAT\n 4. CALL REGISTER\n 5. TONES\n 6. SETTINGS\n 7. CALL DIVERTS\n 8. GAMES\n 9.CALCULATOR\n 10. REMINDERS\n 11.CLOCK\n 12.PROFILES\n 13.SIM SERVICES\n 14. EXIT  ")
    option = int(input("Enter an option: "))

    if option == 14:
        print("Exiting the menu.")
        break


    if option == 1:
        print("1. Search\n 2. Service Nos.'\n 3. Add name\n 4. Erase\n 5. Edit\n 6. Assign tone\n 7. Send b'card\n 8. Options\n 9. Speed dials\n 10. Voice tags\n")
        print()
        sub_option = int(input("Enter your sub-Option: "))
        print()
        
        if sub_option == 1:
            print("Searching...")
        elif sub_option == 2:
            print("Service Nos.'...")
        elif sub_option == 3:
            print("Adding name...")
        elif sub_option == 4:
            print("Erasing...")
        elif sub_option == 5:
            print("Editing...")
        elif sub_option == 6:
            print("Assigning Tone...")
        elif sub_option == 7:
            print("Sending b'card...")
        elif sub_option == 8:
            print("Available options...")
            print(" a. type of view")
            print(" b. memory status")
        elif sub_option == 9:
            print("Speed dialing...")
        elif sub_option == 10:
            print("Opening Voice tags...")
        else:
            print("Choose again or getat!!")

    elif option == 2:
        print("1. Write messages\n 2. Inbox\n 3. Outbox\n 4. Picture messages\n 5. Templates\n 6. Smileys\n 7. Message settings\n 8. Info service\n 9. Voice Mailbox Number\n 10. Service command Editor")
        print()
        sub_choice = int(input("Enter your sub-choice: "))
        print()
        
        if sub_choice == 1:
            print("Writing messages...")
        elif sub_choice == 2:
            print("Viewing inbox...")
        elif sub_choice == 3:
            print("Viewing outbox...")
        elif sub_choice == 4:
            print("Viewing picture messages...")
        elif sub_choice == 5:
            print("Viewing templates...")
        elif sub_choice == 6:
            print("Viewing smileys...")
        elif sub_choice == 7:
            print("Message Settings Menu:")
            print("a. SET")
            print("   i. Message Centre Number")
            print("   ii. Message Sent As")
            print("   iii. Message Validity")
            print("b. Common")
            print("   i. Delivery Reports")
            print("   ii. Reply via Same Centre")
            print("   iii. Character Support")
        elif sub_choice == 8:
            print("Accessing info service...")
        elif sub_choice == 9:
            print("Setting voice mailbox number...")
        elif sub_choice == 10:
            print("Editing service commands...")
        else:
            print("abg exit!!!.")

    elif option == 3:
        print("CHAT")
        chatzone = int(input("Input your chatzone: "))
        if chatzone == 1:
            print("Let's chat...")
        else:
            print("Abeg commot!!!")

    elif option == 4:
        print("1. Missed calls\n 2. Received calls\n 3. Dialed numbers\n 4. Erase recent calls lists\n 5. Show calls duration\n a. Last call duration\n b. All calls duration\n c. Received calls duration\n 6. Dialed calls' duration\n 7. Call timers\n 8. Show call costs\n a. Last call cost\n b. All call cost\n c. Clear counters\n 9. Call cost settings\n a. Call cost limit\n b. Show costs in\n 10. Prepaid credit")
        print()
        call_register = int(input("Enter your callRegister: "))
        print()
        if call_register == 1:
            print("Missed calls...")
        elif call_register == 2:
            print("Received calls...")
        elif call_register == 3:
            print("Dialed numbers...")
        elif call_register == 4:
            print("Erasing recent calls lists...")
        elif call_register == 5:
            print("Showing call durations...")
            print(" a. Last call")
            print(" b. All calls duration")
            print(" c. Received calls duration")
        elif call_register == 6:
            print("Dialed calls' duration...")
        elif call_register == 7:
            print("Call timers...")
        elif call_register == 8:
            print("Showing call costs...")
            print(" a. Last call cost")
            print(" b. All call cost")
            print(" c. Clearing counters")
        elif call_register == 9:
            print("Call cost settings...")
            print(" a. Call cost limit")
            print(" b. Showing call cost")
        elif call_register == 10:
            print("Prepaid credit...")
        else:
            print("Wetin u dey find wey no lost")





