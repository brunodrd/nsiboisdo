test8 = [88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 10, 88, 32, 32, 32, 32, 32, 32, 32, 32, 32, 
         32, 32, 32, 32, 88, 32, 10, 88, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 88, 32, 10, 88, 32, 32, 
         32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 88, 32, 10, 88, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 
         32, 88, 32, 10, 88, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 88, 32, 10, 88, 32, 32, 32, 32, 32, 
         32, 32, 32, 32, 32, 32, 32, 32, 88, 32, 10, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32]
test13 = [88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 10, 
          88, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 88, 32, 10, 
          88, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 88, 32, 10, 
          88, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 88, 32, 10, 
          88, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 88, 32, 10, 
          88, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 88, 32, 10, 
          88, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 88, 32, 10, 
          88, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 88, 32, 10, 
          88, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 88, 32, 10, 
          88, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 88, 32, 10, 
          88, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 88, 32, 10, 
          88, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 88, 32, 10, 
          88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32, 88, 32]
assert carre(13) == ''.join([chr(c) for c in test13])
assert carre(8) == ''.join([chr(c) for c in test8])