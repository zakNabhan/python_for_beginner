'''x = int(input("please enter an integer"))
if x < 0:
    x = 0
    print("negative changed to zero")
elif x == 0:
    print("zero")
elif x == 1:
    print("Single")
else:
    print("more")'''

#measure some strings
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


def ask_ok(retries=4, reminder='Please try again!'):
    prompt = "start!"
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
ask_ok()