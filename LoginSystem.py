import secrets
import smtplib
import getpass
import hashlib
import string
from validate_email import validate_email

hashedUserPassDict = {}
usernameToEmailDict = {}
emailToUsernameDict = {}
emailIsVerifiedDict = {}
customerSupportEmail = ""   # fill in
noResponseVerificationEmail = ""    # fill in
setLowers = set(string.ascii_lowercase)
setUppers = set(string.ascii_uppercase)
setDigits = {i for i in range(10)}
setGoodSymbols = {chr(i) for i in range(33, 47)} + {chr(i) for i in range(58, 63)}
setPasswordPermitted = setLowers | setUppers | setDigits | setGoodSymbols
setUsernamePermitted = setLowers | setUppers | setDigits


usernameRules = ("Usernames must be between 3 and 30 characters. "
                 "Usernames may only include letters and numbers.")
passwordRules = ("Password must be between 12 and 30 characters."
                 "Password must contain at least one uppercase letter."
                 "Password must contain at least one lowercase letter."
                 "Password must contain at least one number."
                 "Password must contain at least one of the following symbols: " + repr(setGoodSymbols) +
                 "Password may only contain uppercase letters, lowercase letters, numbers, "
                 "or one of the above symbols.")

"""
This is the "driver" in order to create an account and verify your email address.
This function pulls together the necessary helper functions. 
"""
def makeAccount():
    print("Welcome to LiveHive. Please enter the username you would like.")
    print(usernameRules)
    username = createUsername()

    print("Please enter the password you would like.")
    password = createPassword()

    hashedUsername = hashThis(username)
    hashedPassword = hashThis(password)
    hashedUserPassDict[hashedUsername] = hashedPassword

    print("Please enter the email address you would like.")
    email = getEmail()
    usernameToEmailDict[username] = email
    emailToUsernameDict[email] = username
    result = sendEmailAndVerify()
    if result:
        emailIsVerifiedDict[email] = True
    else:
        emailIsVerifiedDict[email] = False
    return

"""
This is the "driver" in order to get the user's email address.
This function pulls together the necessary helper functions. 
"""
def getEmail():
    for i in range(1000):
        email = input("Email: ")
        if emailValidator(email):
            if emailPresent(email):
                print("This email is already being used for another account. Please login to that account.")
            else:
                return email
        print("That is not a valid email. If you believe you have entered a valid email, "
              "please enter it again and if "
              "it still does not work then contact customer support at {0} "
              "Please enter a valid email.".format(customerSupportEmail))
    print("You have failed to enter a valid email too many times")
    contactSupport()
    quitScreen()
    return

"""
This function checks if the email in the parameter is already associated with an account,
returning true if it is and false if it is not. 
"""
def emailPresent(email):
    return email in emailToUsernameDict

"""
This function checks if the email in the parameter is a valid email address, returning 
true if it is and false if it is not. 
"""
def emailValidator(email):
    return validate_email(email, True, True, customerSupportEmail, smtp.gmail.com, 10, 10, True, False)

"""
This is the "driver" in order to create a password for an account.
This function pulls together the necessary helper functions. 
"""
def createPassword():
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

"""
This is called whenever the app should quit and go to the home page 
"""
def quitScreen():
    # go to home screen
    return

"""
This function checks if the password in the parameter follows the rules for permissible passwords.
The rules are explained in the String passwordRules
"""
def checkPasswordRules(password):
    chars = set(password)
    return (not (chars.isdisjoint(setLowers) or chars.isdisjoint(setUppers) or chars.isdisjoint(
        setDigits) or chars.isdisjoint(setGoodSymbols))) and (chars.issubset(setPasswordPermitted))

"""
This is the "driver" in order to create a username for a new account.
This function pulls together the necessary helper functions. 
"""
def createUsername():
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

"""
This function checks if the username in the parameter follows the rules for permissible usernames.
The rules are explained in the String usernameRules
"""
def checkUsernameRules(username):
    return (3 <= len(username) <= 30) and set(username).issubset(setUsernamePermitted)

"""
This function checks if the username in the argument is taken by another account
"""
def checkIfUsernameTaken(username):
    userH = hashThis(username)
    if userH in hashedUserPassDict:
        return true
    return false

"""
This function hashes whatever is in its parameter using a SHA-512 hash function for secure encryption
"""
def hashThis(str):
    hasher = hashlib()
    ret = hasher.sha3_512(str)
    return ret

"""
This function relays a message to the user that they should contact customer support
"""
def contactSupport():
    print("Please contact customer support at {0}".format(customerSupportEmail))
    return

"""
This function sends an email with a verification/authentication code for the user to input
"""
def sendEmailAndVerify(userEmail):
    authenticationCode = secrets.randbelow(
        1000000)  # secrets is a more secure random number generator than that of random
    port = 0  # insert port number from LiveHive email here
    emailUsername = noResponseVerificationEmail  # insert LiveHive email here
    emailPassword = " "  # insert LiveHive email password here
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

"""
This function gets the login information from the user 
"""
def askLogin():
    user = input("Username: ")
    password = getpass.getpass()
    return (user, password)

"""
This function verifies that the username and password entered is associated with a valid LiveHive account 
"""
def verifyLogin(username, password):
    usernameHashed = hashThis(username)  # hash username
    passwordHashed = hashThis(password)  # hash password
    return usernameHashed in hashedUserPassDict and hashedUserPassDict[usernameHashed] == passwordHashed

"""
This is the "driver" in order for the user to login.
This function pulls together the necessary helper functions. 
"""
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
