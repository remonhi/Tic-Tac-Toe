# - Yellow -  Information with a general, but relative importance
# ? Orange -  Examples, abbreviations, acronyms, or explanations
# + Green -  Key words, proper nouns, dates, symbols or mathematical formulas
# ~ Blue -  Definitions of key words, or tabular data
# ! Pink - Important, relative to a test or my career
# * Purple -  Personal interest
# // Gray - Done

# - Import modules to follow my CONVENTIONS 

import art               # - for ASCII art
import os                # - for OS commands to clear the screen
import sys               # - for system-specific parameters and functions

# - Define "global" variables and functions.

def clear_screen():
    if os.name == 'nt':  # 'nt' stands for Windows
        os.system('cls')
    else:  # For macOS and Linux (posix-based systems)
        os.system('clear')

# - Set up APIs - N/A

# - Start with my CONVENTION of introductory information  

clear_screen()
path = os.path.abspath(__file__)
day = os.path.basename(os.path.dirname(path))
module = os.path.basename(__file__)
module = module.replace(".py", "")
udemy_day = day + " - " + "Module:  " + module
udemy_day = "Tick Tack Toe"
print(art.text2art(udemy_day, font='medium'))

# - Setup APPLICATION LOGIC "layer" for business logic, routing, templates, etc. 

clear_text = input("Would you like to play Tic Tac Toe? (Y,N, Yes, No, etc.) \u2192 ")
clear_text = clear_text.strip().upper()
print(f"\nThe text to convert is \u2192 {clear_text}")

morse_text = ""
for i in clear_text:
    morse_text += morse_code[i] + " "

print(f"\nThe Morse Code is \u2192 {morse_text}")






