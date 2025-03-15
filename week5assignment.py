#create a class book
class Book():
    def __init__(self, title, author, description, publication_date, isbn, copies_available, checked_out_by):
        self.title = title
        self.author = author
        self.description = description
        self.publication_date = publication_date
        self.isbn = isbn
        self.copies_available = copies_available
        self.checkout_out_by = []

    def checkout(self, name):
        self.checkout_out_by.append(name)
        self.copies_available -= 1
    
    def checkin(self, name):
        self.checkout_out_by.remove(name)
        self.copies_available += 1

    def add_books(self, copies):
        self.copies_available += copies

    def remove_books(self, copies):
        self.copies_available -= copies


class IslamicBooks(Book): #Inherit class Book
    pass


#create an object of the class Books

quran = Book('Quran', 'Hafs', "Huda Duniya", "575 A.D", 11111111, 700000, [])

#calling the method of the class Book
quran.checkout("Abdusalaam")

#create an object of the derived class islamicbooks
hadith = IslamicBooks('sahih',"bukhari","kitabu hadith", "899 A.D", 378474837384, 6000, [])

#calling the method of the class islamicbooks
hadith.checkout("fadlullah")
hadith.checkout("Rayhaan")
hadith.checkin("fadlullah")


#printing to console
print(hadith.copies_available)
print(hadith.checkout_out_by)
print(quran.checkout_out_by)

#Polymorphism using a car class and plane class with different method
class Car():
    def move(self):
        return "brooouuuummmm brooomm" 
    

class Plane():
    def move(self):
        return "fffff flying ing ing ing"
    
for mv in [Car(), Plane()]:
    print(mv.move())
    
