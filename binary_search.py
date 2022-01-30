
def binary_search(lst: list, item: int) -> int:
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = lst[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1

    return None


my_lst = [1, 5, 7, 8, 9, 12, 15, 22, 23, 24, 30, 33, 35, 37, 42, 45]
my_guess = 42

print(binary_search(my_lst, my_guess))


