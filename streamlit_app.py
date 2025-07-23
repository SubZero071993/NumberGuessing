import random 
secret = random.randint(1, 20)
print("أنا أفكر في رقم ما بين 1 و 20، حاول تخمنه")

for attempt in range(1, 6):
    guess = int(input(f"محاولة {attempt}: "))
    if guess < secret: 
        print("أكبر من كذا")
    elif guess > secret:
        print("أصغر من كذا")
    else:
        print(f"صح عليك! الرقم هو {secret}")
        break
else:
    print(f"خسرت! الرقم كان {secret}")
