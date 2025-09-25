import re
def validname(name):
    return bool(re.fullmatch(r"[A-Za-z ]+",name))
def valid_feedback (feed):
    return feed.strip()
def validation():
    try:
        name=input("enter the name :")
        if not name:
            raise ValueError("Name cannot be empty.")
        if not validname(name):
            raise ValueError("A Name doesnot have a number")
        user_feedback=input("enter your feedback:")
        if not valid_feedback(user_feedback):
            raise ValueError("Feedback cannot be empty.")
        print(f"Successfully added a feedback.Thank You {name} for your this feedback {user_feedback}")

    except ValueError as VE:
        print(f"{VE}")
    finally:
        print("Successfully finished a review")
validation()