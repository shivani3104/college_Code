def ask_yes_no_question(question):
    response = input(question + " (y/n): ").lower()
    return response == 'y'

print("Welcome to the Hospital Expert System!")
print("Please answer the following questions to determine your diagnosis.\n")

fever = ask_yes_no_question("Do you have a fever?")
cough = ask_yes_no_question("Do you have a cough?")
sore_throat = ask_yes_no_question("Do you have a sore throat?")
runny_nose = ask_yes_no_question("Do you have a runny nose?")
headache = ask_yes_no_question("Do you have a headache?")
body_aches = ask_yes_no_question("Do you have body aches?")
fatigue = ask_yes_no_question("Do you feel fatigue or weakness?")
shortness_of_breath = ask_yes_no_question("Do you experience shortness of breath?")
chest_pain = ask_yes_no_question("Do you have chest pain?")
vomiting = ask_yes_no_question("Are you experiencing vomiting or nausea?")
diarrhea = ask_yes_no_question("Do you have diarrhea?")
loss_of_taste_or_smell = ask_yes_no_question("Have you experienced loss of taste or smell?")

if fever and cough and sore_throat and runny_nose and headache and body_aches and fatigue and shortness_of_breath:
    print("You may have COVID-19. Please get tested and self-isolate.")
elif fever and cough and sore_throat and runny_nose and headache:
    print("You may have a common cold. Rest and stay hydrated.")
elif fever and cough and sore_throat and body_aches and fatigue:
    print("You may have the flu. Rest, stay hydrated, and consider antiviral medication.")
elif fever and headache and vomiting and diarrhea:
    print("You may have food poisoning. Drink plenty of fluids and rest.")
elif chest_pain and shortness_of_breath:
    print("You may be experiencing a heart attack. Seek emergency medical attention immediately.")
elif fever and cough and shortness_of_breath:
    print("You may have pneumonia. Seek medical attention promptly.")
elif headache and vomiting and loss_of_taste_or_smell:
    print("You may have a sinus infection. Consult a doctor for treatment.")
else:
    print("Your symptoms are not specific enough for a diagnosis. Please consult a doctor.")
