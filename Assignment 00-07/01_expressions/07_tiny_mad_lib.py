
SENTENCE_START : str = "We are not here to struggle only,we learned many things to improve my " #then add user adjective+noun+verb.

def main():
    """Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence 
    with those words!

Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the
blanks of a word template to make an entertaining story! We've provided you with the 
beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

Here's a sample run (user input is in bold italics):

Please type an adjective and press enter. tiny

Please type a noun and press enter. plant

Please type a verb and press enter. fly"""


    adjective : str = input("\033[1;3mPlease enter ADJECTIVE here then press enter to proceed.\033[0m ")
    noun : str = input("\033[1;3mPlease enter NOUN here then press enter to proceed.\033[0m ")
    verb : str = input("\033[1;3mPlease enter VERB here then press enter to proceed. \033[0m")
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

if __name__ == "__main__":
    main()