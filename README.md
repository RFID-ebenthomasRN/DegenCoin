# DegenCoin
CoinFlip Recorder with ridiculously overly ccomplex, ineffective 'predictive'(antiRNG) logic and learnin
**1. Model Built to Predict Coin Flips:**

   - The original code used a multitude of prediction methods based on different strategies ('Bayesian', 'Frequency', 'Time-Adjusted Frequency', 'Markov Chain', 'LSTM').
   - We focused on a simplified LSTM prediction model to condition coin flips, replacing the multiple prediction methods with a more efficient, machine learning based LSTM model.

**2. Replacement of Multipliers with Coin Flip Outcomes:**

   - The initial code was designed around '-multipliers' like '2x', '3x', '5x' and '50x'. We replaced these multipliers with coin flip outcomes 'Heads' and 'Tails'.
 
**3. Introduced Training Threshold for Model Training:**

   - Added a 'training threshold' which determines the number of coin flips before the model starts training itself in the class 'FlipPredictor'. After reaching said threshold, the program simply appends all future function calls to flip history and removes the first element in the sequence, while also ensuing iterative training.

**4. Full Refactoring of Tkinter GUI Interface :**

   - Replaced the interactive GUI elements and dialogues to work according to coin flips instead of the original multipliers.
   - Added 'Submit' button to confirm a coin flip.
   - Provided an interactive function to adjust the 'training threshold'.
   
**5. Integrated Saving and Loading Model:** 

   - Added 'Save' and 'Load' buttons to save the current state of model, and load a previously saved state.This enables retention of learned behavior of model over consecutive sessions.

The readme of the program should include the following sections:

**Title:**

e.g. Coin Flip Predictor GUI

**Description:**

Provide utility function of application. May include goals, potential uses, and interesting points of the project.

**Dependencies:**

List packages the program depends on (e.g. Tkinter, Keras, Numpy).

**Installation & Execution Instructions:**

Step by step on getting the program to run on a local machine.

**Contribution:*
Ne-Ebansski
4.0-TheHomi3
In case you allow, specify guidelines for outsiders contributing to your project. 


**License:**

State the type of software licensing your project uses.

**Credits:**

#In the 4 Model code, we have:

#ModelBuilder` builds the LSTM model.
#BayesianPredictor` builds the Bayesian model.
#The `FlipPredictor` takes a coin flip outcome and trains both models with each new outcome.
#Before that, it employs four distinct strategies to predict the result of the following coin flip:
#LSTM Prediction`
#Bayesian Prediction`
#Frequency Prediction`: Predicts the most common outcome in history.
#Markov Chain Prediction`: Predicts that the outcome will be the same as the last.

#The console displays each model’s predictions and respective accuracy, even
#keeping track of the aggregate or consensus prediction for each coin flip. We're
#tracking model accuracy consistently, averaging the accuracy of every prediction
#model to date. LSTM and Bayesian post higher influence on the consensus prediction
#as they hold 3 and 2 votes, respectively, while Frequency and Markov Chain
#predictions each have a single voice, making them lesser influencers over the choice
#of the final prediction.raging the accuracy of every prediction #model to date. LSTM and Bayesian post higher influence on the consensus prediction #as they hold 3 and 2 votes, respectively, while Frequency and Markov Chain #predictions each have a single voice, making them lesser influencers over the choice #of the final prediction.

#code is now significantly complex with the integration of various models. This can be
#much more susceptible to performance or compatibility issues compared to a simpler
#model.

#In the 2bd attempt at the 4 model version we have 
#`BernoulliNB
#`PredictorWithTimeDependentRatio
#`PredictorByOneStepMarkovChain
#`MajorityVoteClassifier 
#classes,  Bayesian and Markov chain models are appropriately weighted prior to final
#consensus
#allowing the connections between the supervised learning and XHV indicator
#implementations to remain unaltered.


#3rd Vision of 4 Model code 

#Eliminated the form with multiple input options for coin flip results. Replaced it with a
#combobox for selecting the options easily.
#Rather than having three buttons for each action (update, predict, and reset), I
#embedded the update action into the selection operation of the combobox. This
#means that every time you select an option (Heads or Tails), it would update the
#system automatically.

#This condensed user interface allows users to follow the flow easily (selecting either
#”Heads" or "Tails", checking prediction, and optional: saving or loading models). 

#for both versions 
#application now uses SQLite to store the coin flip
history 
#which is more efficient and reliable compared to the previous approach. 
#When you run the app, the program will store all coin flips in the SQLite database. 
#This enables data retention across multiple sessions and allows the model to have a larger training set. 
#The model can now be saved and loaded between different sessions.
