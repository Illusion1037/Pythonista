def run(obj):
	if callable(getattr(obj, 'init', None)):
		obj.init()
		
	if callable(getattr(obj, 'run', None)):
		while True:
			obj.run()
