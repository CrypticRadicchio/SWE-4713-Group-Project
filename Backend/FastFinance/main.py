import FFEmail

flag = True
while flag:
    choice = input("Are you sending to one person? Y/N: ")
    recipient = []
    if choice.lower() != "y":
        mult_flag = True
        while mult_flag:
            response = input("Enter the email of the next recipient (enter STOP when you are done): ")
            if response == "STOP":
                mult_flag = False
            recipient.append(response)
        recipient.pop()  # jank way of removing "STOP" from the end of the list
    else:
        recipient.append(input("Enter the email of your recipient: "))
    subject = input("Enter the email subject: ")
    body = input("Enter the email body: ")
    print(FFEmail.send_email(recipient, subject, body))

    choice = input("Send another email? Y/N: ")
    if choice != "Y":
        print("Goodbye!")
        flag = False
