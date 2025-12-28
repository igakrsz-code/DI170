class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        record = f"{self.phone_number} called {other_phone.phone_number}"
        print(record)
        self.call_history.append(record)

    def show_call_history(self):
        for call in self.call_history:
            print(call)

    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append(message)

    def show_outgoing_messages(self):
        for message in self.messages:
            if message["from"] == self.phone_number:
                print(message)

    def show_incoming_messages(self):
        for message in self.messages:
            if message["to"] == self.phone_number:
                print(message)

    def show_messages_from(self, phone_number):
        for message in self.messages:
            if message["from"] == phone_number:
                print(message)
