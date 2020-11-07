from collections import defaultdict 

def countDistinctEle(string):
    return len(set(string)) 

def smallestSubString(string): 
	
	n = len(string) 
	
	dist_count = countDistinctEle(string)
	
	count_map = defaultdict(lambda: 0) 
	count = 0
	start = 0
	min_len = n 
	

	for j in range(n): 
		count_map[string[j]] += 1
		
		if count_map[string[j]] == 1: 
			count += 1
			
		if count == dist_count: 
			while count_map[string[start]] > 1: 
				if count_map[string[start]] > 1: 
					count_map[string[start]] -= 1
					
				start += 1
				
			len_window = j - start + 1
			
			if min_len > len_window: 
				min_len = len_window 

	return min_len
								
print("Enter string of lowercase alphabets")
string = str(input())
print(smallestSubString(string))
