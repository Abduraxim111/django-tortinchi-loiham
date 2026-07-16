from users.models import User

def user_validator(Username):
    try:
        User.objects.get(Username=Username)
        return True
    except:
        return None
    

def phone_validator(phone_number:str):
    if len(phone_number) !=13:
        return None
    if not phone_number.startswith('+998'):
        return None
    return True

def password_validator(password:str):
    if len(password) < 8:
        return None
    if not password.isalnum():
        return None
    return True
