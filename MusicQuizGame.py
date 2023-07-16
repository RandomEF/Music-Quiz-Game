import random  # We need to generate random songs and this helps us to do this
import csv  # We need to use a csv file for our authentication
import os  # Allows us to access the screen
from TypingFX import *  # Access functions to make a typing effect for print

# Globalises these variables
global points
points = 0
global streak
streak = 0
global row
row = 0
global line
line = 0
global genreSelection
genreSelection = 0
global genre
genre = 0
global userMode
userMode = False # False is guest, True is signed in
global randomFlag
randomFlag = False

# print("\033[0;37;40mTest") The beginning escape sequence changes the colour of the text


def MakeUser(user = ''):
    '''
    Creates a new user
    '''
    pwdPassed = False
    with open('Users.csv', 'a', newline='', encoding="UTF8") as file:  # This opens up the Users file in append mode
        writer = csv.writer(file)  # Assigns a writer object to an variable
        tPrint("\033[0;37;40mPlease make a new user to continue.")
        if len(user) == 0:
            user = tInput("\033[0;37;40mFirst, enter a username: ")
        else:
            tPrint(f"The chosen username is: {user}")
        while not pwdPassed:  # While the passwords do not match
            password = tInput("\033[0;37;40mPlease enter a new password: ")
            pwdCheck = tInput("Please re-enter the password: ")
            if password != pwdCheck:  # Checks if the passwords match
                tPrint("\033[0;37;40mThe passwords do not match.")
            else:
                pwdPassed = True
        global userMode
        userMode = True
        tPrint("\033[0;37;40mNew User Made.")
        time.sleep(1)
        data = ['0', user, password]  # Assigns the default score, the user and the password to a variable
        writer.writerow(data)  # Writes data to a new row in User.csv


def Authentication(bypassGuest = False):
    '''
    Checks that the user is registered and if not, registers them if they do not want to be a guest
    '''
    with open('Users.csv', newline='', encoding="UTF8") as file:  # This opens up the Users file in read mode
        reader = csv.reader(file)  # Assigns the file reader to a variable
        passed = False
        pwdPassed = False
        fails = 0
        global line
        global row
        global userMode
        while not passed:  # While not signed in
            if not bypassGuest:
                guestCheck = tInput("Would you like to sign in? (Y/N): ")
                if guestCheck[0].lower() != 'y':
                    tPrint("You have signed in as guest, where your highscores will not be saved.")
                    userMode = False
                    time.sleep(0.5)
                    return
            user = tInput("\033[0;37;40mPlease enter your username: ")
            for row in reader:
                if user == row[1]:  # Checks if the username matches the user in the row
                    passed = True
                    break
                line += 1
            if passed != True:  # If the username doesn't match any of the users
                MakeUser(user)  # Makes a new user
                pwdPassed = True
                passed = True
            while not pwdPassed:
                password = tInput("\033[0;37;40mPlease enter your password: ")
                if password == row[2]:  # Checks if the password matches the one for that user
                    pwdPassed = True
                else:
                    tPrint("\033[1;31;40mThe password was incorrect.")
                    fails += 1
                    if fails == 5:  # Gives you a hint for the password if you fail too many times
                        hint = FirstLetter(row[2])
                        pwLen = len(row[2])
                        tPrint("\033[1;35;40mPassword Hint:\nFirst Character: " + hint + "\nLength of password: " + str(pwLen))
            userMode = True
            tPrint("\033[1;32;40mAuthenication Passed.")
            time.sleep(1)
            os.system("cls||clear")  # Clears the screen


def Save():
    '''
    Saves the user's score if it is a new highscore
    '''
    global points
    fileLines = 0
    with open('Users.csv', 'r', newline='', encoding="UTF8") as file:  # This opens up the Users file in read mode
        reader = csv.reader(file)
        fileLines = list(reader)  # Makes the reader into a list
        tPrint("\033[0;37;40mSaving...")
        if int(fileLines[line][0]) < points:  # checks if the points are higher than the score in the file
            fileLines[line][0] = points
    with open('Users.csv', 'w', newline='', encoding="UTF8") as file:  # This opens up the Users file in write mode
        writer = csv.writer(file)
        writer.writerows(fileLines)  # Clears the file and writes in the edited data
    time.sleep(0.5)
    tPrint("Saved")
    time.sleep(0.5)


def HighScores():
    '''
    Displays the top 5 scores
    '''
    with open("Users.csv", "r", newline='', encoding="UTF8") as file:  # This opens up the Users file in read mode
        reader = csv.reader(file)
        scoresList = []
        for row in reader:
            scoresList.append(int(row[0]))  # Adds each score to a list
        InsertionSort(scoresList)  # Sorts the list
        tPrint("\033[0;37;40mThe highscores were:\n")
        x = -1
        if len(scoresList) >= 5:
            for i in range(5):  # Prints the top 5 scores by going backwards through the list
                print(scoresList[x])
                x -= 1
        else:
            for i in range(len(scoresList)): # Prints the top scores if less than 5 scores
                print(scoresList[x])
                x-=1


def ListFirstLetter(list):
    '''
    Stores the first letter of a word in a list
    '''
    x = 0
    for index in list:
        temp = index
        temp = temp[0]  # Sets each word in the list to its first letter
        list[x] = temp
        x += 1  # Increments to the next word in the list
    return list


def FirstLetter(word):
    '''
    Returns the first letter of the word
    '''
    word = word[0]  # Sets word to the first letter
    return word


def LetterOnly(letters):
    '''
    Isolates the string so that only the letters remain
    '''
    x = 0
    word = ''
    for index in letters:
        if index == '[':
            x += 1
        elif index == ']':
            x += 1
        elif index == ',':
            x += 1
        elif index == "'":
            x += 1
        else:
            word = word + index  # Makes sure that only letters end up being shown
    return word


