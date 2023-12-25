#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import json

# Define the data to be stored in the JSON file
data = {
    "questions": [
        {
            "question": "What is the capital of France?",
            "options": ["Madrid", "Berlin", "Paris", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
            "answer": "Leonardo da Vinci"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Venus", "Jupiter", "Saturn", "Neptune"],
            "answer": "Jupiter"
        }
    ]
}

# Save data to a JSON file named quiz_questions.json
file_name = 'quiz_questions.json'

with open(file_name, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Data has been saved to {file_name}")

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.questions = self.load_questions_from_json("quiz_questions.json")
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=('Arial', 14))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        self.create_option_buttons()

        self.score_label = tk.Label(root, text="Score: 0", font=('Arial', 12))
        self.score_label.pack(pady=10)

        self.display_question()

    def load_questions_from_json(self, file_name):
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                return data.get('questions', [])
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
            return []

    def create_option_buttons(self):
        for i in range(4):
            button = tk.Button(self.root, text="", font=('Arial', 12), width=20,
                               command=lambda idx=i: self.check_answer(idx))
            button.pack(pady=5)
            self.option_buttons.append(button)

    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data['question'])

            options = question_data['options']
            for i in range(4):
                self.option_buttons[i].config(text=options[i])

    def check_answer(self, idx):
        selected_answer = self.questions[self.current_question]['options'][idx]
        correct_answer = self.questions[self.current_question]['answer']

        if selected_answer == correct_answer:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

        self.current_question += 1
        self.display_question()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quiz App")

    quiz = QuizApp(root)

    root.mainloop()


# In[ ]:




