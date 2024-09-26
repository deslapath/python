def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if '@' not in recipient or '@' not in sender or not recipient.endswith(('.com', '.ru', '.net')) or not sender.endswith(('.com', '.ru', '.net')):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)


send_email('Курьер вас ждет', 'pekar@.ru', sender='university.help@gmail.com')
send_email('Листопад в сентябре', 'kolyan@.t', sender='valentina@.com')
send_email('Булочки подорожали', 'petr@.net', sender='petr@.net')
send_email('Курьер вас не дождался', 'kolyan@.net', sender='valentina@.com')





