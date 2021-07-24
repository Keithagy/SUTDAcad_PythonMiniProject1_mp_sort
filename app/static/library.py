from org.transcrypt.stubs.browser import *
import random

array = []

def gen_random_int(number, seed):
	random.seed(seed)
	result = list(range(number))
	random.shuffle(result)
	return result

def generate():
	global array

	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the global variable array
	array = gen_random_int(number, seed)
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.

	array_str = str(array)[1:-1] + "."

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the global variable array and 
			copy it to a new list
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	global array
	toSort = array[:]
	insertion_sort(toSort)
	array_str = str(toSort)[1:-1] + '.'
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	arr = value.split(',')
	arr_num = []

	for ele in arr:
		arr_num.append(int(ele))

	insertion_sort(arr_num)
	array_str = str(arr_num)[1:-1]+ '.'

	document.getElementById("sorted").innerHTML = array_str


def insertion_sort(array):

    n = len(array)

    for set in range(1,n):

        for pos in range(set,0,-1):

            if array[pos] < array[pos-1]:

                array[pos], array[pos-1] = array[pos-1], array[pos]

            else:

                break

    return array


