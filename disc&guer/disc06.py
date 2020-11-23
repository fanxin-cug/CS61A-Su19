#OOP 1.2
class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg=msg
        self.sender_name=sender_name
        self.recipient_name=recipient_name

class Server:
    """Each Server has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        if email.recipient_name in self.clients:
            #self.clients[email.recipient_name].inbox.append(email)
            self.clients[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds it
        to the clients instance attribute.
        """
        self.clients[client_name]=client

class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server=server
        self.name=name
        self.server.register_client(self,self.name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        e=Email(msg,self.name,recipient_name)
        self.server.send(e)

    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox.append(email)

#2 Inheritance

class Pet():
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)

#2.1
"""
Below is a skeleton for the Cat class, which inherits from the Pet class. 
To complete the implementation, override the init and talk methods and add a new lose_life method.
Hint: You can call the init method of Pet to set a cat’s name and owner.
"""
class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self,name,owner)
        self.lives=lives

    def talk(self):
        """ Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name,"say meow!")

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False.
        """
        if self.lives>0:
            self.lives-=1
            if self.lives==0:
                self.is_alive=False
        else:
            self.is_alive=False

#2.2
"""
More cats! Fill in this implemention of a class called NoisyCat, which is just like a
normal Cat. However, NoisyCat talks a lot – twice as much as a regular Cat!
"""
class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""
    #def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        Cat.talk(self)
        Cat.talk(self)

# Nonlocal 3.2
"""
Write a function that takes in a number n and returns a one-argument function.
The returned function takes in a function that is used to update n. It should return
the updated n.
"""
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f(g):
        nonlocal n
        n=g(n)
        return n
    return f