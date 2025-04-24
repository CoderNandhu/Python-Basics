nums = []

for i in range(1, 21):
    #nums.append(i)
    if i % 3 == 0 and i % 5 == 0 :
            nums.append("fizzbuzz")
    elif i % 3 == 0:
        nums.append("fizz")
    elif i % 5 == 0:
        nums.append("buzz")
    
    else:
        nums.append(i)
        
print(nums)

nums = ["fizzbuzz" if i % 3 == 0 and i % 5 == 0 
        else "fizz" if i % 3 == 0 
        else "buzz" if i % 5 == 0
        else i
        for i in range(1, 21) ]
print(nums)