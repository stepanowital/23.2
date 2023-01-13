
		# СТАНДАРТНЫЕ БИБЛИОТЕКИ

	# COUNTER

# from collections import Counter

# c = Counter('Hello')
# print(c)
# print(c.most_common(1))
# print(dict(c))
# print(c.items())

# b = Counter([1, 2, 3, 3, 4, 4, 4, 4, 5, 7, 12, 100, 100])
# print(b)
# print(b.most_common(1))
# print(dict(b))
# print(b.items())


	# DICT

# from collections import defaultdict

# d = defaultdict(lambda: 0)
# input_str = 'fasgffagasdfsafasdf'
# for item in input_str:
# 	d[item] += 1
# print(d.items())


# class Topic:
# 	def __init__(self, id, blog_id):
# 		self.id = id
# 		self.blog_id = blog_id
#
#
# topics = [Topic(1, 1), Topic(2, 1), Topic(3, 2)]
# d = defaultdict(list)
# for t in topics:
# 	d[t.blog_id].append(t)
#
# print(d)


	# TUPLE

# from collections import namedtuple
#
# Topic = namedtuple('Topic', ['id', 'blog_id'])
# print(Topic)
# topics = [Topic(1, 1), Topic(2, 1), Topic(3, 2)]
# first_topic = topics[0]
# print(first_topic.id, first_topic.blog_id)


ITERTOOLS and FUNCTOOLS - домашнее задание