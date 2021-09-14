import win32com.client as win32
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
def sender():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = '761317@cognizant.com'
    mail.Subject = 'Status Report'
    mail.Body = 'Message body'
    mail.HTMLBody = '<h2>Hi, Here is the report</h2>' #this field is optional
    attach=dir_path+"\\report.zip"
# To attach a file to the email (optional):
    attachment  = attach
    mail.Attachments.Add(attachment)

    mail.Send()

