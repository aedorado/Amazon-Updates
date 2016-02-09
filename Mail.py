import smtplib
import os

# os.getenv(PORT, 8080)
# os.getenv(IP, '0.0.0.0')
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("@gmail.com", "")

msg = "This is awesome baby!"
server.sendmail("@gmail.com", "a@a", msg)
    
server.quit()

# server.login("YOUR EMAIL ADDRESS", "YOUR PASSWORD")
# server.sendmail("YOUR EMAIL ADDRESS", "THE EMAIL ADDRESS TO SEND TO", msg)