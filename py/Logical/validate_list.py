#validate if all numbers are > n in a list
numbers = []
is_valid = True


def validate(nums):
    value = int(input("Enter the number to validate"))
    for i in nums:
        if i < value:
            is_valid = False
            m_index = nums.index(i)
    if is_valid:
        print("All numbers fulfill validation\n")
    else:
        print("The number " + str(numbers[m_index]) + " does not comply the validation.\n")

def fill_list(lng):
    for i in range(lng):
        numbers.append(int(input("Enter a number")))
    print("validating...\n")
    validate(numbers)


fill_list(int(input("Enter the list lenght...\n")))

