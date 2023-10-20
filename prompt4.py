import sys

class animal:

	def print(self):
		print("My favorite animal are axoltols!")
		print(f"Length of its arms : {self.length_arms}")
		print(f"Length of its legs : {self.length_legs}")
		print(f"Number of eyes it has : {self.num_eyes}")
		if (self.tail==True):
			print("I have a tail.")
		else:
			print("I do not have a tail.")

		if (self.furry==True):
			print("I am furry.")
		else:
			print("I am not furry.")


	
	def __init__(self,larms,llegs,neyes,ntail,nfurry):
		self.length_arms = larms
		self.length_legs = llegs
		self.num_eyes = neyes
		self.tail = ntail
		self.furry = nfurry

def main():
	axoltol = animal(2.0,2.0,2,True,False)
	axoltol.print()

if __name__=="__main__":
	main()