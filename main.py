#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 17:54:12 2025

@author: arjun-raf
"""
import sys
import requests
import termios
import tty



class Game:
    lives = 6
    wordLen = 0
    word2guess = ""
    progress = ""
    past_guesses = []
    HANGMAN_PICS = [
                    """
                      +---+
                      |   |
                          |
                          |
                          |
                          |
                    =========
                    """,
                    """
                      +---+
                      |   |
                      O   |
                          |
                          |
                          |
                    =========
                    """,
                    """
                      +---+
                      |   |
                      O   |
                      |   |
                          |
                          |
                    =========
                    """,
                    """
                      +---+
                      |   |
                      O   |
                     /|   |
                          |
                          |
                    =========
                    """,
                    """
                      +---+
                      |   |
                      O   |
                     /|\\  |
                          |
                          |
                    =========
                    """,
                    """
                      +---+
                      |   |
                      O   |
                     /|\\  |
                     /    |
                          |
                    =========
                    """,
                    """
                      +---+
                      |   |
                      O   |
                     /|\\  |
                     / \\  |
                          |
                    =========
                    """
                    ]
    def __init__(self):
        pass
    
    def printSplashScreen(self):
                print(r"""
 _    _      _                                 
| |  | |    | |                                
| |  | | ___| | ___ ___  _ __ ___   ___        
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \       
\  /\  /  __/ | (_| (_) | | | | | |  __/       
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|       
                                               
                                               
 _____                                         
|_   _|                                        
  | | ___                                      
  | |/ _ \                                     
  | | (_) |                                    
  \_/\___/                                     
                                               
                                               
 _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                                                                  
    """)
        # while True:
        #     print("########## ESC to quit ####### Press any key to continue ##########")
        #     key = self.__get_key()
        #     if key == "\x1b":   # ESC
        #         print("Quitting game!")
        #         sys.exit()
        #     elif key == "\n":   # ENTER
        #         print("Starting game...")
        #         break
    def obtainWordLength(self):
        try:
            self.wordLen = int(input("What is the desired length of your word?: "))
            if self.wordLen <= 3:
                print("The word must be at least of four letters! Try again")
                self.obtainWordLength()
        except Exception as  e:
            print(e)
    
    
    def startMainGame(self):
        self.__api_call_for_word()
        self.progress = ["_"]*len(self.word2guess)
        print(f"The word has been chosen. You have {self.lives} lives left")
        self.__set_up_gallows()
        guessNum = 0
        while(self.lives>0):
            print("PAST GUESSES: ")
            print(self.past_guesses)
            guess = input(f"What is your guess #{guessNum}? ").upper()
            self.past_guesses.append(guess)
            if guess in list(self.word2guess):
                
                print("Correct!")
                #print the filled blanks
                for i,letter in enumerate(self.word2guess):
                    if letter == guess:
                        self.progress[i] = guess
                
            else:
                print("Incorrect!")
                self.lives -= 1
                self.draw_hangman()
                
            if"".join(self.progress) == (self.word2guess):
                print("CONGRATULATIONS! You have won an AUDI car")
                sys.exit()
            else:    
                print(" ".join(self.progress))
                guessNum += 1
        print(f"You are dead! The word was {self.word2guess}")
            
    
    
    def __get_key(self):
        if not sys.stdin.isatty():
            # Fallback: if not a real terminal, just use input()
            return input("Press a key: ")[0]
    
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)  # reads one character instantly
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    def __api_call_for_word(self):
        wordLen = self.wordLen
        apiUrl = f"https://random-word-api.herokuapp.com/word?length={wordLen}"
        try:
            response = requests.get(apiUrl)
            if response.status_code == 200:
                self.word2guess = response.json()[0].upper()
        except Exception as e:
            print(e)
            self.word2guess = "COCONUT"
        
    def __set_up_gallows(self):
        self.draw_hangman()
        
        
    
    def draw_hangman(self):
        lives = self.lives
        if (lives==6):
            print(self.HANGMAN_PICS[0])
        elif (lives==5):
            print(self.HANGMAN_PICS[1])
        elif (lives==4):
            print(self.HANGMAN_PICS[2])
        elif (lives==3):
            print(self.HANGMAN_PICS[3])
        elif (lives==2):
            print(self.HANGMAN_PICS[4])
        elif (lives==1):
            print(self.HANGMAN_PICS[5])
        elif (lives==0):
            print(self.HANGMAN_PICS[6])
    
if __name__ == "__main__":
    
    game = Game()
    game.printSplashScreen()
    game.obtainWordLength()
    game.startMainGame()

