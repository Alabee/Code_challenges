def reverse(word):
	reversed_list = list(word[::-1])
	reversed_word = ''.join(reversed_list)

	return reversed_word

print(reverse("ian"))