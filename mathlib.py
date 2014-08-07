#### IMPORT MODULES
from math import *
from decimal import *
from copy import * 
import multiprocessing
import operator



#### TESTING EXPRESSIONS

########################
####	IntegerQ
########################
# Testing the integers or not.
#	IntegerQ(10.0) -> True

def IntegerQ(double) : 
	if isinstance(double , int) : return True
	if not isinstance(double , float) : return "@IntegerQ. TypeError : The argument is NOT 'double'."
	return True if double - int(double) == 0 else False

########################
####	PrimeQ
########################
# Testing the prime or not.
# This algo is refered to the overview of Probrem 10 written by daniel.is.fischer.
#	PrimeQ(11) -> True

def PrimeQ(integer) : 
	if not isinstance(integer , int) : return "@PrimeQ. TypeError : The argument is NOT 'int'."
	if integer == 1 : return False
	if integer < 4 : return True
	if integer % 2 == 0 : return False
	if integer < 9 : return True
	if integer%3 == 0 : return False
	r = int(sqrt(integer))
	f = 5
	while f <= r : 
		if integer % f == 0 : return False
		if integer % (f + 2) == 0 : return False
		f = f + 6
	return True

########################
####	RepdigitQ
########################
# Testing the repdigit number or not.
#	RepdigitQ(111) -> True

def RepdigitQ(integer) : 
	if not isinstance(integer , int) : return "@RepdigitQ. TypeError : The argument is NOT 'int'."
	if integer < 10 : return "@RepdigitQ. The argument is required at least two digits."
	return True if Tally(ToDigit(integer))[0][1] == len(ToDigit(integer)) else False

########################
####	TriangleNumberQ
########################
# Testing the triangle number or not.
#	TriangleNumberQ(21) -> True

def TriangleNumberQ(integer) : 
	if not isinstance(integer , int) : return "@TriangleNumberQ. TypeError : The argument is NOT 'int'."
	return True if IntegerQ(( - 1 + sqrt(1 + 8 * integer))/2) else False

########################
####	PentagonNumberQ
########################
# Testing the pentagon number or not.
#	PentagonNumberQ(12) -> True

def PentagonNumberQ(integer) : 
	if not isinstance(integer , int) : return "@PentagonNumberQ. TypeError : The argument is NOT 'int'."
	return True if IntegerQ((1 + sqrt(1 + 24 * integer))/6) else False

########################
####	HexagonNumberQ
########################
# Testing the hexagon number or not.
#	HexagonNumberQ(15) -> True

def HexagonNumberQ(integer) : 
	if not isinstance(integer , int) : return "@HexagonNumberQ. TypeError : The argument is NOT 'int'."
	return True if IntegerQ((1 + sqrt(1 + 8 * integer))/4) else False

########################
####	PandigitalQ
########################
# Testing the pandigital number or not.
#	PandigitalQ([3 , 1 , 2]) -> True

def PandigitalQ(lst) : 
	if not isinstance(lst , list) : return "@PandigitalQ. TypeError : The arguments is NOT 'list'."
	digit_lst = []
	for i in range(len(lst)):
		digit_lst.append(ToDigit(lst[i]))
	if [x for x in sorted(Flatten(digit_lst))] == [x for x in range(1 , len(lst) + 1)] : 
		return True
	else : 
		return False

########################
####	Pandigital0Q
########################
# Testing the pandigital number containing 0 or not.
#	Pandigital0Q([1 , 0 , 2 , 3]) -> True

def Pandigital0Q(lst) : 
	if not isinstance(lst , list) : return "@Pandigital0Q. TypeError : The arguments is NOT 'list'."
	digit_lst = []
	for i in range(len(lst)):
		digit_lst.append(ToDigit(lst[i]))
	if [x for x in sorted(Flatten(digit_lst))] == [x for x in range(0 , len(lst))] : 
		return True
	else : 
		return False

#### NUMBER THEORY

########################
####	Divisors
########################
# To give a list of the integers that divide n.
#	Divisors(21) -> [1, 3, 7, 21]

def Divisors(integer) : 
	if not isinstance(integer , int) : return "@Divisors. TypeError : The argument is NOT 'int'."
	s = int(sqrt(integer))
	lst = []
	for i in range(1 , s + 1) : 
		if integer % i == 0 : lst.extend([i , integer /i])
	return sorted(lst)

########################
####	GCD
########################
# To give the greatest common divisor of integers.
#	GCD(15 , 21) -> 3

