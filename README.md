## Day 84 - Assignment: Tic Tac Toe

## My Notes

1/2/26

This one really got me thinking. First, I was not going to post to my portfolio website. Second, should I use an array or a dictionary. 3rd, how to make it displa and how to select the location. Anyway, to get started I just copied over one of my previous text based programs.

1/3/26

I started the day with...

1.  Cleaning up the files (not needed) ✅

2.  Updating main.py to the most basic needs (and installing modules as nededed) ✅

3.  Get overview for project ✅

    Using what you have learnt about Python programming, you will build a text-based version of the Tic Tac Toe game. The game should be playable in the command line just like the Blackjack game we created on Day 11. It should be a 2-player game, where one person is "X" and the other plays "O".

    This is a simple demonstration of how the game works:
    https://www.google.com/search?q=tic+tac+toe

    You can choose how you want your game to look. The simplest is to create a game board using "|" and "_" symbols. But the design is up to you.

    If you have more time, you can challenge yourself to build an AI player to play the game with you.

4.  Setup Git and Git Hub (to save for later)

    Removed old virtual environment → rm -rf venv
    Removed the old git tracking → rm -rf .git
    Initialized the virtual environment → python -m venv venv
    Activated the virtual environemtn → source venv/bin/activate
    Initlaized a new repo →
        git init
        git add .
        git commit -m "initial commit"
    Noted old Git Ignore still there → cat .gitignore
    Set branch name → git branch -M main
    Created new repo at Gig Hub → https://github.com/remonhi/Text-to-Morse-Code-Converter
    Connected to net repo → git remote add origin git@github.com:remonhi/Text-to-Morse-Code-Converter.git
    Pushed → git push -u origin main

...then, was standing by to see what would happen. Well, there seemed to be no "assessment" of this code.

Last, laid out my approach...

    1. Ask if want to play.
    2. Setup coin flip (using my weather station).
    3. Create the game board.
    4. Outline all the possible "wins"
    5. Address how to select location.
    6. Figure out how to "stategize" next move of computer.
    7. Determeine when game is won or stalemate
    8. Ask to play a new game.
