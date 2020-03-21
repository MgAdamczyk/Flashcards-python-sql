from tech import v2Q


def newUser(db):
    n = input("Provide your name: ")
    p = input("Provide your password: ")
    addUser(db, n, p)
    print("Added successfully")


def addUser(db, name, passwd):
    cursor = db.cursor()
    query = "INSERT INTO users (name, password) VALUES (" + v2Q(name) + "," + v2Q(passwd) + ")"
    cursor.execute(query)
    db.commit()
    cursor.close()


def logIn(db):
    n = input("Enter your name: ")
    p = input("Enter your password: ")
    cursor = db.cursor()
    query = "SELECT count(*) FROM users WHERE name=" + v2Q(n) + " AND password=" + v2Q(p)
    cursor.execute(query)
    val = cursor.fetchone()[0]
    if val == 0:
        print("Login failed. Invalid username or password")
        return False, ""
    elif val == 1:
        print("Signed corectly")
        return True, n


def changePasswd(db, user):
    x = input("Enter old password: ")
    y = input("Enter new password: ")
    cursor = db.cursor()
    query = "UPDATE users SET password = " + v2Q(y) + " WHERE password = " + v2Q(x) + " AND name = " + v2Q(user)
    cursor.execute(query)
    db.commit()
    cursor.close()
    print("Password updated\n")


def deleteUser(db, user):
    x = input("Are you sure you want to delete your account with all your data (y/n) ? ")
    if x == "y":
        cursor = db.cursor()
        query = "SELECT id_user FROM users WHERE name= " + v2Q(user)
        cursor.execute(query)
        id_user = str(cursor.fetchone()[0])
        query = "DELETE FROM users WHERE id_user = " + id_user
        cursor.execute(query)
        query = "DELETE FROM progress WHERE id_user = " + id_user
        cursor.execute(query)
        db.commit()
        cursor.close()
        print("Your account was deleted successfully\n")
        return True
    else:
        return False
