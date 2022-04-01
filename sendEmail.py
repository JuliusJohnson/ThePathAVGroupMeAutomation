import yagmail
import config.credentials


def sendMail(preservice,service):
    yag = yagmail.SMTP(config.credentials.gmailusername, config.credentials.appsPassword)
    contents = [
        f"<table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\"><tr><td align=\"center\"><h1>Order of Service</h1> \n <p>This is an autogenrated email</p> \n <h2>Pre-Service</h2> {preservice} \n <h2>Service</h2> {service} </td></tr></table>"
    ]

    yag.send('lecale3092@nuesond.com', 'subject', contents)

# # sendEmail("test")