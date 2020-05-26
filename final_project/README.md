# Welcome to the ‘Snake World’!
This is my twist on a **classic ‘Snake Game’**. 

Developed this as my **Final Project** for the [**‘Code In Place – 2020’**](https://engineering.stanford.edu/news/free-coding-education-time-covid-19), a remote learning experience offered by the Stanford University under Prof. Mehran Sahami, Prof. Chris Piech and 800+ Section Leaders teaching 10,000 students all over the world!


# About the Game
This is a two-player version of the Snake Game Classic. 

Following is a walk-through showcasing the game:

- Game starts with a prompt ‘Welcome to the Snake World! Your game begins in 3..2..1..’
- Each player has Keyboard controls provided for navigating their Snake on the arena
    - **Player 1: ← ↓ ↑ →   keys**
    - **Player 2: ‘a’ ‘s’ ‘w’ ‘d’ keys**
- The objective of the game is to **keep eating ‘Food’** that appears in random locations to keep increasing your snake size.
- The game goes on until both the players’ snakes are dead. The **player with maximum** score in the end is **the Winner!**
    - Snake can die in any of the following scenarios:
        - Hits the wall / boundary
        - Hits itself
        - Hits the opponent Snake



# Concepts used in the Code
Code In Place laid down a strong foundation for programming fundamentals and Python. Almost all the concepts learned have been implemented through this code, which includes:
- **Graphics**
- **Animation**
- **Functions & Decomposition**
- **Lists** 
- **Dictionaries**

In addition to these, **‘Classes’** have been utilized for proper code organization and encapsulation.

Exploring the coding techniques for implementing 'Classes' as well as the various 'tkinter' features/usage was a fun learning experience!
Coming up with algorithm (without any help/tutorials) to solve this problem was a eureka moment!

**Libraries used:** tkinter, random, time


# Algorithm 
- Each Snake is **instantiated as a chain of squares** appearing as a single long creature with an **oval ‘snake head’**.
- Navigating through the controls turns the snake in any of the four directions:
    - The ‘snake head’ is repositioned based on the player controls.
    - The block following the snake head is programmed to take snake head’s previous position in the subsequent frame. Similarly, the 3rd block takes the 2nd block position and so on.
- There is a **provision in the code to modify the speed of the snakes**.
- **Food particles (Circles) appear at random positions** one after the other.
- Each **snake is checked for overlaps** (either with food, itself or other snake) and actions are taken accordingly to either eat the food & increase the score OR kill the snake.
- Finally a **winner is displayed based on the scores**.
