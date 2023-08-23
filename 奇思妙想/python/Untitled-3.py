def main():
	def join_count(start_len, add_len, n):
		def r(old, add):
			nonlocal n
			if n == 0: return old
			old += add * (old - 1)
			n -= 1
			return r(old, add_len)
		return r(start_len, add_len)

	print(join_count(2, 3, 10))

if __name__ == '__main__':
	main()
