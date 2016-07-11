# coding=utf-8

import sys
import time
import pprint
import telepot
 
def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	text = msg['text']
	print chat_id, text

	if text == 'D':
		bot.sendMessage(chat_id, """L: 사는 생물
O: 시대별로 불리는 명칭""")
	elif text == 'L':
		bot.sendMessage(chat_id, """A: 동물
P: 식물
B: 곤충""")
	elif text == 'O':
		bot.sendMessage(chat_id, """K: 고려시대
1: 1961년 ~ 현재""")
	elif text == 'A':
		bot.sendMessage(chat_id, """b: 새
S: 해양동물""")
	elif text == 'P':
		bot.sendMessage(chat_id, """G: 풀
T: 나무""")
	elif text == 'B':
		bot.sendMessage(chat_id, """a: 어리무당벌레
Z: 잠자리
N: 나비
I: 집게벌레
R: 독도장님노린재	
So: 섬땅방아벌레""")
	elif text == 'K':
		bot.sendMessage(chat_id, """Woo: 우산도""")
	elif text == '1':
		bot.sendMessage(chat_id, """Dz: 독도""")
	elif text == 'b':
		bot.sendMessage(chat_id, """Bd: 바다제비
Sem: 슴새
Gu: 괭이갈매기
Ye: 노랑부리백로
Br: 황초롱이""")
	elif text == 'S':
		bot.sendMessage(chat_id, """Og: 오징어
Bri: 명티
Dae: 대구
Sh: 상어
Song: 송어T
Jon: 전복
Night: 밤고동
Tea: 감태
Sora: 소라
By: 바위게
Pa: 부채게
Star: 불가사리
Gas: 성게
Dom: 자리돔
Bang: 벵에돔
Mshrimp: 물렁가시붉은새우
Dshrimp: 도화새우""")
	elif text == 'G':
		bot.sendMessage(chat_id, """Ss: 쇠비름
Z: 주름제비란
GG: 괭이밥
Be: 붉은가시딸기
Ba: 바위수국
Ea: 섬장대""")
	elif text == 'T':
		bot.sendMessage(chat_id, """Em: 섬괴불나무
Zi: (줄)사철나무
Bo: 보리밥나무""")
	elif text == 'Z':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EC%9E%A0%EC%9E%90%EB%A6%AC""")
	elif text == 'N':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EB%82%98%EB%B9%84""")
	elif text == 'I':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EC%A7%91%EA%B2%8C%EB%B2%8C%EB%A0%88%EB%AA%A9""")
	elif text == 'Bd':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EB%B0%94%EB%8B%A4%EC%A0%9C%EB%B9%84""")
	elif text == 'Sem':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EC%8A%B4%EC%83%88""")
	elif text == 'Gu':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EA%B4%AD%EC%9D%B4%EA%B0%88%EB%A7%A4%EA%B8%B0""")
	elif text == 'Ye':
		bot.sendMessage(chat_id, """""")
	else:
		# help message
		bot.sendMessage(chat_id, """이 프로그램은 독도에 대해 잘 모르시는 분들을 위해 만들었습니다. 이 프로그램을 작동시키시면 독도의 생물과 역사가 나올 텐데, 생물의 정보가 많아서 독도의 생물에 대해 알 수 있는 프로그램이라고 생각하시면 됩니다. 어떤 것들이 사는지는 알 수 있게 될 것입니다. 
			D를 치시면, 메뉴가 나옵니다.

			D: 메뉴.""")

	#bot.sendMessage(chat_id, text)


TOKEN = "231215962:AAGzoIw7kfHgpbusvvngOyM4TTuBaeG1Jbs"


bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

while 1:
		time.sleep(10)