def GCD(integer1 , integer2) : 
	if not isinstance(integer1 , int) or not isinstance(integer2 , int) : return "@GCD. TypeError : Both the arguments are NOT 'int'."
	a , b = max(integer1 , integer2) , min(integer1 , integer2)
	r = a % b
	if r == 0 : return b
	return GCD(b , r)

########################
####	LCM
########################
# To give the least common multiple of integers.
#	LCM(3 , 5) -> 15

def LCM(integer1 , integer2) : 
	if not isinstance(integer1 , int) or not isinstance(integer2 , int) : return "@LCM. TypeError : Both the arguments are NOT 'int'."
	return integer1 * integer2 / GCD(integer1 , integer2)

#### ELEMENTARY FUNCTIONS

########################
####	nth_Fibonacci
########################
# To give n-th Fibonacci number.(OEIS A000045)
#	nth_Fibonacci(6) -> 8

def nth_Fibonacci(integer) : 
	if not isinstance(integer , int) : return "@nth_Fibonacci. TypeError : The argument is NOT 'int'."
	cnt , a , b = 0 , 0 , 1
	for cnt in range(integer) : 
		a , b = b , a + b
	return a

########################
####	nth_Prime
########################
# To give n-th Prime number.
#	nth_Prime(3) -> 5

def nth_Prime(integer) : 
	if not isinstance(integer , int) : return "@nth_Prime. TypeError : The argument is NOT 'int'."
	if integer == 1 : return 2
	if integer == 2 : return 3
	if integer == 3 : return 5
	if integer == 4 : return 7
	if integer == 5 : return 11
	upper = int(integer * log(integer) + integer * log(log(integer)))
	search = list(range(2 , upper))
	prime = []
	while len(search) > 0 : 
		p = search.pop(0)
		i = 1
		while 1:
			if i >= len(search) : break
			if search[i]%p == 0 : search.pop(i)
			i += 1
		prime.append(p)
	return prime[integer - 1]

########################
####	nth_ChampernowneNumber
########################
# To give n-th digit of the fractional part of the ChampernowneNumber
#	nth_ChampernowneNumber(12) -> 1

def nth_ChampernowneNumber(integer) : 
	if not isinstance(integer , int) : return "@nth_ChampernowneNumber. TypeError : The argument is NOT 'int'."
	res = integer
	digit = 1
	while res > 0 : 
		if res - 9 * pow(10 , digit - 1) * digit > 0:
			res -= int(9 * pow(10 , digit - 1) * digit)
			digit += 1
		else : 
			num = int((res - 1)/digit)
			res -= digit * num
			break
	if digit == 1:
		return integer
	else : 
		return ToDigit(int(pow(10 , digit - 1) + num))[res - 1]

########################
####	CountCycle_inFraction
########################
# To give the number of the recurring cycle in the decimal representation of the unit fractions.
#	CountCycle_inFraction(7) -> 6

def CountCycle_inFraction(integer) : 
	if not isinstance(integer , int) : return "@CountCycle_inFraction. TypeError : The argument is NOT 'int'."
	frac = str(Decimal(1)/Decimal(integer))
	l = len(frac) - 1
	for i in range(l - 2 , 2 , -1):
		b = True
		if frac[l - 1] == frac[i] : 
			c = l - i - 1
			for j in range(c):
				if frac[i + j] != frac[i + j - c] : 
					b = False
					break
			if b : return c
	return 0

########################
####	Factorial
########################
# Factorial
#	Factorial(3) -> 6

def Factorial(integer) : 
	if not isinstance(integer , int) : return "@Factorial. TypeError : The argument is NOT 'int'."

	c = multiprocessing.cpu_count()

	def p_fac(integer) : 
		product = 1
		if integer == 0 : return 1
		for num in range(1 , integer + 1 , c):
			product *= num
		return product

	p = multiprocessing.Pool()
	return reduce(operator.mul , p.map(p_fac , range(integer , integer - c , -1)) , 1)


#### ESTIMATION

########################
####	StirlingApproximation
########################
# To estimate the n factorial
#	StirlingApproximation(10) -> 3598810.84159 (True value : 3628800)

def StirlingApproximation(integer) : 
	if not isinstance(integer , int) : "@Stirling Approximation. TypeError : The argument is NOT 'int'."
	return sqrt(2 * pi * integer) * pow(integer/e , integer) * (1 + 1/(12 * integer) + 1/(288 * pow(integer , 2)) - 139/(51840 * pow(integer , 3)) - 571/(2488320 * pow(integer , 4)))

#### LIST MANIPULATION

########################
####	ToDigit
########################
# Transforming an integer to the list of digits.
#	ToDigit(123) -> [1 , 2 , 3]

