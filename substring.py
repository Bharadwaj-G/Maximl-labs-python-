#max_sistinct_char() -  function to return the max distinct characters in a string
def max_distinct_char(str): 
	distinct_char = set(str)
	max_distinct_char = len(distinct_char)	
	return max_distinct_char

#substrings() - function to return all the substrings as a list
def substrings(string,n):
	l1 = [] 
	for i in range(n): 
		for j in range(i+1,n+1): 
			substring = string[i:j] 
			l1.append(substring)
	return(l1)

#smallestSubstring()  -  function to return the smallest substring with max distinct characters
def smallestSubstring(string): 
	n = len(string)	 
	max_distinct = max_distinct_char(string)    
	min_length = n	 
	substring_list = substrings(string,n)
	for i in range(0,len(substring_list)):
		length = len(substring_list[i]) 
		distinct_char = max_distinct_char(substring_list[i])           #to find distinct characters in substring
		if (length < min_length and max_distinct == distinct_char): 
			min_length = length 
	return min_length

if __name__ == "__main__":  
	string = input()
	l = smallestSubstring(string); 
	print(l) 

