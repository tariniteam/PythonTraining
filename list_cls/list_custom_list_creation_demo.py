class slist(list):
    @property
    def length(self):
        return len(self)
    
lst = slist(['a','b','c'])
print(f"Length of list is: {lst.length}")    
