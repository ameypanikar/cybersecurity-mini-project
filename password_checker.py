import re

def check_strength(pw):
    score = 0
    if len(pw) >= 8: score += 1
    if re.search(r"[A-Z]", pw): score += 1
    if re.search(r"[a-z]", pw): score += 1
    if re.search(r"[0-9]", pw): score += 1
    if re.search(r"[@$!%*#?&]", pw): score += 1

    levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    print("Password Strength:", levels[score])

pw = input("Enter a password: ")
check_strength(pw)
