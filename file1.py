import secrets
import smtplib
import getpass
import hashlib
import string

hashedUserPassDict = {}
customerSupportEmail = ""  # fill in
goodSymbolsL = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|",
                ";", ":", "."]
goodSymbolsStr = "".join(goodSymbolsL)
setLowers = set(string.ascii_lowercase)
setUppers = set(string.ascii_uppercase)
setDigits = {i for i in range(10)}
setGoodSymbols = set(goodSymbolsL)


def makeAccount():
    print("Welcome to LiveHive.")

    print("Please enter the username you would like.")
    usernameRules = "Usernames must be between 3 and 30 characters."  # allows me to more easily change userName rules
    print(usernameRules)
    username = createUsername(usernameRules)

    print("Please enter the password you would like.")
    passwordRules = ("Password must be between 12 and 30 characters\n"
                     "Password must contain at least one uppercase letter\n"
                     "Password must contain at least one lowercase letter\n"
                     "Password must contain at least one number\n"
                     "Password must contain at least one of the following symbols: " + goodSymbolsStr)
    password = createPassword(passwordRules)

    hashedUsername = hashThis(username)
    hashedPassword = hashThis(password)
    hashedUserPassDict[hashedUsername] = hashedPassword
    return


def createPassword(passwordRules):
    for i in range(1000):
        password = getpass.getpass()
        fitsRules = checkPasswordRules(password)  # allows me to more easily change rules for password check
        if not fitsRules:
            print("Password does not follow Password rules.")
            print("As a reminder:")
            print(passwordRules)
        else:
            return password
    print("You have failed to enter a valid password too many times")
    contactSupport()
    quitScreen()
    return

def quitScreen():
    # go to home screen
    return



def checkPasswordRules(password):
    chars = set(password)
    return not (chars.isdisjoint(setLowers) or chars.isdisjoint(setUppers) or chars.isdisjoint(
        setDigits) or chars.isdisjoint(setGoodSymbols))


def createUsername(usernameRules):
    for i in range(1000):
        username = input("Username: ")
        fitsRules = checkUsernameRules(username)  # allows me to more easily change rules for username check
        if not fitsRules:
            print("Username does not follow Username rules.")
            print("As a reminder:")
            print(usernameRules)
        else:
            taken = checkIfUsernameTaken(username)
            if taken:
                print("This username is taken. Please try a new username.")
            else:
                return username
    print("You have failed to enter a valid username too many times")
    contactSupport()
    quitScreen()
    return


def checkIfUsernameTaken(username):
    userH = hashThis(username)
    if userH in hashedUserPassDict:
        return true
    return false


def checkIfPasswordTaken(password):
    passH = hashThis(password)
    if passH in hashedUserPassDict.values():
        return true
    return false


def hashThis(username):
    hasher = hashlib
    ret = hasher.sha3_512(username)
    return ret


def contactSupport():
    print("Please contact customer support at {0}".format(customerSupportEmail))
    return


def checkUsernameRules(username):
    return 3 <= len(username) <= 30


# This function sends an email with a verification/authentication code for the user to input
def sendEmailAndVerify():
    authenticationCode = secrets.randbelow(
        1000000)  # secrets is a more secure random number generator than that of random
    port = 0  # insert port number from LiveHive email here
    emailUsername = " "  # insert LiveHive email here
    emailPassword = " "  # insert LiveHive email password here
    userEmail = input("Enter your email")  # insert email from user here
    emailMessage = " "  # insert email to send to the user here (must include authenticationCode)
    server1 = smtplib.SMTP_SSL('smtp.gmail.com', port)
    server1.login(emailUsername, emailPassword)
    server1.sendmail(emailUsername, userEmail, emailMessage)
    server1.quit()
    userNumber = input("Enter the verification code you received")
    isVerified = false
    for i in range(5):
        if userNumber == authenticationCode:
            isVerified = true
            print("Thank you for verifying your email. Welcome to LiveHive!")
            break
        else:
            userNumber = input("That was the wrong code. Please try again.")
    if not isVerified:
        print("You have entered the incorrect verification code too many times.")
        print("Please email LiveHive customer support at {0} to verify your account".format(customerSupportEmail))
    return isVerified


def askLogin():
    user = input("Username: ")
    password = getpass.getpass()
    return (user, password)


def verifyLogin(username, password):
    username = username  # hash username
    password = password  # hash password
    return username in hashedUserPassDict and hashedUserPassDict[username] == password


def runLogin():
    success = false
    count = 0
    while not success and count <= 5:
        enteredUsername, enteredPassword = askLogin()
        if verifyLogin(enteredUsername, enteredPassword):
            success = true
        else:
            print("Username or password is incorrect. Please try again")
        count += 1
    if success:
        print("Login successful. Welcome to LiveHive!")
    else:
        print("Too many failed login attempts.")
        contactSupport()
    return success