def ToDigit(integer) : 
	if not isinstance(integer , int) : return "@ToDigit. TypeError : The argument is NOT 'int'."
	return [int(x) for x in str(int(integer))]

# If you handle the long type in Python2.7 , you can use ToDigitL.(In Python3 , the long type was integrated into the int type.)
def ToDigitL(integer) : 
	if not isinstance(integer , int) and not isinstance(integer , long) : return "@ToDigitL. TypeError : The argument is NOT 'int' or 'long'."
	return [int(x) for x in str(long(integer))]

########################
####	ToInteger
########################
# Transforming the list of digits to an intger.
#	ToInteger([0 , 1 , 2 , 3]) -> 123

def ToInteger(lst) :
	if not isinstance(lst , list) : return "@ToInteger. TypeError : The argument is NOT 'list'."
	if isinstance(lst , str) : return "@ToInteger. TypeError : The argument is 'string'."
	integer = 0
	for i in range(len(lst)):
		integer += lst[i] * pow(10 , len(lst) - i - 1)
	return int(integer)

# If you handle the long type in Python2.7 , you can use ToIntegerL.(In Python3 , the long type was integrated into the int type.)
def ToIntegerL(lst) :
	if not isinstance(lst , list) : return "@ToIntegerL. TypeError : The argument is NOT 'list'."
	if isinstance(lst , str) : return "@ToIntegerL. TypeError : The argument is 'string'."
	integer = 0
	for i in range(len(lst)):
		integer += lst[i] * pow(10 , len(lst) - i - 1)
	return long(integer)


########################
####	DeleteCases
########################
# To removes all elements of list that match pattern.
#	DeleteCases([0 , 1 , 2 , 3 , 'a'] , 3) -> [0, 1, 2, 'a']
#	DeleteCases([0 , 1 , 2 , 3 , 'a'] , [0 , 3]) -> [1, 2, 'a']

def DeleteCases(lst , expr):
	if not isinstance(lst, list) : return "@DeleteCases. TypeError : The first argument is NOT 'list'."
	if not (isinstance(expr , str) or isinstance(expr , int) or isinstance(expr , list)) : return "@DeleteCases. TypeError : The second argument is NOT either 'list' , 'str' or 'int'."
	lst_copy , expr_copy = deepcopy(lst) , deepcopy(expr)
	if isinstance(expr , list) :
		if expr[0] in lst_copy : 
			while expr[0] in lst_copy : 
				lst_copy.remove(expr_copy[0])
			expr_copy.pop(0)
			return lst_copy if expr_copy == [] else DeleteCases(lst_copy , expr_copy)
		else : 
			return []
	else : 
		if expr_copy in lst_copy : 
			lst_copy.remove(expr_copy)
			return lst_copy
		else : 
			return []

########################
####	Flatten
########################
# To flatten out nested lists.
#	Flatten([0 , 1 , [2 , ['a']]]) -> [0, 1, 2, 'a']

def Flatten(lst):
	if isinstance(lst, list) : 
		return [] if lst == [] else Flatten(lst[0]) + Flatten(lst[1:])
	else : 
		return [lst]

########################
####	Tuples
########################
# To generate a list of all possible n-tuples of elements from list.
#	Tuples([0 , 1] , 2) -> [[0, 0], [0, 1], [1, 0], [1, 1]]

def Tuples(lst , integer) : 
	if not isinstance(lst , list) or not isinstance(integer , int) : return "@Tuples. TypeError : The arguments are NOT respectively 'list' and 'int'."
	if integer == 1:
		return lst
	else : 
		return [Flatten([x] + [y]) for x in lst for y in Tuples(lst , integer - 1)]

########################
####	Permutations
########################
# To generate a list of all possible permutations of the elements in list.
#	Permutations(['a' , 'b' , 'c'] , 2) -> [['a', 'b'], ['a', 'c'], ['b', 'a'], ['b', 'c'], ['c', 'a'], ['c', 'b']]

def Permutations(lst , integer) : 
	if not isinstance(lst , list) or not isinstance(integer , int) : return "@Permutations. TypeError : The arguments are NOT respectively 'list' and 'int'."
	if integer == 1:
		return [[lst[index]] for index in range(len(lst))] 
	else : 
		return [Flatten([x] + [y]) for x in lst for y in Permutations(DeleteCases(lst , x) , integer - 1)]

########################
####	Combinations
########################
# To generate a list of all possible combinations of the elements in list.
#	Combinations(['a' , 'b' , 'c'] , 2) -> [['a', 'b'], ['a', 'c'], ['b', 'c']]

