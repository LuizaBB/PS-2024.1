def educational_resources():
        print("Here are some links to inform yourself better:")

def user_main_option(user_option):
    match user_option:
            # case 0:
            #     create_account()
            # case 1:
            #     login()
            case 0:
                educational_resources()

main_option=int(input("0: Educational Resources\n1: Login\n"))
user_main_option(main_option)