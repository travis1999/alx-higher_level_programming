#!/usr/bin/python3


def roman_to_int(roman_string):
	roman = {'x': 10, 'v': 5, 'i': 1, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
	roman_digits = [roman[x] for x in roman_string]
	total = 0
	for idx, x in enumerate(roman_digits):
		try:
			if x <= roman_digits[idx + 1]:
				total += x
			if x > total:
				total = x - total
		except IndexError:
			total += x
	return total
		
