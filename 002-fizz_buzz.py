
def take_input(labels):
    number = int(input(f"Enter your number to find either { ' or '.join(labels)}: "))
    
    if number < 3:
        print(f"{number} is not divisible by 3. Your number should be grather than 3.")
        take_input()
    return number
    
def find_fizz_buzz(number, labels):
    if number % 3 == 0 and number % 5 == 0:
        return labels[0]
    elif number % 3 == 0:
        return labels[1]
    elif number % 5 == 0:
        return labels[2]
    else:
        return None
    

def main():
    labels = ['fizzbuzz', 'fizz', 'buzz']
    number = take_input(labels)
    result = find_fizz_buzz(number, labels)
    print(f"Your entered number {number} is {'Nothing' if result is None else result }")
    
if __name__ == "__main__":
    main()
