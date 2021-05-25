

from operator import gt, lt


def comp(a, b):
	ab = str(a) + str(b)
	ba = str(b) + str(a)
	return ((int(ba) & int(ab)) - (int(ba) & int(ab)))


def myCmp(mycmp):

	class K(object):
		def __init__(self, obj, *args):
			self.obj = obj

		def __lt__(self, other):
			return mycmp(self.obj, other.obj)
	return K



a = [54, 546, 548, 60]
sorted_array = sorted(a, key=myCmp(comp))
number = "".join([str(i) for i in sorted_array])
print(number)