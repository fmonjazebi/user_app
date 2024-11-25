import re


def name_validator(name):
    if re.math (r"^[a-zA-Z\s]{2,30}$", name):
        return True
    else:
        return False

def family_validator(family):
      if re.math(r"^[a-zA-Z\s]{2,30}$", family):
         return True
      else:
         return False

def user_validator(user):
     if re.math(r"^[a-zA-Z\s\d]{2,15}$", user):
         return True
     else:
         return False

def password_validator(password):
            if re.math(r"^[\w]{2,15}$", password):
                return True
            else:
                return False



def is_active_validator(is_active):
    return bool(re.match(r"^[a-zA-Z\s]{2,30}$", id))

def age_validator(age):
    return  0 < age< 150
