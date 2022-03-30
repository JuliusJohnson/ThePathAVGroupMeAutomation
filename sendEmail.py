import yagmail
import config.credentials


def sendMail(preservice,service):
    yag = yagmail.SMTP(config.credentials.gmailusername, config.credentials.appsPassword)
    contents = [
        f"<h1>Order of Service</h1> \n <p>This is an autogenrated email</p> \n <h2>Pre-Service</h2> {preservice} \n <h2>Service</h2> {service}"
    ]

    yag.send('hekol82277@f1xm.com', 'subject', contents)

# # sendEmail("test")