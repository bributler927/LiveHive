import secrets
import smtplib


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
        print("You have entered the incorrect verification code too many times. Please email LiveHive customer "
              "support at Livehive@gmail.com to verify your account")
    return isVerified


