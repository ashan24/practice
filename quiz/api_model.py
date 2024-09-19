import requests
class api:
    def __init__(self,amount,category,difficulty):
        self.amount = amount
        self.category = category
        self.difficulty = difficulty
       
    def req_api(self):
        amt = self.amount
        category = self.category
        diff_lvl = self.difficulty
        data = requests.get(f"https://opentdb.com/api.php?amount={amt}&category={category}&difficulty={diff_lvl}&type=boolean")
        return data.json()
