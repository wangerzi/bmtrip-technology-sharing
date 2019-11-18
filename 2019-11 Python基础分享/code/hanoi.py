def hanoi(n, A, B, C):
	"""表示将n个碟子，从A借助B移动到C"""
	if n == 1:
		# A 通过 B 移动到 C，如果只有一个盘子，
		print("Move %s => %s"%(A, C))
	else:
		hanoi(n-1, A, C, B) # 将 A 上 N-1 个盘子，从 A 借助 C 移动到 B
		print("Move %s => %s"%(A, C)) # 将 A 上最后一个盘子，直接移动到 C
		hanoi(n-1, B, A, C) # 将 B 上 N-1 个盘子，从 B 借助 A 移动到 C

hanoi(64, "A塔", "B塔", "C塔")
