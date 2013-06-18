# -*- coding: utf8 -*-

class Machines():
	inserted_money_sum = 0  #최종 투입된 금액
	#Test Code짜고 나서 시간 남으면 product를 객체화 하기
	products_dict = {
					'vita500'   : {'price' : 500, 'number' : 2},
					'milk'      : {'price' : 700, 'number' : 13},
					'coffee'    : {'price' : 900, 'number' : 8}
					}

	def add_money(self, inserted_money):
		#입력 데이터를 숫자형으로 형변환 (왜냐면 $raw_input()은 숫자입력도 문자열로 입력을 받기때문)
		# [성환] 기계에 동전이 아닌 다른것을 넣으려고 하면 에러출력후 종료
		self.inserted_money_sum += inserted_money
		print '[Machine] 지금까지 %d가 투입되었네요' % self.inserted_money_sum
		
	def show_list_products(self):
		print '\n구매가능 음료수'
		print '현재 투입금액 : %d'%self.inserted_money_sum
		print '------------------'
		for key,value in sorted(self.products_dict.items()):
			# 자판기에 있는 총액보다 가격이 적을경우에만 보여줌
			if value['price'] < self.inserted_money_sum and value['number'] > 1:
				print "[Machine]%s : %d원" % (key,value['price'])

	def select_product(self, product):
		# 음료수를 선택할때 음료수의 개수를 줄이고, 알맞게 고른건지 말해줌
		if not product:
			print '음료 선택을 종료합니다'
			return '[Select End]'


		if product in self.products_dict.keys():
			# 1. product의 price가 내가 가진 금액보다 비싸면 못팜,  
			# 2. product의 개수가 모자라면 못팜
			# show_list_products는 출력만 안해줄뿐 처리를 막아 주진 않음 그래서 이곳에서 해줌
			if self.inserted_money_sum > self.products_dict[product]['price'] and self.products_dict[product]['number'] > 1:
				self.products_dict[product]['number'] = self.products_dict[product]['number']-1
				self.inserted_money_sum -= self.products_dict[product]['price']
				print '[ Machine ] %s 음료수 나옴'%product
				return '[Select OK]'
			else:
				print '개수가 모자라거나, 투입된 금액이 모자랍니다' # 나중에는 같이 처리하지 말고 개수가 모자랄경우에는 [Select Error를 반환해 다시 고를 수 있게하자]
				return '[Select End]'
		else:
			print '[Machine] 메뉴를 다시 골라주세요'
			return '[Select Error]'

	def sell_product(self):	
		while 1:
			self.show_list_products()
			product = raw_input("마실거 고르기? (안먹고 돈 받으려면 엔터)")
			if self.select_product(product) == '[Select End]':
				break

		print '반환금 %d'%self.inserted_money_sum
		


class Human():
	#{ 돈의종류 : 돈의갯수 }
	my_money_dict = {5000 : 2 , 1000 : 1, 500 : 2 , 100 : 8} 

	def check_money(self):
		print '\n내 주머니 상황'
		print '--------------------'
		for key,value in sorted(self.my_money_dict.items()):
			print "%d원이 %d개 있어요" % (key,value)

	def insert_money(self, Machines):
		inserted_money = raw_input('\n돈을 넣으세요(입금을 마치려면 엔터) : ')
		
		if not inserted_money: 
			print '입금을 종료합니다'
			return '[Insert End]'

		# 주화가 아닌 다른것을 넣으려고 한다면 에러 출력후 종료
		try:
			inserted_money = int(inserted_money)

		except ValueError:
			print "[!]뭘 넣으려고 하시는 겁니까. 그러다 기계 고장납니다."
			return '[Not Coin]'

		#투입한 만큼 지갑에서 돈을 뺀다. (해당 돈의 갯수에서 하나 빼기)
		# [성환] 존재하지 않는 주화를 넣으려 한다면 에러출력후 종료
		try:
			if self.my_money_dict[inserted_money] > 0:
				Machines.add_money(inserted_money)
				self.my_money_dict[inserted_money] -= 1
				self.check_money()
			else:
				self.check_money()
				print '[!]돈이 부족합니다'
				return '[Lack Money]'
        
		except KeyError:
			#[유효하지 않은 돈]
			print "[!]%d원 짜리는 존재 하지 않습니다."%(inserted_money)
			return '[Not Valid Coin]'

# 메인 로직
if __name__ == '__main__':
	machine = Machines()
	Sunghwan = Human()

	Sunghwan.check_money()
	
    #돈 투입하기
	while 1:
		if Sunghwan.insert_money(machine) == '[Insert End]':
			break
	
	#제품 판매
	machine.sell_product()
