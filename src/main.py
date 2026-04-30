from operations import *

def menu():
    print("\n--- String Toolkit ---")
    print("1. Reverse Text")
    print("2. Count Vowels")
    print("3. Replace Vowels with #")
    print("4. Check Palindrome")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "5":
            print("Goodbye!")
            break

        text = input("Enter your text: ")

        if choice == "1":
            print("Reversed:", reverse_text(text))

        elif choice == "2":
            print("Vowel count:", count_vowels(text))

        elif choice == "3":
            print("Modified:", replace_vowels(text))

        elif choice == "4":
            if is_palindrome(text):
                print("Yes, it's a palindrome!")
            else:
                print("No, it's not.")

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()