#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	num = 0

	for car in text:
		if car.isalnum():
			num += 1

	return num

def get_word_length_histogram(text):
	histogramme = [0]
	for mot in text.split():
		length = get_num_letters(mot)

		if length >= len(histogramme):
			histogramme += [0]*(length - len(histogramme) + 1)
		histogramme[length] += int(length != 0)

	return histogramme

def format_histogram(histogram):
	ROW_CHAR = "*"
	numligne = 0
	affichage = ''
	alignment = len(str(len(histogram) - 1))
	for elem in histogram:
		if numligne > 0:
			affichage += f'{numligne : >{alignment}} '+ (ROW_CHAR * elem) + '\n'
		numligne += 1
	#'\n'.join([f'{numligne : >{alignment}} {ROW_CHAR * elem}' for numligne, elem in enumerate(histogram) if numligne != 0])
	return affichage

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	hauteur = max(histogram)
	resultat = ''
	for i in range(hauteur - 1, -1, -1):
		for j, elem in enumerate(histogram):
			resultat += (BLOCK_CHAR if elem >= i+ 1 else ' ') if j != 0 else ''
		resultat += '\n'
	return resultat + LINE_CHAR * len(histogram)


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
