import tkinter as tk

def main():
    # list of Harvard classes in the quiz
    # how do we implement the humanities stem esque?? #from the email
    classes = [
        "CS50",
        "Gov10",
        "Hum10",
        "Expos 20",
        "Ec10",
        "Math55",
        "LS1A/B",
        "Happiness",
        "Biotech Ethics",
        "Stat110"
    ]

    # start every class at 0 points
    scores = {}
    for course in classes:
        scores[course] = 0

    # each question has:
    # question text
    # 4 answer choices
    # a mapping from each choice to the class/classes that get a point
    questions = [
        {
            "question": "1. What's your dream trip?",
            "choices": {
                "a": "Explore hıstorıc landmarks ın Ancient Rome",
                "b": "Leısure by the costsıde on Lake Como, Italy",
                "c": "Dancıng away the streets of Cartagena, Colombıa",
                "d": "Adventurous explorıng on a safarı ın Kenya"
            },
            "points": {
                "a": ["CS50", "Math55"],
                "b": ["Gov10", "Ec10"],
                "c": ["Hum10", "Happiness"],
                "d": ["Expos 20", "Biotech Ethics"]
            }
        },
        {
            "question": "2. Which skill do you value most?",
            "choices": {
                "a": "Problem-solving",
                "b": "Persuasion",
                "c": "Communication",
                "d": "Data analysis"
            },
            "points": {
                "a": ["CS50", "Math55", "LS1A/B"],
                "b": ["Gov10", "Ec10", "Biotech Ethics"],
                "c": ["Hum10", "Expos 20", "Happiness"],
                "d": ["Stat110"]
            }
        },
        {
            "question": "3. Which weekend plan sounds best?",
            "choices": {
                "a": "Going to an escape room",
                "b": "Watching an election",
                "c": "Reading by the Charles",
                "d": "Walking your dog"
            },
            "points": {
                "a": ["CS50", "Math55", "Stat110"],
                "b": ["Gov10", "Ec10"],
                "c": ["Hum10", "Expos 20", "Biotech Ethics"],
                "d": ["Happiness", "LS1A/B"]
            }
        },
        {
            "question": "4. When facing a tough question, what do you usually do first?",
            "choices": {
                "a": "Break it into logical steps",
                "b": "Think about its effect on people and systems",
                "c": "Think about its deeper meaning",
                "d": "Look for evidence or patterns"
            },
            "points": {
                "a": ["CS50", "Math55"],
                "b": ["Gov10", "Ec10", "Biotech Ethics"],
                "c": ["Hum10", "Expos 20", "Happiness"],
                "d": ["Stat110", "LS1A/B"]
            }
        },
        {
            "question": "5. What animal represents you",
            "choices": {
                "a": "An owl",
                "b": "A jaguar",
                "c": "A bunny",
                "d": "A snake"
            },
            "points": {
                "a": ["CS50", "Math55"],
                "b": ["Gov10", "Ec10"],
                "c": ["Hum10", "Expos 20", "Happiness", "Biotech Ethics"],
                "d": ["LS1A/B", "Stat110"]
            }
        },
        {
            "question": "6. What are your friends most likely to ask you for help with?",
            "choices": {
                "a": "Solving a relationship issue",
                "b": "Justifying getting late to class",
                "c": "Sending a breakup message",
                "d": "Regaining motivation for a task"
            },
            "points": {
                "a": ["CS50"],
                "b": ["Gov10", "Ec10", "Happiness"],
                "c": ["Expos 20", "Hum10", "Biotech Ethics"],
                "d": ["Math55", "LS1A/B", "Stat110"]
            }
        },
        {
            "question": "7. Which activity are you most drawn to?",
            "choices": {
                "a": "Baking cookies",
                "b": "Drum circle",
                "c": "Birdwatching",
                "d": "Hurdle jumping"
            },
            "points": {
                "a": ["CS50", "Math55"],
                "b": ["Gov10", "Ec10"],
                "c": ["Hum10", "Expos 20", "Happiness", "Biotech Ethics"],
                "d": ["LS1A/B", "Stat110"]
            }
        },
        {
            "question": "8. What lounge chair are you?",
            "choices": {
                "a": "spinning desk chair",
                "b": "bean bag",
                "c": "sofa with a leg chair",
                "d": "the grass."
            },
            "points": {
                "a": ["CS50", "Math55"],
                "b": ["Gov10", "Ec10", "Biotech Ethics"],
                "c": ["Hum10", "Expos 20", "Happiness"],
                "d": ["LS1A/B", "Stat110"]
            }
        },
        {
            "question": "9. What gen z saying are you?",
            "choices": {
                "a": "As you should.",
                "b": "They ate that",
                "c": "Chat, Is that rizz?",
                "d": "Im just a girl."
            },
            "points": {
                "a": ["CS50", "Math55"],
                "b": ["Gov10", "Ec10", "Biotech Ethics", "Happiness"],
                "c": ["Hum10", "Expos 20"],
                "d": ["LS1A/B", "Stat110"]
            }
        },
        {
            "question": "10. What app are you?",
            "choices": {
                "a": "Youtube shorts",
                "b": "Sidechat",
                "c": "Letterbox",
                "d": "Strava"
            },
            "points": {
                "a": ["CS50", "Math55"],
                "b": ["Gov10", "Ec10", "Biotech Ethics"],
                "c": ["Hum10", "Expos 20", "Happiness"],
                "d": ["LS1A/B", "Stat110"]
            }
        }
    ]

    current_question = 0 # keeps track of which question the user is currently on

    def show_question():
        #get the current question dictionary
        q = questions[current_question]

        #change the label to show the current question
        question_label.config(text=q["question"])

        #change each button to show the current answer choices
        button_a.config(["choices"]["a"])
        button_b.config(["choices"]["b"])
        button_c.config(["choices"]["c"])
        button_d.config(["choices"]["d"])

    def choose_answer(answer): #ASK
        nonlocal current_question

        #add one point to every class thats like connected to the answer clicked
        for course in questions[corrent_question["points"][answer]]:
            scores[course] += 1

    #move to the next question
        current_question += 1

    #if there arew more questions show the next one
    if current_question < len(questions):
        show_question()
    else:
        show_results() # get these checked in office hours

