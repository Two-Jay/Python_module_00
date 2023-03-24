# * import
# --------------------------------------------------------------------------
import sys
import random

# * config
# --------------------------------------------------------------------------
sys.tracebacklimit = 0

# * global variable
# --------------------------------------------------------------------------
msg_hello = """This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
"""

# * Class UserInputManager
# --------------------------------------------------------------------------
class UserInputManager:
    def __init__(self, min, max):
        self._min = min
        self._max = max
    
    def get_input(self):
        while True:
            print(f"What's your guess between {self._min} and {self._max}?")
            sended = input(">> ")
            if self.validate_input(sended) == True:
                return sended
                     
    def validate_input(self, input):
        if input == "exit" or input.isdigit():
            return True
        else:
            print("That's not a number.")
            return False
        
# * Class AnswerJudge
# --------------------------------------------------------------------------
class AnswerJudge:
    def __init__(self, answer):
        self._answer = answer
        self._attempts = 0

    def judge_answer(self, input):
        user_input = int(input)
        self._attempts += 1
        if user_input == self._answer:
            return self.tell_correct_answer()
        else:
            return self.tell_wrong_answer(user_input)
    
    def tell_correct_answer(self):
        if self._answer == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if self._attempts == 1:
            print("Congratulations! You got it on your first try!")
        else:
            print(f"Congratulations, you've got it!\nYou won in {self._attempts} attempts!")
        return True
    
    def tell_wrong_answer(self, input):
        if input > self._answer:
            print("Too high!")
        else:
            print("Too low!")
        return False

# * GuessGame
# --------------------------------------------------------------------------
class GuessGame:
    def __init__(self, answer_min, answer_max):
        self._answer_min = answer_min
        self._answer_max = answer_max
    
    def run_guess_game(self):
        self._answer = random.randint(self._answer_min, self._answer_max)
        input_manager = UserInputManager(self._answer_min, self._answer_max)
        answer_judge = AnswerJudge(self._answer)

        while True:
            input = input_manager.get_input()
            if input == "exit":
                self.exit_game()
            if answer_judge.judge_answer(input) == True:
                break
    
    def exit_game(self):
        print("Goodbye!")
        exit()

# * main
# --------------------------------------------------------------------------
def print_Hello():
    print(msg_hello)
    game = GuessGame(1, 99)
    game.run_guess_game()

def main():
    print_Hello()

if __name__ == "__main__":
    main()