		# СИНТАКСИС

# foo = lambda: 1
# print("*" * 10)
# print(foo)
# print(foo())
#
#
foo1 = lambda v: v + 1
print("*" * 10)
print(foo1)
print(foo1(1))
#
#
# foo2 = lambda *args, **kwargs: (args, kwargs)
# print("*" * 10)
# print(foo2)
# print(foo2(1, 2, var=5))


		# ЧЕМУ ЭКВИВАЛЕНТНЫ ЛЯМБДЫ
# foo1 = lambda v: v + 1

# def foo1(v):
# 	return v + 1

# print(foo1(5))


# foo2 = lambda *args, **kwargs: (args, kwargs)

# def foo2(*args, **kwargs):
# 	return (args, kwargs)

# print(foo2())


		# ГДЕ УДОБНО ИСПОЛЬЗОВАТЬ

# def mapper(func, arr):
# 	return [func(item) for item in arr]
#
#
# emails_text = 'stepanowital@mail.ru , vistepanov@kphk.kz '
# print(emails_text.split(','))
# res = mapper(lambda v: v.strip(), emails_text.split(','))
# print(res)
