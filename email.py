#email scheduler
import smtplib
s = smtplib.SMTP
s.starttls()
s.login("soundaryamurthy99@gmail.com","password")
message = "hlo"
s.sendmail("soundaryamurthy99@gmail.com", "soundaryamurthy99@gmail.com",message)
print("DONE")
s.quit()
