class library:
def__init__(self,book_name,author):
self.book_name=book_name
self.author=author
self.is_available=true

def check_out(self):
    if self.is_available:
    self.is_available=False
    print(f"'{self.book_name}'has been checked out.")
else:
    print(f"'{self.book_name})'is already checked out.")
    