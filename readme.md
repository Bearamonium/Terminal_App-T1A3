# Terminal Application - T1A3

## Application Creater

### Philip Mills

#### October 2023 Standard Cohort, Coder Academy

## GitHub Repository Link

https://github.com/Bearamonium/Terminal_App-T1A3.git

## Text-Based Dungeon Crawler

Welcome to Amoria - a simple, single player, text-based dungeon crawler adventure! 

## Code Styling Guide - PEP 8

Where applicable outside of styling code used from textwrap, PEP 8 has been chosen as the appropriate styling guide for the code used for Amoria. The style guide makes the code easier for overall readability and comprehension - using correct indentations and naming conventions. 

The link for the PEP 8 styling guide can be found at https://peps.python.org/pep-0008/#programming-recommendations. 

## Features List

### Classes

Amoria offers a simple choice for new adventurers at the start of their dungeon dive; three basic classes can be chosen by players prior to the commencement of the game. These three classes are: 

- Sun's Hunter
- Crimson Blade
- Night Whisperer

Object Orientated Programming (OOP) will be implemented as the main building blocks of this application, and each of the three classes above will be initialised as their own class within the code. Skills for each class with be included as functions, along with the variables to store their gear score based on their inventory, a dictionary of their skills for usage in tables and implementing actions and their base lives. Error handling is used to ensure that players select one of classes available, until a correct option is made.

The player variable will be intialised as an object of one of the three Classes once the player has chosen the relevant input to do so.

### Dungeon Movement & Exploration

To progress through the dungeon, Amoria will require user input at a constant level to continue forward (or left... or right... or run away!). Each step on your journey will provide you with adequate descriptions of what you are seeing and providing you the oppurtunity choose your next action.

A menu will consitently make itself available to the player, asking them to choose from 1 of 4 actions, with the final one being to move. Prompts will be provided to move the desired direction, and players will type in the direction listed to the room they'd like to move into. This filters through a room dictionary, and constantly updates the current room variable so that the correct descriptions and room contents are available each and every time the player moves. 

If you choose to explore the current room, you can find one of three things - an enemy to fight, items to loot or... nothing. The function to explore the room will loop through these three options listed, and will deal with each one by one, until finally nothing is left in the room to explore further. If an enemy is defeated or an item is picked up, those items are deleted from the room's dictionary values, making sure that players won't have to fight the same enemy twice or be able to pick up multiples of the same items. 

### Battle Features

Similar to some popular dungeon-crawler esque table-top role-playing games, Amoria uses a simple battle generator; your gear score will be put up against the monster's indicated challenge rating, and then converted into running balances for a simple skill usage input from the player. This feature will really stipulate the requirement for exploration; as you progress further, the challenge rating for monsters will get higher and higher. Taking a linear path will only cause more trouble for players, so it is highly recommended to stop and take a breather, and really interact with the environment around you within Amoria. 

Once you run into an enemy, you'll enter the combat loop which will prompt the player to either attack or flee. If you choose to flee, you'll be prompted whether you were successful or not, but if not, be prepared to fight! A table will be generated for you on the available skills you have to use, their damage along with how many times you can use the skill in Amoria.

The flow of battle is simple; it's the players turn, then it's the monsters turn, and so on until one of you is down and out for the count. Be wary, if you lose in battle, it's GAME OVER, and you'll be prompted to restart your adventure. 

### Inventory Management - Equipping and Unequipping Items

On your journey, you will find other items that are available to be used and equipped by your character. If an item is available in the room, you will be prompted whether you would like to collect it or not. 

Once you have picked it up, you have the option in the menu to open your inventory, which will allow you to view the current items you hold in your inventory, and the weapon and armour you currently have equipped. Once in the inventory, you will be asked whether you would like to equip or unequip an item and choose the slot you'd like to change. After following the prompts, the desired item will either be simply moved to your inventory, leaving an open weapon or armour slot, or replace that item with another in your inventory. 

### Inventory Management - Item Usage

In certain rooms, items can be used to unveil the secrets in Amoria - but you'll have to find them first! 

Once you have collected an item, you can enter your inventory again and choose whether you'd like to use an item or not, and then be prompted to type in the item name you'd like to use. Your either successful in the usage of the item; prompting that the item has been used following a text output, or it's unsuccessful and you are sent back to the inventory. 

The key to move forward is hidden, Amoria not willing to give it up as easily as one might think. 

### Restart Game

Initial variables have all been included in one function, which allows for the game to be able to loop through instances of the game once the player had been defeated or sucessfully completed the game. 

Each loop of restarting the game will re-initalise each room, along with your starting position in the game, allowing you to start your journey back into Amoria. 

## Implementation Plan

