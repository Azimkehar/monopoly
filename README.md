## How to run the code
Use any IDE to run game.py file to run the monopoly game. I used pycharm IDE for my project. FYI I have only tested with rolls_1.json and rolls_2.json that needs to tested for any potential bugs.

## Outcome of the game.
* Using rolls_1.json file the outcame was 
  * Peter won with remaining balance of 37
  * Billy came 2nd with remaining balance of 19
  * Charlotte came 3rd with remaining balance of 8
  * Sweedal came last with remaining balance of 3
  
* Using rolls_2.json file the outcame was
  * Billy won with remaining balance of 75
  * Charlotte came 2nd with remaining balance of 48
  * Peter came 3rd with remaining balance of 12
  * And Sweedal came last again with remaining balance of 5

## Woven coding test

Your task is to write an application to play the game of Woven Monopoly.

In Woven Monopoly, when the dice rolls are set ahead of time, the game is deterministic.

### Game rules
* There are four players who take turns in the following order:
  * Peter
  * Billy
  * Charlotte
  * Sweedal
* Each player starts with $16
* Everybody starts on GO
* You get $1 when you pass GO (this excludes your starting move)
* If you land on a property, you must buy it
* If you land on an owned property, you must pay rent to the owner
* If the same owner owns all property of the same colour, the rent is doubled
* Once someone is bankrupt, whoever has the most money remaining is the winner
* There are no chance cards, jail or stations
* The board wraps around (i.e. you get to the last space, the next space is the first space)


### Your task
* Load in the board from board.json
* Implement game logic as per the rules
* Load in the given dice rolls files and simulate the game
  * Who would win each game?
  * How much money does everybody end up with?
  * What spaces does everybody finish on?


The specifics and implementation of this code is completely up to you!

### What we are looking for:
* We are a Ruby house, however feel free to pick the language you feel you are strongest in.
* Code that is well thought out and tested
* Clean and readable code
* Extensibility should be considered
* A git commit-history would be preferred, with small changes committed often so we can see your approach

Please include a readme with any additional information you would like to include, including instructions on how to test and execute your code.  You may wish to use it to explain any design decisions.

Despite this being a small command line app, please approach this as you would a production problem using whatever approach to coding and testing you feel appropriate.
