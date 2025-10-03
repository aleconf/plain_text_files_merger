# Motivation

As a chess player, I have got plenty of [PGN files](https://en.wikipedia.org/wiki/Portable_Game_Notation), and it often happens that I have to merge several of them together, with a blank line separating the different files: for instance, I want to create a file with all games of a given player, or a file with games related to a given [ECO code](https://en.wikipedia.org/wiki/Encyclopaedia_of_Chess_Openings#Main_ECO_codes), and so on. \
The order according to which PGN files are merged is not important, because I can use some dedicated programs for rearranging the games in the file afterwards, e.g. [Scid vs. PC](https://scidvspc.sourceforge.net/). \
Since I have not found an available solution for merging the files as I like, I decided to create it myself, generalising it to any type of [plain text](https://en.wikipedia.org/wiki/Plain_text) files and allowing to choose what to write in the separating line.

Clearly, checking the file extension is not a suitable method to recognise plain text files, since one can rename a binary file as a `.txt` one, and on the contrary there are plain text files with an extension different from `.txt`, e.g. PGN or CSV files.

# Description

The code asks for the following information:
- the full path (e.g. `/Users/aleconf/GitHub/plain_text_files_merger`) of the directory containing the plain text files to be merged: the input is validated, i.e. the code verifies that such directory actually exists;
- the string to write in the line separating the different files (Enter for a blank line);
- the full path of the directory where the merged file should be saved: the input is validated, i.e. the code verifies that such directory actually exists;
- the name of the output file: the input is validated, i.e. the code verifies that such file does not exist yet.

The code then analyses all files inside the given directory, determines which files are plain text, merges them together, and saves the result as a file according to the received input.

# How to use it

All executable files have been created using PyInstaller.

- On a Mac computer: 
    - run
        ```
        ./dist/filemerger_mac
        ```
    - For getting the full path of a directory run
        ```
        pwd
        ```


### Remark for non-technical users

Clearly, one could prefer not to have any separator at all in the merged file, or that the separator is not on a line by itself: there are (at least) two solutions for this use case, and the second one does not require writing code at all.
1. Modify the Python code, namely lines 42-46.
2. Run the executable file using as separator a string which for sure is **not** contained in any of the plain text files to be merged, e.g. «per potere con lo aiuto di sì alta mira pervenire al disegno loro». Then use a text editor that supports regexes, e.g. [Sublime Text](https://www.sublimetext.com/) or [Notepad++](https://notepad-plus-plus.org/), and with regexes enabled replace all instances of the string «\nper potere con lo aiuto di sì alta mira pervenire al disegno loro\n» (i.e. the string «**\n*the separator you inserted when running the file*\n**») with your desired separator (leave empty the Replace field if you want no separator at all).

# To-do list

* [ ] Create a Windows executable file.
* [ ] Create a GUI with a File Explorer that allows the selection of only a subset of all plain text files and their rearrangement in the desired, customised merging order.
