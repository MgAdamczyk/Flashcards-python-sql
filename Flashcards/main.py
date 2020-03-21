from database import dbConnection
from user import *
from flashcard import *

print("Connecting to the the database...\n")
db = dbConnection()

end = False
while not end:
    print("Menu")
    print("0 - Quit")
    print("1 - Log in")
    print("2 - Register")
    x = input("Choose one option: ")
    if x == "0":
        print("Exit")
        break
    elif x == "1":
        logged, user = logIn(db)
        if logged:
            while logged:
                print("Menu")
                print("1 - Log out")
                print("2 - Display all flashcards")
                print("3 - Display all flashcards from chosen lesson")
                print("4 - Learn")
                print("5 - Add new flashcard")
                print("6 - Remove flashcard")
                print("7 - Your profile")
                y = input("What do you want to do?")

                if y == "1":
                    logged = False
                elif y == "2":
                    printAllCards(db)
                elif y == "3":
                    printLessonCards(db)
                elif y == "4":
                    cardLearn(db, user)
                elif y == "5":
                    addFlashcard(db)
                elif y == "6":
                    removeCard(db)
                elif y == "7":
                    while True:
                        print("Your profile")
                        print("1 - Change your password")
                        print("2 - Delete your account")
                        print("3 - Back")
                        z = input("Choose one option: ")
                        if z == "1":
                            changePasswd(db, user)
                        elif z == "2":
                            if deleteUser(db, user):
                                logged = False
                                break
                        elif z == "3":
                            break
                        else:
                            print("Invalid value entered, try again")
                else:
                    print("Invalid value entered, try again")
    elif x == "2":
        newUser(db)
    else:
        print("Invalid value entered, try again")
