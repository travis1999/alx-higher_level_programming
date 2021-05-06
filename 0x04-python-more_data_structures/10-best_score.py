#!/usr/bin/python3


def best_score(a_dictionary):
	scores = list(a_dictionary.values())
	highest_score = max(scores)
	keys = list(a_dictionary.keys())
	return keys[scores.index(highest_score)]
