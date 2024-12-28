# Quiz-Application-Project
<b>#1.PROJECT DESCRIPTION</b>
<br>
This project is a console based quiz application
<br>
It involves the following functions as listed below:
<br>
1.Reading questions with their respective answers and options from a questions.txt file
<br>
2.Displaying or conducting a quiz with the questions and the options in the given txt file and also displaying the instructions of the quiz at the start and storing the user's name
<br>
3.Recording the responses from the user to each question in the quiz and displaying the user's answer along with the fact that whether his answer is correct or incorrect
<br>
4.Displaying the user's score at the end of the quiz along with notifying the user about the completion of the quiz
<br>
5.Recording the user's name and score and storing in a scores.txt file
<br>
<b>#2.FEATURES OF THE PROJECT</b>
<br>
The project involves a lot of features that make the quiz application even if it is on the console quite appealing and also draws the attention of the user on how by the power of coding one can achieve anything
<br>
The key features include:
<br>
<i>Functions/Methods:</i>
<br>
The code behind the project involves simple functions that handle the functionality of the program quite well and easily.You can say that the tasks involved in the quiz application are divided among the methods
<br>
on the basis of the names
<br>
The code involves 3 functions:
<br>
<big>1.quizpresentation()</big>:It reads the questions,options and correct answer from the questions.txt file and is responsible for the the presentation or display of the quiz as it controls the call of the 
<br>
function which is responsible for recording the response from the user and displaying the questions of the quiz
<br>
<big>2.questiondata(s)</big>:It displays the questions to the user upon call and also displays the user his/her answer and the fact that whether his answer is correct or not
<br>
s is the the line read from the questions.txt file stored as a list
<br>
<big>3.userscore()</big>:Notifies the user about his/her score and the quiz completion and stores the user's name and score in a scores.txt file
<br>
<i>Variables:</i>
<br>
Only two global variables are used mainly:
<br>
1.<u>.qno</u>--> Stores the question number of the question
<br>
2.<u>score</u>-->Stores the score of the user in terms of the number of correct answers given by the user
<br>
Little local variables are used too as:
<br>
1.<u>ans</u>------> Stores the response to a question made by the user
<br>
2.<u>s1</u>-------> Stores the line read from the questions.txt file as a list
<br>
3.<u>n1</u>-------> Stores the striped name of the user along with a comma and space
<br>
4.<u>name</u>-----> Stores the original name of the user as entered by him/her
<br>
5.<u>finalscore</u>--> Stores the finalscore of the user in terms of the total number of questions answered 
<br>
6.<u>f</u>:Reads each line from the questions.txt file
<br>
<i>Simplicity</i>
<br>
Simple print statements are used where unecessary code is not required like to display the instructions of the quiz ,to record  username input and the enter key input from the user input() function and simple if 
<br>
and else is used to begin the quiz after user presses the enter key
<br>
<i>Colorama module</i>
<br>
Colorama module is used to make the console more appealing and to make the text which is displayed to the user look better.It also adds an extra sense of right or wrong when the user enters right or wrong answer 
<br>
respectively
<br>
<b>#3.How to run the project</b>
<br>
There are three simple steps to run this project which are given below as follows:
<br>
STEP 1: Enter your questions of the quiz along with their options and correct answer in the way as given below:
<br>
<b><big>Question,Option A,Option B,Option C,Option D,Correct Answer</big></b>
<br>
<b>REMEMBER THE COMMAS AND ALSO WRITE EACH DATA SET IN A NEW LINE</b>
<br>
STEP 2: Run the main py file using anyone of your ide which runs python and enjoy the quiz application :)
<br>
STEP 3:Check the scores file to know about the users which have played the game along with their respective scores
<br>
<b>#4.Instructions for installation</b>
<br>
To ENJOY all the FEATURES of this project i would highly recommend the user to install the colorama module in the ide through which you will run the py file


