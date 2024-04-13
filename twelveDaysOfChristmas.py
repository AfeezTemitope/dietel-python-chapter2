
    days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

    day = int(input("Enter the day of Christmas you want to see (1-12):\n")) - 1

    if 0 <= day < len(days):
        print(f"On the {days[day]} day of Christmas,")
        print("My true love sent to me:")

        gifts = [
            "A partridge in a pear tree.",
            "Two turtle doves, and",
            "Three French hens,",
            "Four calling birds,",
            "Five golden rings,",
            "Six geese a-laying,",
            "Seven swans a-swimming,",
            "Eight maids a-milking,",
            "Nine ladies dancing,",
            "Ten lords a-leaping,",
            "Eleven pipers piping,",
            "Twelve drummers drumming,"
        ]

        for i in range(day, -1, -1):
            print(gifts[i])
    else:
        print("Invalid day. Please enter a number between 1 and 12.")

