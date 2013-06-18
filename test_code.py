import unittest
from src import *

class TestUm(unittest.TestCase):
	Test_human = Human()
	Test_machine = Machines()

	def test_trash_machine(self):
		self.assertEqual(self.Test_human.insert_money('trash_machine', 500), '[Insert End]')
		self.assertEqual(repr(self.Test_machine), '<Machine>')

	def test_insert_money(self):
		self.assertEqual(self.Test_human.insert_money(self.Test_machine, 500),'[Insert OK]' )
		self.assertEqual(self.Test_human.insert_money(self.Test_machine, ''),'[Insert End]' )
		self.assertEqual(self.Test_human.insert_money(self.Test_machine, 1234),'[Not Valid Coin]' )
		self.assertEqual(self.Test_human.insert_money(self.Test_machine, 'abc'),'[Not Coin]' )
	"""
	def test_select_product(self):
		Test_machine.select_product에서
		[Select OK]
		[Select Error]
		[Select End] 되는 경우 Test하기
	"""

if __name__=='__main__':
	unittest.main()
