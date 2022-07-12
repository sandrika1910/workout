#def is_palindrome(word,lst1,lst2,lst3):
#    if len(word) % 2 == 1:
#        length = len(word) + 1
#        length /= 2
#        length=int(length)
#        middle_word=word[length-1]
#        for x in word:
#            if x == middle_word:
#                break
#            lst1.append(x)
#        for i in word:
#            lst2.append(i)    
#        lst2.reverse()
#        #print(lst1)
#        for x in reversed(word):
#           if x == middle_word:
#               break
#           lst3.append(x)   
#    
#        if lst1 == lst3:
#            return True
#        else:
#            return False
# 
#    else:
#        reversedWord = word[::-1]
#        for x in word:
#            lst1.append(x)
#        for i in reversedWord:
#            lst3.append(i)
#        print(reversedWord)
#        if lst1 == lst3:
#            return True
#        else:
#            return False 
#print(is_palindrome('haah',[],[],[]))

def is_polindrome(word):
    if len(word) == 0:
        return True
    elif word == word[::-1]:
        return True
    else:
        return False
    
print(is_polindrome('asa'))