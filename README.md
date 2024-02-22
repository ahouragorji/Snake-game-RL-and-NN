# Snake game with Neural Networks and Reinforcement Learning
## Introduction
In this project, we utilized a neural network model trained with reinforcement learning to play the Snake game.
## model.py
Here is our neural network model. We employed the torch library and incorporated four Linear Layers with dynamic dimensions.
## Game.py
This script assists us in managing our game environment.
## Replay.ipynb
We utilize this script to observe our trained model in action.
## Snake.ipynb
This serves as our primary code, encompassing the creation, training, and evaluation of our neural network-based model. We utilized an input size of 10 to represent our states with 10 parameters. Additionally, we configured the output dimension to 5, enabling our model to indicate the preferred path.
## Results
### Score
![image](https://github.com/ahouragorji/Snake-game-RL-and-NN/assets/99167642/afa0118f-5daa-451d-aeaa-0141382c6740)
This plot illustrates our Score per Episode. The performance improvement is evident, culminating in a score of 76.
### Length of the snake
By the end of our training, we achieved an average snake length of 10.
![image](https://github.com/ahouragorji/Snake-game-RL-and-NN/assets/99167642/0fc99e6d-0312-47a8-873e-a56703af5aad)

This project was a component of the "Principles of Artificial Intelligence" course.
