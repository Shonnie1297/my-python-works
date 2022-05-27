## Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def is_anagram(s1, s2):
   if(sorted(s1)==sorted(s2)):
        print(sorted(s1) , sorted(s2))
        return True      
        return False
print(is_anagram('earth', 'heart')) 

      

