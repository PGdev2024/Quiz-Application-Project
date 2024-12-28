# Quiz-Application-Project
<b>#1.PROJECT DESCRIPTION</b>
This project is a console based quiz application
It involves the following functions as listed below:
1.Reading questions with their respective answers and options from a questions.txt file
2.Displaying or conducting a quiz with the questions and the options in the given txt file and also displaying the instructions of the quiz at the start and storing the user's name
3.Recording the responses from the user to each question in the quiz and displaying the user's answer along with the fact that whether his answer is correct or incorrect
4.Displaying the user's score at the end of the quiz along with notifying the user about the completion of the quiz
5.Recording the user's name and score and storing in a scores.txt file
<br>
<b>#2.FEATURES OF THE PROJECT</b>
The project involves a lot of features that make the quiz application even if it is on the console quite appealing and also draws the attention of the user on how by the power of coding one can achieve anything
The key features include:
<i>Functions/Methods:</i>
The code behind the project involves simple functions that handle the functionality of the program quite well and easily.You can say that the tasks involved in the quiz application are divided among the methods
on the basis of the names
The code involves 3 functions:
1.quizpresentation():It reads the questions,options and correct answer from the questions.txt file and is responsible for the the presentation or display of the quiz as it controls the call of the function which is responsible for recording the response from the user and displaying the questions of the quiz
2.questiondata(s):It displays the questions to the user upon call and also displays the user his/her answer and the fact that whether his answer is correct or not
s is the the line read from the questions.txt file stored as a list
3.userscore():Notifies the user about his/her score and the quiz completion and stores the user's name and score in a scores.txt file
<i>Variables:</i>
Only two global variables are used mainly:
1.qno--> Stores the question number of the question
2.score-->Stores the score of the user in terms of the number of correct answers given by the user
Little local variables are used too as:
1.ans------> Stores the response to a question made by the user
2.s1-------> Stores the line read from the questions.txt file as a list
3.n1-------> Stores the striped name of the user along with a comma and space
4.name-----> Stores the original name of the user as entered by him/her
5.finalscore--> Stores the finalscore of the user in terms of the total number of questions answered 
6.f:Reads each line from the questions.txt file
<i>Simplicity</i>
Simple print statements are used where unecessary code is not required like to display the instructions of the quiz ,to record  username input and the enter key input from the user input() function and simple if and else is used to begin the quiz after user presses the enter key
<i>Colorama module</i>
Colorama module is used to make the console more appealing and to make the text which is displayed to the user look better.It also adds an extra sense of right or wrong when the user enters right or wrong answer respectively
<b>#3.How to run the project</b>
There are three simple steps to run this project which are given below as follows:
STEP 1: Enter your questions of the quiz along with their options and correct answer in the way as given below:
Question,Option A,Option B,Option C,Option D,Correct Answer
REMEMBER THE COMMAS AND ALSO WRITE EACH DATA SET IN A NEW LINE
<br>
STEP 2: Run the main py file using anyone of your ide which runs python and enjoy the quiz application :)
<br>
STEP 3:Check the scores file to know about the users which have played the game along with their respective scores
<b>#4.Instructions for installation</b>
To ENJOY all the FEATURES of this project i would highly recommend the user to install the colorama module in the ide through which you will run the py file


