class Message:
    def __init__(self):
        self.message = ""
        self.name = ""

    def writemessage(self):
        self.message = input("Please input a message: ")
        self.name = input("Please input your name: ")
        with open("servermessages.txt", "a") as f:
            f.write("Message from: " + self.name + " Message contents: " + self.message + '\n')

    def viewmessage(self):
        with open("servermessages.txt", "r") as f:
            messages = f.readlines()
            for lines in messages:
                lines = lines.strip('\n')
            print(messages)

    def send(self):
        print("Message sent")


class Email(Message):
    def __init__(self):
        super(Email, self).__init__()

    def sending_email(self):
        print("Sending email message...")
        Message.send()


class TextMessage(Message):
    def __init__(self):
        super(TextMessage, self).__init__()

    def writemessage(self):
        self.message = input("Please input a message: ")
        self.name = input("Please input your name: ")
        length = len(self.message)
        if length > 144:
            self.message = self.message[0:144]
            print("File was too large, only first 144 characters were sent.")
        with open("servermessages.txt", "a") as f:
            f.write("Message from: " + self.name + " Message contents: " + self.message + '\n')

    def sending_text(self):
        print('Sending text message...')
        Message.send()


class Letter(Message):
    def __init__(self):
        super(Letter, self).__init__()

    def sending_letter(self):
        print("Sending letter message")
        Message.send()



message1 = Message()
message1.writemessage()
message1.viewmessage()