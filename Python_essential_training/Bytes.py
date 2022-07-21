bytes(4)
#print b'\x00\x00\x00\x00'

smileBytes = bytes(':-)', 'utf-8')
smileBytes
#print b'\xf0\x9f\x99\x84

smileBytes.decode('utf-8')
#print :-)