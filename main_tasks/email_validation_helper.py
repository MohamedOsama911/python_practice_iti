import re
def validate_email(email:str)->bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.fullmatch(pattern, email):
        return True
    return False


def filter_emails(emailList:list)->list:
    return list(filter(validate_email,emailList))

def get_email_domains(emailList:list)->list:
    filtered_emails=filter_emails(emailList)
    return list(map(lambda x: x.split("@")[1],filtered_emails))



