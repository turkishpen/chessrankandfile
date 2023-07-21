#i got the template from here if you are wondering: https://www.javatpoint.com/python-program-to-generate-a-random-string 
import random  
import string  
def specific_string(length):  
        files = 'abcdefgh'
        ranks = '12345678'
        result = ''.join((random.choice(files)) for x in range(length))
        result2 = ''.join((random.choice(ranks)) for x in range(length))  
        print("file: ", result)  
        print("rank: ", result2)
      
specific_string(1)

#ok bai ^-^