def show_results():
    #find the highest score
    highest_score = max(scores.values())
    
    print("Welcome to the Harvard Class Personality Quiz!")
    print("Answer each question by typing a, b, c, or d.")
    print()

    # ask each question
    # for q in questions:
        # print(q["question"])
        # for letter in ["a", "b", "c", "d"]:
            # print(letter + ")", q["choices"][letter])

        button = tk.Button(...).lower().strip() # THIS IS FOR THE UI
        # so we make a button rather than a, b, c,d 

        # keep asking until the user gives valid input
        while answer not in ["a", "b", "c", "d"]:
            print("Please enter only a, b, c, or d.")
            answer = input("Your answer: ").lower().strip()

        # add 1 point to every class tied to that answer
        for course in q["points"][answer]:
            scores[course] += 1

        print()

    # find the highest score
    # highest_score = max(scores.values())

       # find all classes that have the highest score
    # (there might be more than one if there is a tie)
    winners = []
    for course in scores:  # loop through each class in the dictionary
        if scores[course] == highest_score:
            winners.append(course)  # add it to winners if it matches the max score

    # print final result
    # print("YOUR RESULT!!!")

    # if only one winner, print it normally
    if len(winners) == 1:
        print("You are most like:", winners[0])
    else:
        # if multiple winners, print all of them
        print("You are a mix of these Harvard classes:")
        for winner in winners:
            print("-", winner)

    print()
    # print("PERSONALITY REPORT!!!")

    # loop through each class again to show scores and percentages
    for course in scores:
        # convert score (out of 10) into a percentage
        percentage = (scores[course] / 10) * 100

        # print both the raw score and the percentage (rounded to whole number)
        print(f"{course}: {scores[course]}/10 ({percentage:.0f}%)")


main()
