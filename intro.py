from Password_Generator import generate_senp

if __name__ == "__main__":
    question = input("Do you want a short password? (y/n) ")
if question == 'y':
    try:
       generate_senp.generate_password_simple()
    except ValueError:
        print("Error!!")
else:
    question = input("Do you want a strong password? (y/n) ")
    if question == 'y':
        try:
            generate_senp.generate_password_advanced()
        except ValueError:
            print("Error!!")
    else:
        print("You must enter a valid answer")
        exit()