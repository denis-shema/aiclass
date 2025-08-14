# class library:
    def __init__(self,books):
         self.books=books    
     def borrow_books(self,title):
         for i in self.books:
             if title.lower() == i.lower():
                 return "available"
                 break
             else:
                 return "not available"
 books=["biology","physics","chemistry","agriculture","maths","english"]
 documents=library(books)
 print(documents.borrow_books("chemistry")) 