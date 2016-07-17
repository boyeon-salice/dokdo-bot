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
		bot.sendMessage(chat_id, """
Z: 잠자리
N: 나비
I: 집게벌레""")
	elif text == 'K':
		bot.sendMessage(chat_id, """Woo: 우산도""")
	elif text == '1':
		bot.sendMessage(chat_id, """Dz: 독도""")
	elif text == 'b':
		bot.sendMessage(chat_id, """Bd: 바다제비
Sem: 슴새
Gu: 괭이갈매기
Ye: 노랑부리백로""")
	elif text == 'S':
		bot.sendMessage(chat_id, """Og: 오징어
Bri: 명태
Dae: 대구
Sh: 상어
Song: 송어
Jon: 전복
Pa: 부채게
Star: 불가사리
Gas: 성게
Dom: 자리돔
Bang: 벵에돔
Mshrimp: 물렁가시붉은새우
Dshrimp: 도화새우""")
	elif text == 'G':
		bot.sendMessage(chat_id, """Ss: 쇠비름
GG: 괭이밥
Be: 붉은가시딸기
Ba: 바위수국
Ea: 섬장대""")
	elif text == 'T':
		bot.sendMessage(chat_id, """Em: 섬괴불나무
Zi: (줄)사철나무
Bo: 보리밥나무""")
	elif text == 'Ss':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EC%87%A0%EB%B9%84%EB%A6%84""")
	elif text == 'Be':
		bot.sendMessage(chat_id, """https://www.culturecontent.com/content/contentView.do?search_div=CP_THE&search_div_id=CP_THE014&cp_code=cp1010&index_id=cp10100167&content_id=cp101001670001&print=Y""")
	elif text == 'Ba':
		bot.sendMessage(chat_id, """https://www.culturecontent.com/content/contentView.do?search_div=CP_THE&search_div_id=CP_THE014&cp_code=cp1010&index_id=cp10100332&content_id=cp101003320001&print=Y""")
	elif text == 'Ea':
		bot.sendMessage(chat_id, """http://www.ibric.org/myboard/read.php?id=753&Board=ulleung&PARA4=1""")
	elif text == 'Em':
		bot.sendMessage(chat_id, """http://namu-ro.com/LINK_SITE/search_index.php?num=546""")
	elif text == 'Zi':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EC%82%AC%EC%B2%A0%EB%82%98%EB%AC%B4""")
	elif text == 'Bo':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EB%B3%B4%EB%A6%AC%EB%B0%A5%EB%82%98%EB%AC%B4""")
	elif text == 'GG':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EA%B4%AD%EC%9D%B4%EB%B0%A5""")
	elif text == 'Dom':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EC%9E%90%EB%A6%AC%EB%8F%94""")
	elif text == 'Bang':
		bot.sendMessage(chat_id, """https://namu.wiki/w/%EB%B2%B5%EC%97%90%EB%8F%94""")
	elif text == 'Mshrimp':
		bot.sendMessage(chat_id, """http://www.nifs.go.kr/frcenter/species/?_p=species_view&mf_tax_id=MF0009080""")
	elif text == 'Dshrimp':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EB%8F%84%ED%99%94%EC%83%88%EC%9A%B0%EC%83%81%EA%B3%BC""")
	elif text == 'Gas':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EC%84%B1%EA%B2%8C%EB%A5%98""")
	elif text == 'Star':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EB%B6%88%EA%B0%80%EC%82%AC%EB%A6%AC%EB%A5%98""")
	elif text == 'Song':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EC%86%A1%EC%96%B4""")
	elif text == 'Jon':
		bot.sendMessage(chat_id, """dhttps://ko.wikipedia.org/wiki/%EC%A0%84%EB%B3%B5""")
	elif text == 'Pa':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EB%B6%80%EC%B1%84%EA%B2%8C%EC%83%81%EA%B3%BC""")
	elif text == 'Z':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EC%9E%A0%EC%9E%90%EB%A6%AC""")
	elif text == 'N':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EB%82%98%EB%B9%84""")
	elif text == 'I':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EC%A7%91%EA%B2%8C%EB%B2%8C%EB%A0%88%EB%AA%A9""")
	elif text == 'Bd':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EB%B0%94%EB%8B%A4%EC%A0%9C%EB%B9%84""")
	elif text == 'Woo':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EC%9A%B0%EC%82%B0%EB%8F%84""")
	elif text == 'Dz':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EB%8F%85%EB%8F%84""")
	elif text == 'Sem':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EC%8A%B4%EC%83%88""")
	elif text == 'Gu':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EA%B4%AD%EC%9D%B4%EA%B0%88%EB%A7%A4%EA%B8%B0""")
	elif text == 'Ye':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EB%85%B8%EB%9E%91%EB%B6%80%EB%A6%AC%EB%B0%B1%EB%A1%9C""")
	elif text == 'Og':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EC%98%A4%EC%A7%95%EC%96%B4""")
	elif text == 'Bri':
		bot. sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EB%AA%85%ED%83%9C""")
	elif text == 'Dae':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EB%8C%80%EA%B5%AC_(%EC%96%B4%EB%A5%98)""")
	elif text == 'sh':
		bot.sendMessage(chat_id, """https://ko.wikipedia.org/wiki/%EC%83%81%EC%96%B4""")
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