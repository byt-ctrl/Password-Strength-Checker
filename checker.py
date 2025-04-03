# WRITTEN BY OM [byt-ctrl]
# Password Strength Checker

import re

def execute_password_strength(pswd):
    score=0
    suggestions=[]

    # Length: 3 points for characters beyond 13, 2 points for those between 8 and 12
    

    if len(pswd)>=13:
        score+=3
    elif len(pswd)>=8:
        score+=2
    else:
        suggestions.append("Increase password length to at least 8 characters.")

    #The uppercase letter generates 1 point value from its weight parameter.
    if re.search(r"[A-Z]",pswd):
        score+=1
    else:
        suggestions.append("Add at least one Uppercase Letter.")

    #The number 1 signifies the weight value of the lowercase letter.
    if re.search(r"[a-z]",pswd):
        score+=1
    else:
        suggestions.append("Add At least onr lowercase letter.")

    # Weight variable determines the value of 1 point.
    if re.search(r"[$%^&*(),.?\":{}|<>!@#]",pswd):
        score+=2
    else:
        suggestions.append("Add at least one special character  (!, @, #, $, etc.)")
    



    # Classification of Strengths by Score
    if score>=8:
        strength="Strong"
    elif score>=5:
        strength="Medium"
    else:
        strength="Weak"     
   
     # Final Assessment and Output Recommendations
    if suggestions:
        print()
        result=f"Your Password is classified as {strength}\n\nSuggestions to improve :\n" + "\n".join(suggestions)
    else:
        result=f"Your password is classified as: {strength}\nPassword is strong and secure!"

    return result



if __name__=="__main__":
    user_input=input("Kindly Provide a password to verify its strength -->  ")
    strength_result=execute_password_strength(user_input)

   

print(strength_result)

# END
