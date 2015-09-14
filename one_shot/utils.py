def handle_methods(*methods):
	def decorator(f):
		def wrapper(request, *args, **kw):
			for method in methods:
				if request.method == method.upper():
			  		func = globals()[method.lower() + "_" + f.__name__]
			  		return func(request)
			return f(request)
		return wrapper
	return decorator
