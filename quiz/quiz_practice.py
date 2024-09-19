from api_model import api
def game(amount,api_category,difficult):
    api_call = api(amount,api_category,difficult)
    quiz = api_call.req_api()
    quiz_data = quiz['results']
    marks = 0
    for data in quiz_data:
        print(data['question'])
        answer = input("answer:")
        if(answer == data['correct_answer'].lower()):
            marks += 1

    print(f"You made {marks} correct answer")