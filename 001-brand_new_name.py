import random

def main():
    print("Welcome to Brand New Name Generator")
    first_name = input("Enter Your name: ").lower()
    last_name = input("Enter you last name: ").lower()
    city = input("Enter your city: ").lower()
    zip_code = str(random.randint(6000,7000))
    
    arg_params = [ first_name, last_name, city, zip_code ]
    print("Full name: {} {}, city: {}, Zipcode: {}".format(first_name, last_name, city, zip_code))
    print(f"Full name: {first_name} {last_name}, City: {city}, ZipCode: {zip_code}")
    print("Full Name: {} {}, City: {}, Zipcode: {}.".format(*arg_params))
    
    brand_new_name = "{}{}@{}{}".format(first_name, last_name[:2], city[1], zip_code[0:2])
    
    print(f"Your Brand New Name is: {brand_new_name}")
    

if __name__ == "__main__":
    main()