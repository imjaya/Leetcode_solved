#append to a list and check if there is a pair
class Solution:
		def isValid(self, s: str) -> bool:
			if not s:
				return True
			if len(s)==1:
				return False
			left = "{[("
			pair = "{}()[]"
			x = []
			for i in s:
				if i in left:
					x.append(i)
				else:
					if not x or x.pop()+i not in pair:
						return False      
			return True if not x else False