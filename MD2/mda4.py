def shortestPalindrome(s):
	rev = s[::-1]
	for i in range(len(s)):
		if s.startswith(rev[i:]):
			if len(rev[:i]) == 0:
				print("this is palindrome")
				break
			else:
				print(len(rev[:i]))
				print(rev[:i] + s)
s = input()
shortestPalindrome(s)