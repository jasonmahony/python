#!/usr/bin/python

#import operator

class Package:
    def __init__(self, *args):
        self.l = int(args[0])
        self.w = int(args[1])
        self.h = int(args[2])
        self.wt = int(args[3])
    
#    def l(self, l):
#        if self.l < 0 or self.l > 350: raise Exception("Length not right") 
    
    def volume(self):
        return self.l * self.w * self.h

package = Package(2,3,4)
print package.volume()
        
    
   