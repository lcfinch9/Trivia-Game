#### ---- SETUP ---- ####

## -- Libraries -- ##

import requests
import random
import base64
import pp

## -- URL parts -- ##

BASE_URL = "https://opentdb.com/api.php"
QUESTION_COUNT = 5

category_codes = {
    "History": "23",
    "Science and nature": "17",
    "Computers": "18",
    "Music": "12",
    "Books": "10"
}

#### ---- QUESTION REQUEST ---- ####

## -- Category display -- ##

print("--- TRIVIA TIME ---")
print("Choose a category:")
categories = list(category_codes.keys())
for i in range(len(categories)):
    print(str(i) + ": " + categories[i])

## -- Category input -- ##

category_index = int(input())
category_name = categories[category_index]
category_code = category_codes[category_name]

## -- Request and response -- ##

parameters = {"encode": "base64", "amount": QUESTION_COUNT, "category": category_code}

url = BASE_URL + "/"
response = requests.get(url, params=parameters)

## -- Status check -- ##

if response.status_code != 200:
    print("Sorry, an error has occurred.")

## -- Question parsing -- ##

else:
    body = response.json()
    question_list = body["results"]

#### ---- TRIVIA GAME ---- ####

question_num = 1
correct = 0

for item in question_list:

    ## -- Question display -- ##

    print("\nQUESTION " + str(question_num))
    question = base64.b64decode(item["question"])
  
    print(question)
    question_num += 1

    ## -- Decode right and wrong answers -- ##

    correct_ans = base64.b64decode(item["correct_answer"])
    incorrect_ans = []
    for ans in item["incorrect_answers"]:
        conv_ans = base64.b64decode(ans)
        incorrect_ans.append(conv_ans)

    ## -- Options display -- ##

    incorrect_ans.append(correct_ans)
    random.shuffle(incorrect_ans)
    for i in range(len(incorrect_ans)):
        print(str(i) + ": " + str(incorrect_ans[i]))

    ## -- User guess -- ##

    user_ans = int(input())
    user_ans = incorrect_ans[user_ans]

    ## -- Reply -- ##

    print()
    if user_ans == correct_ans:
        print("That's right!")
        correct += 1
    else:
        print("Sorry, the correct answer was: " + str(correct_ans))

    input("Press enter to continue.")

## -- Final score -- ##

avg = correct / 5 * 100
print("\nYou got " + str(avg) + "% correct!")
