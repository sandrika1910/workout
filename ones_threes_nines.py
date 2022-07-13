class CheckAnswr:
	def ones_threes_nines(self,num):
		self.num = num
		self.nines,self.threes,self.ones = 0,0,0

		if self.num // 9 >= 1:
			self.nines = self.num // 9
			self.num -= self.nines * 9

			if self.num // 3 >= 1:
				self.threes = self.num // 3	
				self.num -= self.threes * 3

				if self.num // 1 >= 1:
					self.ones = self.num // 1
				else:
					self.ones = 0
			else:
				self.ones = self.num // 1
				
		else:
			if self.num // 3 >= 1:
				self.threes = self.num // 3	
				self.num -= self.threes * 3
				print(f'threes: {self.threes}; num: {self.num}')
				if self.num // 1 >= 1:
					self.ones = self.num // 1
				else:
					self.ones = 0
			else:
				self.ones = self.num // 1

		return f"nines: {self.nines}, threes: {self.threes}, ones: {self.ones} "

obj = CheckAnswr()
print(obj.ones_threes_nines(int(input('number: '))))
