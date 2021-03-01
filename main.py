from emails import Email


class Bot():
    def __init__(self):
        pass

    def send_email(self):
        host = 'smtp.gmail.com'
        port = '587'
        user = 'brunoferreira.tecnico@gmail.com'
        password = ''
        subject = 'Teste'
        body = 'Teste 123'
        to = 'brunoferreirasoftware@gmail.com'
        copied = ['brunoperfil02@gmail.com', 'bruno.silva@realdatapower.com']

        self.email = Email(host,
                           port,
                           user,
                           password,
                           subject,
                           body,
                           to,
                           copied)

        self.email.configs()
        self.email.message()
        self.email.html()
        self.email.attachment()
        self.email.send()


bot = Bot()
bot.send_email()
print('')
