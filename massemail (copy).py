import smtplib
import re
from time import time_ns

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+");

startTime = time_ns();
emailCnt = 0;

# Email subject amd body
SUBJECT = ''

textFile = open("body.txt");

TEXT = textFile.read();

textFile.close()
# Gmail Sign In
# Credentials
gmail_sender = ''
gmail_passwd = ''

#Connect and login to Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

try:
    server.login(gmail_sender, gmail_passwd)
    print ('login success')
except:
    print ('login failed')
    exit()

#Read emails from txt file
file = open("emails.txt", 'r');
Lines = file.readlines();

for email in Lines:
    emailCnt += 1;
    if not EMAIL_REGEX.fullmatch(email):
        print ("IVE:", email.strip())
        continue

    TO = email.strip();
    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY.encode("utf8"))
        print ("OK!:", email.strip())
    except:
        print ("ERR:", email.strip())

server.quit()

endTime = time_ns();

ttc = endTime - startTime;

print(ttc / 1e9, "sec to finish");
print((ttc / 1e9) / emailCnt, "sec avg");
