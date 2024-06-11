from Questions import Question

questions_prompts = ["what colors are apple \n a) Red/Green\n b) Orange \n c) Yellow \n\n",
                     "what colors are bananas \n a) Teal \n b) Magenta \n c) Yellow \n\n ",
                     "what colors are strawberries \n a) Yellow \n b) Red \n c) Blue \n\n "

                     ]

questions = [Question(questions_prompts[0], "a"),
             Question(questions_prompts[1], "c"),
             Question(questions_prompts[2], "b")
             ]


def runTest(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if question.answer == answer:
            score += 1
    print("you got" + str(score) + "/" + str(len(questions)) + "Correct")


runTest(questions)