# run this in python3
# MVP: Just go through like 10 Korean words in a given round
# Eventually we'll want a system that remembers the past and knows which words are hard and easy etc

def main():
    point_total = 0
    questions_list = []
    vocabulary_words = {"일부러":"purposefully", "심오한":"profound", '갈색':'brown color', '승객':'passenger', '휴전':'truce'}
    get_questions(questions_list, vocabulary_words)

    for english, korean in questions_list:
        user_answer = input(question_formatting(english))

        if user_answer == korean:
            point_total += 1
            print("정답입니다!")
        else:
            print("That's not correct! The answer was " + korean)

def get_questions(questions_list, vocabulary_words):
    for korean, english in vocabulary_words.items():
        questions_list.append((english, korean))

def question_formatting(text):
    return "How do you say {0} in Korean? ".format(text) 

if __name__ == '__main__':
    main()