Object Orientated Programming (OOP) will be the main basis of creation for all source code of Amoria. Trello has been used as the project management software of choice, link below: 

https://trello.com/invite/b/0OJzT7jV/ATTI306d9fa0e046d2ea4643d11059b7f5282E1CD145/terminal-application

- Classes
    - Each class will have it's own abilities, starting inventory and starting gear score
    - Skills will be added as separate functions to allow a battle loop to be efficiently created
    - Each class will use inheritance on the main Class of Character
    - Gear scores for the characters will be based on the attriubtes of the weapon and armour they have currently equipped - starting inventory will be initialised in the class

- Dungeon Movement
    - All movement within the dungeon will be held within the gameplay loop, and take user inputs to move their character through each room/floor in the dungeon. 
    - Input will then move the current room variable to match the room player wanted to move to
    - Players will be able to move into new rooms depending on whether they have used the specified item in the room dictionary
    - Descriptions of each room will printed for the player each time they enter a new room
    - Menu will be included which gives the player options on what they would like to do in the current room
    - Additional descriptions, if available, will also print to the player when exploring the room
    - Combat and item pick up will be prompted when exploring the room as well

- Combat
    - Combat loop, using other functions like an attack list to be implemented
    - Player will be prompted that they have run into an enemy, and can choose to either attack or flee from the encounter
    - Attack list function will print a table of available skills to the user if they choose to attack, and user will type in the relevant skill name to use the skill
    - Monster will attack AFTER player has made their choices 
    - Damage will be handled through the monster's challenge rating, and the players gear score, handled through a instanced attribute that will reset each encounter based on their current gear score total
    - Game over or continuation of the game based on the outcome of combat

- Loot Features & Inventory Management
    - Items to be added into the rooms dictionary for players to pick up as they progress
    - Inventory management feature to be included to allow players to access their current items
    - Equip and unequip items feature to be added for players to change their current equipped items using input prompts
    - Usage of items will also be available, depending on the room dictionary and if the item is listed as availabe to use

### Screenshots from Trello: 

![Alt text](./resources/Screenshot%202023-12-16%20120133.png)

![Alt text](./resources/Screenshot%202023-12-16%20120157.png)

![Alt text](./resources/Screenshot%202023-12-19%20002900.png)

![Alt text](./resources/Screenshot%202023-12-19%20003018.png)

![Alt text](./resources/Screenshot%202023-12-19%20003156.png)

![Alt text](./resources/Screenshot%202023-12-20%20233924.png)

![Alt text](./resources/Screenshot%202023-12-20%20234052.png)

![Alt text](./resources/Screenshot%202023-12-23%20110139.png)

![Alt text](./resources/Screenshot%202023-12-23%20111943.png)

## Installation & Guide

### Prerequisites: 

- Operating Systems: 
    - Linux
    - macOS
    - Windows 
- Bash: Access to a Bash environment (default on Linux and macOS, available through GitBash or WSL on Windows)
- Python: Installation steps below, you can check if python is already installed using ```python --version``` on the command line

### Installation Steps: 

1. Open a Terminal

    - Linux/macOS: Open the Terminal app.
    - Windows: 
        - Git Bash: Open Git Bash.
        - PowerShell: Follow steps below for Windows setup.
        - WSL: Open the WSL terminal

2. Navigate to Directory: 
Use the ```cd``` command to change thr working directory to the location of the run.sh file included in the folder download. For example: 

```bash
cd ./path/to/your/download/location
```

Alternitively, you could open your terminal app in the current folder by right clicking on the folder and choosing "Open in terminal". 

3. Run the following command to execute the script: 

```bash
bash run.sh
```

### Windows Installation Steps: 

#### Download and install Python

1. Download the Installer:

- Visit the official Python website: https://www.python.org/downloads/windows/.
- Choose the latest stable version of Python 3 (e.g., Python 3.10 as of today).
- Click the "Download Windows installer (64-bit)" button (or 32-bit if needed).

2. Run the Installer:

- Double-click the downloaded installer file.
- Check the "Add Python 3.x to PATH" option (crucial for running Python from the command line).
- Click "Install Now" to proceed with the standard installation.

3. Verify Installation:

- Open a command prompt or PowerShell window.
- Type python --version and press Enter.
- If Python is installed correctly, you'll see its version number displayed.

#### Install WSL

1. Open Windows Powershell terminal
    - Run command ```wsl --install```.
    - Set up username and password.
    - Reboot system.

2. Open Ubunu terminal 
    - Run command ```sudo apt update```, followed by ```sudo apt upgrade```.
    - After the two commands above are finalised, you will need to then run ```sudo apt-get install python3.10-venv```.<br>
      The above commands should then have successfully installed everything you need to run the ```bash run.sh``` in the Windows Powershell Terminal. 





