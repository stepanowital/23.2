from audioop import reverse  # FILTER

# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# res = filter(lambda x: x > 4, arr)  # на данном этапе обращения к данным не происходит
# print(res)
# print(iter(res))
# print(list(res))


		# MAP

# emails_text = 'stepanowital@mail.ru , vistepanov@kphk.kz '
# res = map(lambda x: x.strip(), emails_text.split(','))  # на данном этапе обращения к данным не происходит
# print(res)
# print(iter(res))
# print(list(res))
# print(list(map(lambda x: x.upper(), ['sentence', 'fragment'])))


		# ENUMERATE

# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# it = enumerate(arr)
# print(it)
# print(iter(it))
# print(list(it))

# for index, item in enumerate(arr):
# 	print(index, item)

# найти позиции переносов в строке
# text = '''hello
# world
# мир
# труд
# май'''
#
# for pos, character in enumerate(text):
# 	if character == '\n':
# 		print(f'Позиция знака переноса находится на {pos} знаке.')


		# ZIP

# ids = [10, 11, 12, 13, 14, 15, 16, 17, 18]
# names = ['Антон', 'Сергей', 'Пирог', 'Жнец']
#
# res = zip(ids, names)
# print(res)
# print(iter(res))
# print(list(res))
#
# # заменяем enumerate
# res = zip(range(len(ids)), names)
# print(list(res))


		# SORTED

# a = [5, 3, 2, 1, 7, 4, 6]
# res = sorted(a, reverse=True)
# print(res)

# users = [(10, 'Александр'), (9, 'Егор'), (8, 'Женя')]
# res = sorted(users, key=lambda v: v[0], reverse=False)
#
# print(dict(res), iter(res))
# d = dict(res)
# for key, value in d.items():
# 	print(key, value)

# sorted, min, max, set, dict, list, len


		# Без функционального программирования

	# filter
arr = [1, 2, 3, 4, 5]
# res = filter(lambda x: x > 3, arr)
# print(list(res))

# val_filter = lambda x: x > 3
# print(val_filter(4))
#
#
# def new_filter(val_filter, arr):
# 	for item in arr:
# 		if val_filter(item):
# 			yield item
#
#
# res = new_filter(val_filter, arr)
# print(list(res))


	# MAP

# def new_map(mapper, arr):
# 	for item in arr:
# 		yield mapper(item)
#
#
# res = new_map(lambda x: x ** 2, arr)
# print(list(res))


	# ZIP

# def new_zip(*args):
# 	min_lenght = min(map(len, args))
# 	print(min_lenght)
# 	for i in range(min_lenght):
# 		yield tuple(arr[i] for arr in args)
#
#
# res = new_zip([1, 2, 3], ['a', 'b'], ['c', 'g'])
# print(res, list(res))


		# СОЕДИНЯЕМ ВСЁ ВМЕСТЕ

class User:
	def __init__(self, id, name, age):
		self.id = id
		self.name = name
		self.age = age

users = [User(1, 'Иван', 39), User(2, 'Сергей', 35), User(3, 'Жорж', 25), User(4, 'Иван', 20), User(5, 'Женя', 40)]

# res = filter(lambda user: user.age > 30, users)
# res = map(lambda user: user.id, res)
# res = set(res)
# res = sorted(res, reverse=False)
# print(res)


		# ДОБАВЛЯЕМ ГЕНЕРАТОРЫ. ПИШЕМ СИСТЕМУ РАССЫЛОК

def send_message(msg, user_ids):
	print(f'Message "{msg}" has been sent to users: {user_ids}')
	return True


chunk_size = 2


def chunker(iter_obj):
	buf = []
	for item in iter_obj:
		buf.append(item)
		if len(buf) >= chunk_size:
			yield buf
			buf = []
	if buf:
		yield buf


res = filter(lambda user: user.age > 30, users)
res = map(lambda user: user.id, res)
chunks = chunker(res)
res = map(lambda user_ids: send_message('Hello', user_ids), chunks)
print(list(res))













