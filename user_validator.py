import re


def name_validator(name):
    if re.match (r"^[a-zA-Z\s]{2,30}$", name):
        return True
    else:
        return False

def family_validator(family):
      if re.match(r"^[a-zA-Z\s]{2,30}$", family):
         return True
      else:
         return False

def user_validator(user):
     if re.match(r"^[a-zA-Z\s\d]{2,15}$", user):
         return True
     else:
         return False

def password_validator(password):
    if re.match(r"^[\w]{2,15}$", password):
        return True
    else:
        return False



def is_active_validator(is_active):
    if re.match(r"^[a-zA-Z\s]{2,30}$", is_active):
        return True
    else:
        return False

def age_validator(age):
    return  0 < age< 150
