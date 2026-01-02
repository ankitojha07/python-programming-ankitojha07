# function and If else
def greet_user(name,experience_year, language):
    if experience_year >=3 and language == "Python" or language == "py" or language == "python":
        return f"Welcom back PyDev, {name}! You're and experienced {language} developer."
    if experience_year >=3 and language == "JavaScript" or language == "js" or language == "Javascript":
        return f"Welcom back JS Dev, {name}! You're and experienced {language} developer."
    else:
        return f"Hi, {name}! Let's level up your skills."

message = greet_user("Ankit", 3, "js")
print(message)