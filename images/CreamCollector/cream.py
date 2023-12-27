from telethon.sync import TelegramClient

api_id = 24604317 #12345
api_hash = '4ad3a4c6528080ec6592877d8c34fb43' #'0123456789abcdef0123456789abcdef'
phone_number = '+79782908358'
#bot_token = '6905665943:AAFm1KCC4PR_lX2QesYrIrCsirBZGf9yLZI' #'12345:0123456789abcdef0123456789abcdef'

# We have to manually call "start" if we want an explicit bot token
client = TelegramClient('cream', api_id, api_hash)#TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
#bot.send_code_request('+79782908358')
#code = input()
#bot.sign_in('+79782908358',code)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))
channel = input('Введите название канала: ')

messages = client.iter_messages(channel)#bot.get_messages(channel)

#print(bot.get_me())
#for message in client.iter_messages(channel):
#        print(message.sender_id, ':', message.text)
print(messages[0].text)
print(messages[1].text)
print(messages[2].text)
