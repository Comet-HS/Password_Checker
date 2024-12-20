import string

def check_common_password(password):
    with open('common_passwords.txt', 'r') as f:
        common = f.read().splitlines()
    if password in common:
        return True
    return False

def password_strength(password):
    score = 0
    upper = 0
    lower = 0 
    digit = 0
    special = 0
    length = len(password)

    for n in range(1, length):
        if any(i.isupper() for i in password):
            upper = 1
        if any(i.islower() for i in password):
            lower = 1
        if any(i.isdigit() for i in password):
            digit = 1
        if any(i in string.punctuation for i in password):
            special = 1

    characters = [upper, lower, digit, special]

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1

    score += sum(characters)

    if score < 5:
        return "Weak", score
    elif score == 5:
        return "Okay", score
    elif 5 < score < 7:
        return "Good", score
    else:
        return "Strong", score
    
def feedback(password):
    if check_common_password(password):
        return "Password was found in a common list. Score: 0/8"

    strength, score = password_strength(password)

    feedback = f"Password strength: {strength} (Score: {score}/8)\n"

    if score < 5:
        feedback += "Recommendations to strengthen password:\n"
        if len(password) <= 8:
            feedback += "- Create a longer password (At least 8 characters). \n"
        if not any(i.isupper() for i in password):
            feedback += "- Include uppercase letters.\n"
        if not any(i.islower() for i in password):
            feedback += "- Include lowercase letters.\n"
        if not any(i.isdigit() for i in password):
            feedback += "- Include numbers.\n"
        if not any(i in string.punctuation for i in password):
            feedback += "- Include special characters (@, #, $).\n"

    return feedback

def main():
    while True:
        print("'ctrl + c' to exit")
        password = input("Enter the password: ")
        print(feedback(password))

main()