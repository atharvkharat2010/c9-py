class library:
    def __init__(self,list,name):
        self.bookslist=list
        self.name=name
        self.lendict={}
    def displaybooks(self):
        print(f"we have following books in our library")
        for book in self.bookslist:
            print(book)
    def lendbook(self,user,book):
        if book not in self.lendict.keys():
            self.lendict.update({book:user})
            print("lender-book data base has been updated.you can take tha book")
        else:
            print(f"book is alresdy being used by{self.lendict[book]}")
    def addbook(self,book):
        self.bookslist.append(book)
        print("book has been added to the book list")
    def returnbook(self,book):
        self.lendict.pop(book)
if __name__ =='__main__':
    book=library(['python','c++','c#','c','java','javascript','html','php','css'],"codewithharry library")
    while(True):
        print(f"welcome to the {book.name} library.enter your choice to continue")
        print("1. display books")
        print("2. lend books")
        print("3. add books")
        print("4. return books")
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("please choose a valid option")
            continue
        else:
            user_choice=int(user_choice)
        if user_choice==1:
            book.displaybooks()
        elif user_choice==2:
            book.lendbook(input("enter you name"),input("enter the name of book"))
        elif user_choice==3:
            book.addbook(input("enter the name of book you want to add"))
        elif user_choice==4:
            book.returnbook(input("enter the name of the book you want to return"))
        else:
            print("not a valid option")
        print("press q to quit and c to continue")
        user_choice2=""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2=input()
            if user_choice2=="q":
                exit()
            elif user_choice2=="c":
                continue