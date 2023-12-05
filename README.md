# FlappyBird Game Documentation

## Introduction

Welcome to the documentation for the FlappyBird project! This project is a simple implementation of the classic Flappy Bird game using Python and the Pygame library.

## Table of Contents

1. [Overview](#1-overview)
2. [Installation](#2-installation)
3. [Game Components](#3-game-components)
   - [Display](#display)
   - [Background](#background)
   - [Bird](#bird)
   - [Pipes](#pipes)
   - [Sound Effects](#sound-effects)
   - [Font](#font)
   - [Score](#score)
4. [Game Loop](#4-game-loop)
5. [Controls](#5-controls)
6. [Conclusion](#6-conclusion)

## 1. Overview
Welcome to the documentation for the FlappyBird project! This project is a simple implementation of the classic Flappy Bird game using Python and the Pygame library.

## 2. Installation
Before running the game, make sure you have Python and Pygame installed. You can install Pygame using the following command:
```bash
pip install pygame
```

To run the game, execute the provided Python script:
```
python flapybird.py
```
## 3. Game Components

*Display*  
The game window has a width of 280 pixels and a height of 512 pixels.  

*Background*  
The game features a background image loaded from "assets/images/sprites/Background.png".  

*Bird*  
The bird has three frames for animation: Bird_down, Bird_mid, and Bird_up. The bird's movement is controlled by the spacebar.  

*Pipes*  
Pipes are created, drawn, and moved to create obstacles for the bird. They spawn at random heights.  

*Sound Effects*  
The game includes sound effects for flapping wings, collisions, and scoring points.  

*Font*  
A custom font ("04B_19.ttf") is used to display the score and high score.  

*Score*  
The player's score is displayed during the game, and the high score is shown at the game over screen.  

## 4. Game Loop
The game follows a continuous loop where events are processed, and the game state is updated and rendered. The loop handles user input, bird movement, pipe generation, collision detection, and scoring.  

## 5. Controls

<li> *Spacebar*: Flap the bird's wings to navigate through pipes.  
<li> Press spacebar to start a new game after a game over.  


## 6. Conclusion
 You've successfully explored the documentation for the FlappyBird project. Have fun playing the game and challenge yourself to achieve a high score! If you encounter any issues or have suggestions for improvement, feel free to contribute to the GitHub repository.  