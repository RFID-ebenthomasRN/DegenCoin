Oksy take the format for this code and create a third code.
Start this new code by asking questions
1. Name of game
    1. Use this for the title of the program
2. How many variables are there
    1. The use of this answer is obvious 
3. What are the variables, and w
    1. What is their value, 
    2. percentage of winning
    3. RNG Range 

Once the names and percentages are given, use this info to create buttons labelled with the value provided. 
That way, when each value occurs, the user can easily click the button allowing for each data point a better understanding of the ACTUAL frequency of each variable. This will be compared to the percentage provided, and the relationship shall be presented numerically; and graphically. In relation to the stated percentage and in relation to each other.
Use this info and the code we just refined to create novel programs for the user. Initially, the program will act as a recording spot for the frequency of occurrence for each of the variables provided. 

Once the program is established to collect the data and represent and record probability and occurrence. Implement the logic models used in past programs to try to begin to guess what the next variable to occur will be.
Keep track of the accuracy of guesses for all models and like in previous programs make this information accessible. 

Finally, add a random number generator as a 5th model. Possible values are 1 - 99999, correlate the actual random number delivered to the range provided in the initial questioning fir each variable, if the number falls within the range of  given variable display the resulting variable as a 5th model of prediction 

Each game should be saved a retained after is creation by asking user if they would like to save game when closing or if user select save during program use. Program is named title given initially and stored in a manner and place that is accessible to user. So that user may reopen program, have all variables and corresponding buttons remain in place and all past data is recalled. 
 
It is not required that user be able to specify range from which dates selected, assume all data point for graph creation and model training. Lets start here and once completed provide suggestions to improve operation and use 


1. `game_config.py`:  Asks for the user input for game creation and stores necessary information to be used across the application.

2. `game_database.py`: Handles database connectivity and functions required for storing and retrieving game and variable information.

3. `model_builder.py`: Contains functions and classes for building and training the prediction models.

4. `variable_predictor.py`: Houses the main logic for predicting the next variable based on different models.

5. `main_app.py`: The main application script that ties everything together. It creates the game GUI and implements the full functionality of the app.

6. `visualizer.py`: Handles the functionality for visualizing the data collected and the predictions made. 

7. `game_utils.py`: Holds utility functions that can be used across the project, such as RNG range handling, game saving and loading etc. 