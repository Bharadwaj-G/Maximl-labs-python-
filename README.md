# Maximl-labs-python-Test

Here,
we have to take an input string S containing lowercase English alphabets and have to return the length of smallest substring with maximum number of distinct characters.

For this I have used 3 functions -
1)max_distinct_char() - to return the max number of distinct characters in  a string
2)substrings() - to return the list of substrings for a given string
3)smallestSubstrings() - to find the required smallest substring from the list of substrings

For finding the smallest substring,
I have checked the following conditions for each substring in the list of substrings:
1)the substring should be of minimum length
2)it should have max number of distinct characters

From this,Out of all the substrings in the list, the smallest one with max. number of distinct characters is found and its length is returned in the output.
