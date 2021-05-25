import os

MAX=512


def smallestStr(string, n):
	i, j=0,0

	check=[0 for i in range(MAX)]
	for i in range(MAX):
		check[i] = -1

	for i in range(n):


		if (check[ord(string[i])] == -1):
			check[ord(string[i])] = i

	for i in range(n):
		flag = False

		for j in range(ord(string[i])):
			if (check[j] > check[ord(string[i])]):
				flag = True
				break

		if (flag):
			break

	if (i < n):

		ch1 = (string[i])
		ch2 = chr(j)

		for i in range(n):

			if (string[i] == ch1):
				string[i] = ch2

			elif (string[i] == ch2):
				string[i] = ch1

	return "".join(string)

st = "ccad"
str=[i for i in st]
n = len(str)

print(smallestStr(str, n))
