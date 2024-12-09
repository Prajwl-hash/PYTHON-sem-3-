<<<<<<< HEAD
import random
questions = [
    ("What is the capital of France?","paris"),
    ("What is 2 + 2 ","4"),
    ("What is the color of the sky?","Blue"),
]

random.shuffle(questions)


with open('quiz.txt','w') as file:
    for question,answer in questions:
=======
import random
questions = [
    ("What is the capital of France?","paris"),
    ("What is 2 + 2 ","4"),
    ("What is the color of the sky?","Blue"),
]

random.shuffle(questions)


with open('quiz.txt','w') as file:
    for question,answer in questions:
>>>>>>> c965dbf5152de176c2dbd9448cc71dbd01538425
        file.write(f"{question} (Answer :{answer})\n")