def Combinations(lst , integer) : 
	if not isinstance(lst , list) or not isinstance(integer , int) : return "@Combinations. TypeError : The arguments are NOT respectively 'list' and 'int'."
	return DeleteDuplicates([sorted(elem) for elem in Permutations(lst , integer)])

########################
####	Riffle
########################
# To riffle the list within an expr.
#	Riffle([1 , 2 , 3] , ['x' , 'y']) -> [1, 'x', 2, 'y', 3, 'x']
#	Riffle([1 , 2 , 3] , 0) -> [1, 0, 2, 0, 3, 0]

def Riffle(lst , expr) : 
	if not isinstance(lst , list) : return "@Riffle. TypeError : The first argument is NOT 'list'."
	if not (isinstance(expr , str) or isinstance(expr , int) or isinstance(expr , list)) : return "@Riffle. TypeError : The second argument is NOT either 'list' , 'str' or 'int'."
	if isinstance(expr , list) :
		if len(lst) > len(expr) : expr *= (int(len(lst)/len(expr)) + 1)
		return [lst[0]] + [expr[0]] + Riffle(lst[1:] , expr[1:]) if len(lst) > 0 else []
	else : 
		return [lst[0]] + [expr] + Riffle(lst[1:] , expr) if len(lst) > 0 else []

########################
####	DeleteDuplicates
########################
# To deletes all duplicates from list.
#	DeleteDuplicates([1, 7, 8, 4, 3, 4, 1, 9, 9, 2]) -> [1 , 7 , 8 , 4 , 3 , 9 , 2]

def DeleteDuplicates(lst) : 
	if not isinstance(lst , list) : return "@DeleteDuplicates. TypeError : The argument is NOT 'list'."
	newlst=[]
	for elem in lst:
		if elem not in newlst:
			newlst.append(elem)
	return newlst

########################
####	Tally
########################
# To tally the elements in list, listing all distinct elements together with their multiplicities.
#	Tally(['a' , 'a' , 'b' , 'a' , 'c' , 'b' , 'a']) -> [['a' , 4] , ['b' , 2] , ['c' , 1]]

def Tally(lst) : 
	if not isinstance(lst , list) : return "@Tally. TypeError : The argument is NOT 'list'."
	unique_lst = DeleteDuplicates(lst)
	return Transpose([unique_lst , map((lambda x : lst.count(x)) , unique_lst)])

########################
####	Position
########################
# To give a list of the positions at which objects matching pattern appear in expr.
#	Position(['a' , 'a' , 'b' , 'a' , 'c' , 'b' , 'a'] , 'a') -> [0 , 1 , 3 , 6]

def Position(lst , expr) : 
	if not isinstance(lst , list) : return "@Position. TypeError : The argument is NOT 'list'."
	position_list = []
	for count in range(len(lst)):
		if lst[count] == expr:
			position_list.append(count)
	return position_list

########################
####	Transpose
########################
# To transpose the first two levels in list. The length of the returned list is fit with the shorter list.
#	Transpose([[1 , 3 , 5] , [2 , 4]]) -> [[1 , 2] , [3 , 4]]

def Transpose(lst) : 
	if not isinstance(lst , list) : return "@Transpose. TypeError : The argument is NOT 'list'."
	return [list(elem) for elem in zip(*lst)]

########################
####	Compare
########################
# To compare two lists. This returns indices that match same place in each list.
#	Compare(['l' , 'i' , 'm' , 'e'] , ['l' , 'e' , 'm' , 'm' , 'o' , 'n']) -> [0 , 2]

def Compare(lst1 , lst2) : 
	if not isinstance(lst1 , list) and not isinstance(lst2 , list) : return "@Compare. TypeError : The arguments are NOT 'list'."
	return [index for index in range(min(len(lst1) , len(lst2))) if lst1[index] == lst2[index]]

########################
####	Filter
########################
# To filter the list using the index list. This returns elements that match in the index list.
#	Filter(['l' , 'i' , 'm' , 'e'] , [0 , 2]) -> ['l' , 'm']

def Filter(expr , indices) : 
	if not isinstance(expr , list) and not isinstance(indices , list) : return "@Filter. TypeError : The arguments are NOT 'list'."
	for i in range(len(indices)):
		if not IntegerQ(indices[i]) : return "@Filter. TypeError : The index list is required only integers."
	return [expr[i] for i in indices]

########################
####	Product
########################
# To product all of elements in list.
#	Product([2 , 3 , 5]) -> 30

def Product(lst) : 
	if not isinstance(lst , list) and not any([isinstance(element , int) for element in lst]) : return "@Product. TypeError : The argument is NOT 'list' or any elements of the list is NOT 'int'."
	return reduce(operator.mul , lst)
