#sethook
import requests
import json
auth_token = 'xxxxxxxxx-ttttttttttttttttt-wwwwwwwwwwww' # тут ваш токен полученный в начале #п.2
hook = 'https://chatapi.viber.com/pa/set_webhook'
headers = {'X-Viber-Auth-Token': auth_token}


sen = dict(url='https://yourdomain.ru/webhook2020',
           event_types = ['unsubscribed', 'conversation_started', 'message', 'seen', 'delivered'])
# sen - это body запроса для отправки к backend серверов viber
#seen, delivered - можно убрать, но иногда маркетологи хотят знать,
#сколько и кто именно  принял и почитал ваших сообщений,  можете оставить)

r = requests.post(hook, json.dumps(sen), headers=headers)
# r - это пост запрос составленный по требованиям viber 
print(r.json())
# в ответном print мы должны увидеть "status_message":"ok" - и это значит,
#  что вебхук установлен