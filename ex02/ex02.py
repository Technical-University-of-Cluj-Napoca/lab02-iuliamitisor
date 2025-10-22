def multiply_all(*args: int) -> int: 
    result = 1
    for num in args:
        result *= num
    return result

if __name__ == "__main__":
    input_str = input("Enter numbers: ")
    input_nums = list(map(int, input_str.split()))
    result = multiply_all(*input_nums)
    print(result)