#	return lst[0] * Product(lst[1:]) if len(lst) > 1 else lst[0]

########################
####	InnerProduct
########################
# To calculate the inner product.
#	InnerProduct([1 , 3 , 5] , [2 , 4 , 6]) -> 44

def InnerProduct(lst1 , lst2) : 
	if not isinstance(lst1 , list) and not isinstance(lst2 , list) : return "@InnerProduct. TypeError : The arguments are NOT 'list'."
	return sum([Product(scholar) for scholar in Transpose([lst1 , lst2])])

########################
####	PadLeft
########################
# To makes a list of length n by padding list with zeros on the left.
#	PadLeft([1 , 2 , 3] , 5) -> [0 , 0 , 1 , 2 , 3]

def PadLeft(lst , integer) : 
	if not isinstance(lst , list) or not isinstance(integer , int) : return "@PadLeft. TypeError : The arguments are NOT respectively 'list' and 'int'."
	return [0 for i in range(integer - len(lst))] + lst


########################
####	RotateLeft
########################
# To cycle the elements in lst n positions to the left.
#	RotateLeft([1 , 2 , 3 , 4] , 1) -> [2 , 3 , 4 , 1]

def RotateLeft(lst , integer) : 
	if not isinstance(lst , list) or not isinstance(integer , int) : return "@RotateLeft. TypeError : The arguments are NOT respectively 'list' and 'int'."
	n = integer % len(lst)
	return Flatten(lst[n:] + lst[:n])

########################
####	RotateRight
########################
# To cycle the elements in lst n positions to the right.
#	RotateRight([1 , 2 , 3 , 4] , 1) -> [4 , 1 , 2 , 3]

def RotateRight(lst , integer) : 
	if not isinstance(lst , list) or not isinstance(integer , int) : return "@RotateRight. TypeError : The arguments are NOT respectively 'list' and 'int'."
	n = (-integer) % len(lst)
	return RotateLeft(lst , n)

########################
####	Intersection
########################
# To give a sorted list of the elements common to all the list.
#	Intersection([[3 , 2 , 1] , [1 , 3 , 5]]) -> [1 , 3]

def Intersection(lst) : 
	if not isinstance(lst , list) : return "@Intersection. TypeError : The argument is NOT 'list'."
	if len(lst) > 2 : 
		return Intersection([DeleteDuplicates(sorted([elem for elem in lst[0] if elem in lst[1]]))] + lst[2:])
	else : 
		return DeleteDuplicates(sorted([elem for elem in lst[0] if elem in lst[1]]))

########################
####	Union
########################
# To give a sorted list of all the distinct elements that appear in any of the list.
#	Union([[3 , 2 , 1] , [1 , 3 , 5]]) -> [1 , 2 , 3 , 5]

def Union(lst) : 
	if not isinstance(lst , list) : return "@Intersection. TypeError : The argument is NOT 'list'."
	return lst if len(lst) == 0 else sorted(DeleteDuplicates(Flatten(lst)))

########################
####	Complement
########################
# To find which elements in the first list are not in any of the subsequent lists.
#	Complement([[9 , 8 , 5 , 2 , 1] , [3 , 1 , 5] , [7 , 9]]) -> [2 , 8]

def Complement(lst) : 
	if not isinstance(lst , list) : return "@Complement. TypeError : The argument is NOT 'list'."
	if len(lst) > 1 : 
		return Complement([DeleteDuplicates(sorted([elem for elem in lst[0] if elem not in lst[1]]))] + lst[2:])
	else : 
		return DeleteDuplicates(sorted(lst[0]))

########################
####	WordScore
########################
# Scoring the CAPITAL letters in the word.
#	WordScore('ALPHABET') -> [1, 12, 16, 8, 1, 2, 5, 20]

def WordScore(string) : 
	if not isinstance(string , str) : return "@WordScore. TypeError : The argument is NOT string."
	lst = [c for c in string]
	num_lst = []
	for c in lst : 
		if 95 < ord(c) < 123 : return "Any small letters are included in the argument."
		if 64 < ord(c) < 92 : 
			num_lst.append(ord(c) - 64)
		else : 
			return "A non capital letter is included in the argument."
	return num_lst

#### FILE I/O

########################
####	FileToList
########################
# Rearranging a text file to a list.
#	WordScore('./word.txt') -> ['"A"', '"ABILITY"', '"ABLE"', ... ]

def FileToList(string) : 
	if not isinstance(string , str) : 
		print("@FileToList. This is not a file path.")
		return None
	f = open(string , 'r')
	for line in f:
		itemList = line[:-1].split(',')
	return itemList

