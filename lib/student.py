class Student:
    def __init__(self):
        pass

    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")

class ChattyStudent(Student):
    def __init__(self):
        # Call the parent constructor.
        super().__init__()
    def hello(self):
        
        # Extend the greeting with a chatty follow-up.
        print("Hey there! I'm so excited to learn stuff.")
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        # Override raise_hand to print "Pick me!" ten times.
        for _ in range(10):
            print("Pick me!")
