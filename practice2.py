from random import randint
from game_data import data
# f = open("D:\\msc-python\excercise\game_data.py", "r")
# print(f.read(5))
len = len(data)
count = 0
marks = 0
while count != 5:
    first_ran = randint(0,len + 1)
    second_ran = randint(0,len + 1)
    
    if (first_ran == second_ran):
        continue
    else:
        first_name = data[first_ran]['name']
        second_name = data[second_ran]['name']
        first_follower = int(data[first_ran]['follower_count'])
        second_follower = int(data[second_ran]['follower_count'])
        print ('**who has more followers??**')
        print(f'A: {first_name}  \nB: {second_name} ')
        choose = input('choose one:')
        if(choose == 'a' and first_follower > second_follower):
            marks = marks + 1
        elif(choose == 'b' and second_follower > first_follower):
            marks = marks + 1
        else:
            count = 5

print(f'Total marks = {marks}')