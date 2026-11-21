class Notification:
    def send(self):
        print("Sending a generic notification")
class EmailNotification:
    def send(self):
        print("Sending a gener notification")
class SMSNotification(Notification):
     def send(self):
        print("Sending SMS Notification")
        Notification = [Notification(),EmailNotification(),SMSNotification()]
     for n in Notification:
         n.send()
         