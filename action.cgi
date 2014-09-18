#!/usr/bin/python
import os
import cgi, cgitb 
import sys

SENDMAIL = "/usr/sbin/sendmail" # sendmail location

form = cgi.FieldStorage() 

#check for anti-spam values
# redirect AJAX response message back to alertify that anti-spam does not match
# not good enough to do it only via client side JS (in case they turn it off).

if form.getvalue('email') is not None:
	FROM = form.getvalue('email')
else:
	FROM = "no-reply@samueljrains.com"
TO = ["jack@samueljrains.com"]

SUBJECT = "A message from your site!"
NAME = form.getvalue('name')
TEXT = form.getvalue('message')

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

Name: %s
Message: %s
""" % (FROM, ", ".join(TO), SUBJECT, NAME, TEXT)

print message
# Send the mail
p = os.popen("%s -t -i" % SENDMAIL, "w")
p.write(message)
p.close()
sys.exit()