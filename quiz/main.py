from api_model import api
import quiz_practice as quiz
def main():
    print("\t**Welcome to Quiz game**\nBefore starting game please provide us your name")
    name = input("name:")
    print(f"""\t welcome {name}. please choose the type of quiz you want to play
        1. General knowledge
        2. animal
        3. history
        """)
    category = input("choose one:")
    api_category = assign_apicategory(category)
    print("""\t please choose the difficulty level
        -- easy or medium or hard --
        """)
    difficult = input("choose level:")
    amount = int(input("How many questions you like to play:"))
    
    quiz.game(amount,api_category,difficult)

def assign_apicategory(id):
    if id == '1':
        return 9
    elif id == '2':
        return 27
    elif id == '3':
        return 23


if __name__ == '__main__':
  main()
