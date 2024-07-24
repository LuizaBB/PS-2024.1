def educational_resources():
        print("Here are some links to inform yourself better:")

def create_account():
        database=open("database_1.txt", "a")
        print("Create account:")
        user_name=str(input("Insert your name: "))
        user_age=int(input("Insert your age: "))
        user_password=str(input("Insert your password (8 carater max.): "))
        account_information=[f"Name: {user_name}", f"\nAge: {user_age}", f"\nPassword: {user_password}\n\n"]
        print(f"Collected information: {account_information}")
        database.writelines(account_information)
        database.close()

def user_main_option(user_option):
    match user_option:
            case 0:
                create_account()
            case 1:
                educational_resources()
def main():
        main_option=int(input("Welcome:\n0: Create Account\n1: Educational Information\nOption: "))
        user_main_option(main_option)
main()