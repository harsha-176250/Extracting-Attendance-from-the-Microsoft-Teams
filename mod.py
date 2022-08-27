import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

def transfer(date):
    
    fpp=open(date+".txt","w")
    with open ("num.csv","r") as roll:
        fp=open("attendance_"+ date+".txt","r")
        data=list()
        for k in fp:
            e=k.split()
            k=" ".join(e)
            data.append(k.rstrip())
        a=data.pop()
        b=data.pop()
        c=data.pop()
        fdata=list()
        for j in roll:
            i=j.rstrip()
            i=i.split(",")
            if i[1] in data:
                fdata.append(i[0])
        fdata.sort()
        print(fdata)
        for k in fdata:
            
            fpp.write(k+"\n")
            

  
    fpp.write(c+ "\n"+b+ "\n"+a+ "\n")
    fpp.close()
    print("sucess transfer")

def gmail(toaddr,date,filename):
    # libraries to be imported 

    fromaddr = "masthanaiah.191cs115@nitk.edu.in"


# instance of MIMEMultipart 
    msg = MIMEMultipart() 

# storing the senders email address 
    msg['From'] = fromaddr 

# storing the receivers email address 
    msg['To'] = toaddr 

# storing the subject 
    msg['Subject'] = "attendance_"+date

# string to store the body of the mail 
    body = "Respected sir,\nThe following document contains the attendance of "+date

# attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 

# open the file to be sent 
    
    attachment = open(filename, "rb") 

# instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
    p.set_payload((attachment).read()) 

# encode into base64 
    encoders.encode_base64(p) 

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# attach the instance 'p' to instance 'msg' 
    msg.attach(p) 

# creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
    s.starttls() 

# Authentication 
    s.login(fromaddr, "cvscpscm") 

# Converts the Multipart msg into a string 
    text = msg.as_string() 

# sending the mail 
    s.sendmail(fromaddr, toaddr, text) 

# terminating the session 
    s.quit() 

  
