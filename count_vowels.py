def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in string:
        if char in vowels:
            count += 1
    
    return count


# Test the function
if __name__ == "__main__":
    test_string = "Hello"
    result = count_vowels(test_string)
    print(f"String: '{test_string}'")
    print(f"Number of vowels: {result}")
