import numpy as numpy
import sys

def mypoly(x):
	result = x**3 + 8
	return result

def main():
	i = mypoly(9)
	print(1)
	if i > 27:
		print("YAY!")

if __name__=="__main__":
	main()