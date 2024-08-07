''' A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.
'''

t1 = ("Make a lot of money")
t2 = "buy now"
t3 = "subscribe"
t4 = "click this"

m = input("Enter your message")

if ((t1 in m) or (t2 in m) or (t3 in m) or (t4 in m)):
    print("spam detected in",m)

else:
    print("spam free")