def GenreSelection(changeSelection = 1):
    '''
    Allows the selected genre to be changed
    '''
    global genre
    global randomFlag
    passed = False
    genreList = ["Disco.txt", "Electronic Dance.txt", "Folk.txt", "Indie.txt", "Metal.txt", "Pop.txt", "Punk.txt", "Rap.txt", "Rock.txt", "Video Game.txt"]
    if changeSelection == 0:
        if randomFlag:
            choice = random.randint(1, len(genreList))
            genre = genreList[choice - 1]
            passed = True
        return genre
    while not passed:
        choice = int(input("Your options are:\n1. Disco\n2. Electronic Dance\n3. Folk\n4. Indie\n5. Metal\n6. Pop\n7. Punk\n8. Rap\n9. Rock\n10. Video Game\n0. Random: "))
        if choice > len(genreList) or choice < 0:
            print("That was not an option.")
            continue
        elif choice == 0:
            randomFlag = True
            choice = random.randint(1, len(genreList))
        genre = genreList[choice - 1]
        passed = True
    return genre


def SongSelection():
    '''
    Selects a random song within the genre
    '''
    global genre
    if genre == 0:
        genre = GenreSelection()
    else:
        selection = input("Do you want to change the genre? (Y/N): ")
        if selection[0].lower() == 'y':
            genre = GenreSelection(1)
        else:
            genre = GenreSelection(0)
    f = open("Genres\\" + genre,"r")  #this selected genre document is saved into the variable 'f'
    linez = f.readlines()  # takes all items from the document and puts it into a list
    index = random.randint(0,len(linez) -3)  # Randomly selects an index in the song
    line = linez[index]
    linesSplit = line.split(':')  # Splits the line via the colon
    artist = linesSplit[0]  # Assigns the first half to artist
    song = linesSplit[1]  # Assigns the second half to song
    sShow = song.split()  # Splits the song into each of the words
    song = linesSplit[1]  # Reassigns song so that it isn't split
    song = song[:len(song) -1]  # Cuts the song name to remove the new line escape character
    sShow = ListFirstLetter(sShow)  # Reduces each word to the first letter of each one
    return artist, sShow, song


def AskSong():
    '''
    The main game loop
    '''
    os.system("cls")  # Clears the screen
    global streak  # References the global variables
    global points
    chances = 2
    guessed = False
    selection = SongSelection()  # Chooses a song
    artist = selection[0]
    sShow = selection[1]
    song = selection[2]
    songLow = song.lower()  # Lowercase of the song
    sShow = str(sShow)
    sShow = LetterOnly(sShow)  # Shows only the letters in the name
    print("\033[1;33;40mStreak:", streak)
    print("Points:", points)
    tPrint("\033[0;37;40mArtist -> " + artist)
    tPrint("Song's Initials-> " + sShow)
    tPrint("Can you guess the song? ")
    while not guessed:
        while chances >= 1:  # While the chances are not zero
            guess = input()
            guess = guess.lower()  # Lowercase the guess
            if guess == songLow:  # If the guesses match
                tPrint("\033[1;32;40mCorrect!")
                guessed = True
                streak += 1
                points += streak
                tPrint("\033[0;37;40mYou earned %s point(s)" % streak)
                tPrint("You are now on %s point(s)" % points)
                time.sleep(1)
                break
            else:
                chances -= 1
                streak = 0
                points -= 1
                if chances == 1:
                    tPrint("You only get one more chance, have another go! \n")
                break
        if chances == 0:
            tPrint("\033[1;31;40mGame Over")
            tPrint("\033[0;37;40mThe song was " + song)
            if not userMode:
                disableGuest = tInput("It seems you are a guest; would you like to sign in to save your scores? (Y/N): ")
                if disableGuest[0].lower() == 'y':
                    Authentication(True)
                    Save()
            HighScores()
            points = 0
            Replay()
    AskSong()


def Replay():
    '''
    If the game ends, asks if the player wants to play again
    '''
    guess = tInput("Want to play again?: ")
    guess = guess.lower()  # Sets the guess to lowercase
    if guess[0] == "y":
        os.system("clear")  # Clears the screen
        AskSong()
    else:
        tPrint("Thanks for playing!")
        quit()


def Rules():
    '''
    Displays the rules
    '''
    tPrint("\033[1;33;40mBy Eshan Fadi ft Arul Batra\n")
    time.sleep(1)
    tPrint("\033[0;37;40mFor a selected song, the artist and the song's initials will show.")
    tPrint("As you play with consecutive right answers, you gain a streak.")
    tPrint("You gain extra points based on your streak.")
    time.sleep(1)
    tPrint("However, you get 2 chances for each song and making a mistake breaks your streak.")
    time.sleep(1)
    tPrint("Making 2 mistakes results in a game over.")


def Menu():
    '''
    The beginning menu system
    '''
    selection = -1
    while selection != 0:  # While the selection is not quit
        selection = tIntInput("\033[0;37;40m1. Play a new game of Music Guess\n2. Display Highscores\n3. Rules\n0. Exit\n")
        if selection == 1:
            Authentication()
            AskSong()
        elif selection == 2:
            HighScores()
        elif selection == 3:
            Rules()
            tInput("Please press any key to continue...")
        else:
            tPrint("That was not an option.\n")
    quit()


def InsertionSort(list):
    '''
    Insertion Sort
    '''
    for i in range(1, len(list)):
        save = list[i]
        pos = i - 1
        while pos >= 0 and save < list[pos]:
            list[pos + 1] = list[pos]
            pos -= 1
        list[pos + 1] = save

if __name__ == "__main__":
    SongSelection()