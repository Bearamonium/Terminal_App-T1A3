# Terminal Application - T1A3

## GitHub Repository Link

https://github.com/Bearamonium/Terminal_App-T1A3.git

## Code Styling Guide - PEP 8

## Text-Based Dungeon Crawler

Welcome to Amoria - a simple, single player, text-based dungeon crawler adventure! 

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

Object Orientated Programming (OOP) will be the main basis of creation for all source code of Amoria. 

- Classes<br>
        Each class will have it's own abilities, starting inventory and starting gear score

- Dungeon Movement <br>
        All movement within the dungeon will be held within the gameplay loop, and take user inputs to move their character through each room/floor in the dungeon. 

## Installation & Guide

To begin installation, you will need to open your terminal program or app of choice, and run the command to execute the installation file run.sh. 

Amoria requires Python to be installed on your computer. The bash script provided (run.sh) will run through the specific installation requirements and in turn install python on your computer if you don't already have it. 

Once it has completed the installation, it will then initalise a virtual environment which will allow the program to install the required packages it needs to run. Following this, Amoria is yours to explore! 

