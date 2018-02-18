def reverse(phrase):
	reversed_list = list(phrase[::-1])
	reversed_list.remove(".")
	reversed_phrase = ''.join(reversed_list)
	reversed_phrase= reversed_phrase +str(".")
	return reversed_phrase

print(reverse("ian is big."))