def main():
    string1 = input("Enter the first string: ").strip()
    string2 = input("Enter the second string: ").strip()
    
    length1 = len(string1)
    length2 = len(string2)
    
    if length1 > length2:
        print("The first string is longer.")
    elif length2 > length1:
        print("The second string is longer.")
    else:
        print("Both strings are of equal length.")

if __name__ == "__main__":
    main()