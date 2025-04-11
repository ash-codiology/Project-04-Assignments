print(" Welcome to the Pharmacist Mad Libs by Ashfa Shakeel \n")

# User inputs
drug_name = input("Enter a medicine name: ")
body_part = input("Enter a body part: ")
adjective = input("Enter an adjective: ")
symptom = input("Enter a symptom (e.g., headache, nausea): ")
doctor_name = input("Enter a doctor's name: ")
action_verb = input("Enter an action verb (e.g., mix, swallow, shake): ")
place = input("Enter a place (e.g., hospital, pharmacy): ")
time_period = input("Enter a time period (e.g., 2 days, one week): ")

# Madlib story template
madlib = f"""
Today I visited the {place} and the pharmacist handed me a bottle of {drug_name}.
The label said: "Apply to your {body_part} twice daily for {time_period}."
I was feeling very {adjective} because of my {symptom}, but I trusted {doctor_name}'s advice.
I carefully {action_verb} the medicine and followed instructions.
By the end of {time_period}, I felt so much better!
Pharmacy magic is real! 
"""

print(madlib)
print("Made with care by Ashfa Shakeel ❤️")

