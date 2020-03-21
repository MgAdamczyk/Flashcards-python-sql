from tech import v2Q


def addFlashcard(db):
    pl = input("Enter the Polish name: ")
    en = input("Enter according English name: ")
    ls = input("Which lesson do you want to assign a word to? ")
    cursor = db.cursor()
    query = "INSERT INTO flashcards (pol, eng, lesson) VALUES (" + v2Q(pl) + "," + v2Q(en) + "," + ls + ")"
    cursor.execute(query)
    db.commit()
    cursor.close()
    print("Added new flashcard into lesson number " + ls + "\n")


def removeCard(db):
    ls = input("Which lesson do you want to remove the flashcard from? ")
    word = input("Which word do you want to remove? ")
    cursor = db.cursor()
    query = "DELETE FROM flashcards WHERE lesson = " \
            + v2Q(ls) + " AND (pol = " + v2Q(word) + " OR eng = " + v2Q(word) + ")"
    cursor.execute(query)
    db.commit()
    cursor.close()
    print("Remove flashcard of " + word + " from lesson number " + ls + "\n")


def printAllCards(db):
    cursor = db.cursor()
    query = "SELECT pol, eng, lesson FROM flashcards ORDER BY lesson, pol"
    cursor.execute(query)
    for x in cursor:
        print("lesson: " + str(x[2]) + "\tpol: " + x[0] + "\teng: " + x[1])
    print("All displayed\n")
    db.commit()
    cursor.close()


def printLessonCards(db):
    ls = input("Enter lesson from which you want to print flashcards: ")
    cursor = db.cursor()
    query = "SELECT pol, eng FROM flashcards WHERE lesson = " + ls + " ORDER BY pol"
    cursor.execute(query)
    print("All flashcards from " + ls + " lesson: ")
    for x in cursor:
        print("pol: " + x[0] + "\teng: " + x[1])
    print("All displayed\n")
    db.commit()
    cursor.close()


def cardLearn(db, user):
    ls = input("Choose lesson to learn: ")
    cursor = db.cursor()
    query = "SELECT id_user FROM users WHERE name= " + v2Q(user)
    cursor.execute(query)
    id_user = str(cursor.fetchone()[0])
    query = "SELECT * FROM flashcards f LEFT JOIN progress p ON f.id_flashcard = p.id_flashcard " \
            "WHERE f.lesson = " + ls + " AND (p.id_user= " + id_user + " OR p.id_user IS NULL)" + \
            " UNION " \
            "SELECT * FROM flashcards f RIGHT JOIN progress p ON f.id_flashcard = p.id_flashcard " \
            "WHERE f.lesson = " + ls + " AND (p.id_user= " + id_user + " OR p.id_user IS NULL)"
    cursor.execute(query)

    toLearn = []
    for x in cursor:
        toLearn.append(x)
        if not x[7]:
            cursor2 = db.cursor()
            query = "INSERT INTO progress (id_user, id_flashcard, know) " \
                    "VALUES (" + id_user + "," + str(x[0]) + ", False)"
            cursor2.execute(query)
            cursor2.close()
            db.commit()

    while len(toLearn) > 0:
        toAdd = []
        for x in toLearn:
            print("pol: " + x[1] + "\teng: ?")
            y = input("Do you know this word in English (y/n)? ")
            if y == "y":
                query = "UPDATE progress SET know = True WHERE id_user=" + id_user
            else:
                query = "UPDATE progress SET know = False WHERE id_user=" + id_user
                toAdd.append(x)
            cursor.execute(query)
            db.commit()
            print("pol: " + x[1] + "\teng: " + x[2])
        toLearn.clear()
        for x in toAdd:
            toLearn.append(x)
    print("Congratulations! You have learnt all words in the lesson :)\n")
    cursor.close()
