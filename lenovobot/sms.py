import smtplib

def send(message):
    carriers = {
        'att': '@mms.att.net',
        'tmobile': ' @tmomail.net',
        'verizon': '@vtext.com',
        'sprint': '@page.nextel.com'
    }

    # Replace the number with your own, or consider using an argument\dict for multiple people.
    usersettings = open("user.txt", "r")
    data = usersettings.readlines()
    to_number = data[0] + carriers[data[1].replace('\n', '')]
    auth = ('autonoreply10@gmail.com', 'popguy21')

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
    # Send text message through SMS gateway of destination number
    server.sendmail(auth[0], to_number, message)
    server.quit()