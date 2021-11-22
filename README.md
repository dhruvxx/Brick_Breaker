# BRICK_BREAKER

This game is a termial-based replica of the game -  brickbreaker.  
It involves using a ball to break an arrangement of bricks with the use of a movable paddle to direct the ball and prevent it from falling off the screen.

---

## Types of bricks

There are a total of 3 kinds of bricks:
 - *White coloured bricks*:  
These bricks have the highest strength, that is, their strength equals 6
 - *Magenta coloured bricks*:  
These bricks have the strength equal to 4
 - *Blue coloured bricks*:  
These bricks are the weakest amongst the other brings and if the ball hits this brick, then the brick breaks.

---

## Game Controls
 - 'a' : Moves paddle left
 - 'd' : Moves paddle right
 - 'q' : Ends game
 - 'z' : Moves to the next level
 - 'x' : Moves to the level after next level

---

## Winning and Losing
You lose if the ball touches the ground. It ends the game.

---

## Running the game:
To run the game, run the following commands:

`pip3 install colorama`


`python3 main.py`

---

## Collisions:
- *With bricks and ball*:  
Ball reflects when it hits the brick at any surface and makes a sound.

- *With paddle and ball*:  
Ball reflects when it hits the top of the paddle and makes a sound.

- *With ball and wall*:  
Ball reflects when it hits the wall and makes a sound.

---

## OOPS Concepts:
When making this game, the following OOPS concepts were applied:

- *Abstraction*:  
All the functionality in main.py is implemented via intuitive commands like ball.move() and board.render().

- *Encapsulation*:  
Each game element has it's own class and methods to make the operation and functioning of those game elements simpler.

- *Inheritance*:  
Defines a class that inherits all the methods and properties from another class. 

- *Polymorphism*:  
Different classes have methods with the same name.

---
