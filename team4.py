####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'CatsdaBest' # Only 10 chars displayed.
strategy_name = 'Collude more than Betray'
strategy_description = 'Collude 70% of the time and betray 30% of the time, only after the other person betrays'
    
import random
    
def move(my_history, their_history, my_score, their_score, result):
    return 'c'

    if 'b' in their_history:
        return 'b'
    else:
        if random.random():
            return 'b'
        else:
            return 'c'
            
    if move(my_history='',
            their_history='',
            my_score=0,
            their_score=0,
            result='c'):

        real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False
            