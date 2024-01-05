# FlappyBird Game Documentation

## Introduction

Welcome to the documentation for the FlappyBird project! This project is a simple implementation of the classic Flappy Bird written in 3D Unity.

## Table of Contents

1. [Overview](#1-overview)
2. [Installation](#2-installation)
3. [Game Components](#3-game-components)
4. [Game Loop](#4-game-loop)
5. [Controls](#5-controls)

## 1. Overview
Welcome to the documentation for the FlappyBird project! This project is a simple implementation of the classic Flappy Bird game using 3D Unity.

## 2. Installation
Before running the game, download the game from release section. Un-Zip and run Flappy-Bird 3D.exe.
Or if you want to analyze the code clone and open it with Unity 2022.3.f1.
To run the game, execute the provided Python script:

## 3. Game Components

*Display*  
The game window has a width of 280 pixels and a height of 512 pixels.  

*Background*  
Made an scene which it has 3D clouds, barrels and background components.  

*Bird*  
The bird was reimplemented with animation, texture and effects such when crashes from barrel as exemple.

*Pipes*  
Pipes are created, drawn, and moved to create obstacles for the bird. They spawn at random heights.  

*Sound Effects*  
The game includes sound effects for flapping wings, collisions, and scoring points.  

*Score*  
The player's score is displayed during the game, and the high score is shown at the game over screen.  

## 4. Game Loop
The game follows a continuous loop where events are processed, and the game state is updated and rendered. The loop handles user input, bird movement, pipe generation, collision detection, and scoring.  

## 5. Controls

<li> *Spacebar*: Flap the bird's wings to navigate through pipes.  
<li> Press spacebar to start a new game after a game over.  
