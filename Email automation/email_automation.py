#this is for sending my email to HR for internship

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#here you write email detail

sender_email = "your email"
reciver_email = "reciver email"
password = "app pass word"    #for password use "app possword" option password of google account, don't type main one

#content for email

subject = "Application for internship"
body = """Dear Hiring Manager,
I am excited to apply for a Data Engineering internship at your organization. With hands-on experience building ETL pipelines, optimizing workflows with Apache Spark and Airflow, and applying machine learning models that achieved a ROC-AUC score of 0.82, I am eager to contribute to scalable, data-driven IT solutions.
My background includes developing automated CSV-to-database pipelines, working with MySQL/PostgreSQL, and applying Python (pandas, NumPy) for data cleaning and analysis. These experiences have strengthened my ability to design reliable systems and deliver actionable insights.
I am motivated to learn from industry professionals and contribute to your IT team’s success. I would welcome the opportunity to discuss how my skills align with your current projects.
Best regards,
Paras Nainwal
nainwalparas@gmail.com"""

#now we will setup the mime

message = MIMEMultipart()
message["FROM"] = sender_email
message["To"] = reciver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))
filename = "ypur resume file"   # resume file 
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename={filename}",
)
message.attach(part)


try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, reciver_email, message.as_string())
        print("Email send successfully!")

except Exception as e :
    print(f"error : {e}")

