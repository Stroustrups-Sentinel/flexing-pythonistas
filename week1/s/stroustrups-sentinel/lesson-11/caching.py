# implementing a way of caching results for calculations

global_cache = {}

def kid(a, b):
    if (a,b) in global_cache:
        print("[i]: used cache")
        return global_cache[(a,b)]
    # c = a * b
    c = 0
    for i in range(b):
        c += a
    global_cache[(a,b)] = c
    return c

while True:
    print("[Use '0' to quit]")
    a = input("Enter value for 'a' : ")
    b = input("value for 'b' : ")
    if a == '0' or b == '0':
        print("Good Bye 👋")
        break
    print("answer is: " , kid(int(a),int(b)))
    print('-'*35)
