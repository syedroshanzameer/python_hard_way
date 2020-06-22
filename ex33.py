

def whle_loop(num,increament):
    i = 0 
    numbers = []

    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increament
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("THe numbers: ")

    for num in numbers:
        print(num)


whle_loop(20,5)