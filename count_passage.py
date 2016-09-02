#count = {}
#for w in open('romeo.txt').read().split():
 #   if w in count:
  #      count[w] += 1
   # else:
    #    count[w] = 1
#for word, times in count.items():
 #   print "%s was found %d times" % (word, times)
    
    
from collections import Counter
yourtext = open('hamlet.txt').read().split()
print Counter(yourtext).most_common(15)
