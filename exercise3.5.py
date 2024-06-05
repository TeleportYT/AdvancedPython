import string


class UsernameContainsIllegalCharacter(Exception):
    pass


class UsernameTooShort(Exception):
    pass


class UsernameTooLong(Exception):
    pass


class PasswordMissingCharacter(Exception):
    def __init__(self, message):
        self._message = 'The password is missing a character' + message

    def __str__(self):
        return self._message



class PasswordTooShort(Exception):
    pass


class PasswordTooLong(Exception):
    pass


class PasswordMissingUpperCase(PasswordMissingCharacter):
    def __init__(self):
        super().__init__(' (Uppercase)')


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __init__(self):
        super().__init__(' (Lowercase)')


class PasswordMissingDigit(PasswordMissingCharacter):
    def __init__(self):
        super().__init__(' (Digit)')


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __init__(self):
        super().__init__(' (Special)')


def check_input(username, password):
    usernameAllowed = set(string.ascii_letters + string.digits + '_')
    char = None
    for c in username:
        if c not in usernameAllowed:
            char = c
            print(char)
            break

    if char is not None:
        raise UsernameContainsIllegalCharacter(f"Username contains illegal character {char} in {username.find(char)} ")
    elif len(username) < 3:
        raise UsernameTooShort("Username should've be at least 3 characters long")
    elif len(username) > 16:
        raise UsernameTooLong("Username should've be maximum 16 characters long")

    if not any(p in password for p in string.punctuation):
        print("hi")
        raise PasswordMissingSpecial()
    elif not any(p in password for p in string.ascii_uppercase):
        raise PasswordMissingUpperCase()
    elif not any(p in password for p in string.ascii_lowercase):
        raise PasswordMissingLowercase()
    elif not any(p in password for p in string.digits):
        raise PasswordMissingDigit()
    elif len(password) < 8:
        raise PasswordTooShort("Password should've be at least 8 characters long")
    elif len(password) > 40:
        raise PasswordTooLong("Password should've be maximum 40 characters long")
    print('OK')


def __main__():
    while (True):
        try:
            check_input(input("\nPlease Enter Username:\n"), input("\nPlease Enter Password:\n"))
            break
        except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong) as nameError:
            print(nameError)
        except (PasswordMissingCharacter, PasswordTooShort, PasswordTooLong) as passError:
            print(passError.__str__())
        print("Try again")


if __name__ == '__main__':
    __main__()
