class A (object):
	def print_hi(self):
		print('hi')
		
class B (A):
	def __init__(self):
		self.hi = 'hi'
		
def run(b):

	if hasattr(b, 'print_hi') and callable(getattr(b, 'print_hi')):

		b.print_hi()
	
#if callable(getattr(b, 'print_bye', None)):
	#print('check')
	
	#b.print_bye()
	
#if not callable(getattr(b, 'pie', None)):
	#print('error ')
