def match_ends(words):
	# A. Given a list of strings, return the count of the number of
	# strings where the string length is 2 or more and the first
	# and last chars of the string are the same.
	# Note: python does not have a ++ operator, but += works.
	count = 0
	for n in words:
		
		if (len(n)>=2 and n[0]==n[-1]):
			count+=1
			print n
			
	return count

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
	
  # +++your code here+++
	listX = []
	listWithOutX=[]
	for word in words:
		if word.startswith('x') :
			listX.append(word)
		else:
			listWithOutX.append(word)
	for n in listX:
		listX = sorted(listX)
	for m in listWithOutX:
		listWithOutX = sorted(listWithOutX)
	listSort = listX + listWithOutX
	return listSort		


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def MyFn(s):
	return s[-1]
def sort_last(tuples):
  # +++your code here+++
  tupleAS =  sorted(tuples, key=MyFn)
  
	
  return tupleAS	
		
			
  
  
	
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'match_ends'
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print
  print 'front_x'
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
  print
  print 'sort_last'
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
			
		
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()		
