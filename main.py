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
    def __init__(self):
        pass
    
    def printSplashScreen(self):
        print(r""" WELCOME TO....
                 _                                             
                | |                                            
                | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
                | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                | | | | (_| | | | | (_| | | | | | | (_| | | | |
                |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                    __/ |                      
                                   |___/                       
    """)
        while True:
            print("########## ESC to quit ####### Press any key to continue ##########")
            key = self.__get_key()
            if key == "\x1b": #ESC
                print("Quitting game!")
                sys.exit()
            else:
                break
    def obtainWordLength(self):
        try:
            self.wordLen = int(input("What is the desired length of your word?: "))
            if self.wordLen <= 3:
                print("The word must at least of four letters! Try again")
                self.obtainWordLength()
        except Exception as  e:
            print(e)
    
    
    def startMainGame(self):
        self.__api_call_for_word()
        self.__set_up_gallows()
        
    
    def __get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    def __api_call_for_word(self):
        wordLen = self.wordLen
        apiUrl = f"https://random-word-api.herokuapp.com/word?length={wordLen}"
        try:
            response = requests.get(apiUrl)
            if response.status_code == 200:
                self.word2guess = response.json()[0]
        except Exception as e:
            print(e)
        
if __name__ == "__main__":
    
    game = Game()
    game.printSplashScreen()
    game.obtainWordLength()
    game.startMainGame()

