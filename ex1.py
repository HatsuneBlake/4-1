def rangetest(*argcheks):
	def onDecorator(func):
		if not __debug__:
			return func
		else:
			def onCall(*args):
				for (i,low,high) in argcheks:
					if args[i] < low or args[i] > high:
						msg = 'Argument %s not in %s...%s'%(args[i],low,high)
						raise TypeError(msg)
				return func(*args)
			return onCall
	return onDecorator
	
@rangetest([0,1,12],[1,1,31],[2,0,2018])
def birthday(M,D,Y):
	print ('Birthday at {0}/{1}/{2}'.format(M,D,Y))
	
if __name__ == '__main__':
	birthday(1,1,2012)
	try:
		birthday(-1,-1,2012)
	except TypeError as e:
		print(e)