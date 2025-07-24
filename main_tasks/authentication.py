from email_validation_helper import *
def authentication(users:list,user:dict)->bool:
    username=user["username"]
    password=user["password"]
    correctNameFlag=False
    userIndex=0
    for i in range(len(users)):
        if users[i]["name"]==username:
            correctNameFlag=True
            userIndex=i
            break
    else:
        print("Incorrect username")
        return False
    if correctNameFlag:
        if users[userIndex]["password"]==password:
            print("Welcome!")
            return True
        else:
            print("Incorrect password")
            return False

def userInput()->dict:
    user={}
    user["username"] = input("Enter your username: ")
    user["password"] = input("Enter your password: ")
    
    user["email"] = input("Enter your email: ")
    if validate_email(user["email"])==False:
        raise f"invalid email"
    return user


def login(users:list,trials:int):
    for i in range(trials):
        try:
            user = userInput()
        except Exception as e:
            print(f"invalid information")
            continue
        if authentication(users=users,user=user)==True:
            users.append(user)
            break
        else:
            if i<trials-1:
                print("please try again")
    else:
        raise Exception("You have exceeded the number of trials, please try again later")

tempUsers=[{"name":"ahmed","password":"123","mail":"correctOne@gmail.com"},{"name":"osama","password":"123456","mail":"correctTwo@test.com"}]
testDict={"name":"ahmed","password":"123456","mail":"correctOne@gmail.com"}

login(users=tempUsers,trials=3)
