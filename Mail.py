import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("ism2013018@iiita.ac.in", "")
 
msg = "YOUR MESSAGE!"
server.sendmail("ism2013018@iiita.ac.in", "ism2013018@iiita.ac.in", msg)
server.quit()

# server.login("YOUR EMAIL ADDRESS", "YOUR PASSWORD")
# server.sendmail("YOUR EMAIL ADDRESS", "THE EMAIL ADDRESS TO SEND TO", msg)