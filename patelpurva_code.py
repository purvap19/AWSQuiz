'''This program allows user to play quiz, view scoreboard, download questions,
delete a user, and view user guide based on user input.'''
import boto3
from botocore.exceptions import ClientError
import logging
#logs information, including time, to a log file
logging.basicConfig(filename='logfile.txt', format='%(levelname)s %(asctime)s: %(message)s', level=logging.INFO)
def menu_choices():
    '''This function provides a command-line menu for the program'''
    print("Choose one of the following options: ")
    print("a. Take quiz")
    print("b. View scoreboard")
    print("c. Download all questions")
    print("d. Delete a user from the leaderboard")
    print("e. View user guide")
    print("f. Exit")
def question_1():
    '''Function for first question and answer'''
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Leaderboard')
    s3_client = boto3.client(service_name='s3')
    #from quiz.txt file in S3 read first question
    result = s3_client.get_object(Bucket="bucket-week8", Key='quiz.txt')
    for line in result["Body"].readlines()[0:1]: #outputs the first line from the txt file
        each_line = line.decode('utf-8')
        print(each_line)
    answer_1 = str(input("Enter your answer: "))
    #if answer is correct, add one point, else no point is added
    if answer_1 == 'D':
        print("Correct!")
        print("+1 point")
        print("")
        increment()
        question_2()
    elif answer_1 == 'A' or answer_1 == 'B' or answer_1 == 'C':
        print("Incorrect! Correct answer was D. Verona")
        question_2()
    else:
        print("Please enter valid option!")
        question_1()
def question_2():
    '''Function for second question and answer'''
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Leaderboard')
    s3_client = boto3.client(service_name='s3')
    #from quiz.txt file in S3 read second question
    result = s3_client.get_object(Bucket="bucket-week8", Key='quiz.txt')
    for line in result["Body"].readlines()[1:2]: #outputs the second line from the txt file
        each_line = line.decode('utf-8')
        print(each_line)
    answer_2 = str(input("Enter your answer: "))
    if answer_2 == 'B':
        print("Correct!")
        print("+1 point!")
        print("")
        increment()
        question_3()
    elif answer_2 == 'A' or answer_2 == 'C' or answer_2 == 'D':
        print("Incorrect! Correct answer was B. Octopus")
        question_3()
    else:
        print("Please enter valid option!")
        question_2()
def question_3():
    '''Function for third question and answer'''
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Leaderboard')
    s3_client = boto3.client(service_name='s3')
    #from quiz.txt file in S3 read third question
    result = s3_client.get_object(Bucket="bucket-week8", Key='quiz.txt')
    for line in result["Body"].readlines()[2:3]: #outputs the third line from the txt file
        each_line = line.decode('utf-8')
        print(each_line)
    answer_3 = str(input("Enter your answer: "))
    if answer_3 == 'C':
        print("Correct!")
        print("+1 point")
        print("")
        increment()
        question_4()
    elif answer_3 == 'A' or answer_3 == 'B' or answer_3 == 'D':
        print("Incorrect! Correct answer was C. Ostrich")
        question_4()
    else:
        print("Please enter valid option!")
        question_3()
def question_4():
    '''Function for fourth question and answer'''
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Leaderboard')
    s3_client = boto3.client(service_name='s3')
    #from quiz.txt file in S3 read fourth question
    result = s3_client.get_object(Bucket="bucket-week8", Key='quiz.txt')
    for line in result["Body"].readlines()[3:4]: #outputs the fourth line from the txt file
        each_line = line.decode('utf-8')
        print(each_line)
    answer_4 = str(input("Enter your answer: "))
    if answer_4 == 'A':
        print("Correct!")
        print("+1 point")
        print("")
        increment()
        question_5()
    elif answer_4 == 'B' or answer_4 == 'C' or answer_4 == 'D':
        print("Incorrect! Correct answer was A. Uranus")
        question_5()
    else:
        print("Please enter valid option!")
        question_4()
def question_5():
    '''Function for third question and answer'''
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Leaderboard')
    s3_client = boto3.client(service_name='s3')
    #from quiz.txt file in S3 read fifth question
    result = s3_client.get_object(Bucket="bucket-week8", Key='quiz.txt')
    for line in result["Body"].readlines()[4:5]: #outputs the fifth line from the txt file
        each_line = line.decode('utf-8')
        print(each_line)
    answer_5 = str(input("Enter your answer: "))
    if answer_5 == 'C':
        print("Correct!")
        print("+1 point")
        print("")
        increment()
        question_6()
    elif answer_5 == 'A' or answer_5 == 'B' or answer_5 == 'D':
        print("Incorrect! Correct answer was C. Au")
        question_6()
    else:
        print("Please enter valid option!")
        question_5()
def question_6():
    '''Function for third question and answer'''
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Leaderboard')
    s3_client = boto3.client(service_name='s3')
    #from quiz.txt file in S3 read sixth question
    result = s3_client.get_object(Bucket="bucket-week8", Key='quiz.txt')
    for line in result["Body"].readlines()[5:6]: #outputs the sixth line from the txt file
        each_line = line.decode('utf-8')
        print(each_line)
    answer_6 = str(input("Enter your answer: "))
    if answer_6 == 'B':
        print("Correct!")
        print("+1 point")
        print("")
        increment()
        question_7()
    elif answer_6 == 'A' or answer_6 == 'C' or answer_6 == 'D':
        print("Incorrect! Correct answer was B. Honey")
        question_7()
    else:
        print("Please enter valid option!")
        question_6()
def question_7():
    '''Function for third question and answer'''
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Leaderboard')
    s3_client = boto3.client(service_name='s3')
    #from quiz.txt file in S3 read seventh question
    result = s3_client.get_object(Bucket="bucket-week8", Key='quiz.txt')
    for line in result["Body"].readlines()[6:7]: #outputs the seventh line from the txt file
        each_line = line.decode('utf-8')
        print(each_line)
    answer_7 = str(input("Enter your answer: "))
    if answer_7 == 'B':
        print("Correct!")
        print("+1 point")
        print("")
        increment()
        question_8()
    elif answer_7 == 'A' or answer_7 == 'C' or answer_7 == 'D':
        print("Incorrect! Correct answer was B. Copper")
        question_8()
    else:
        print("Please enter valid option!")
        question_7()
def question_8():
    '''Function for third question and answer'''
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Leaderboard')
    s3_client = boto3.client(service_name='s3')
    #from quiz.txt file in S3 read eigth question
    result = s3_client.get_object(Bucket="bucket-week8", Key='quiz.txt')
    for line in result["Body"].readlines()[7:8]: #outputs the eighth line from the txt file
        each_line = line.decode('utf-8')
        print(each_line)
    answer_8 = str(input("Enter your answer: "))
    if answer_8 == 'A':
        print("Correct!")
        print("+1 point")
        print("")
        increment()
        question_9()
    elif answer_8 == 'B' or answer_8 == 'C' or answer_8 == 'D':
        print("Incorrect! Correct answer was A. 46")
        question_9()
    else:
        print("Please enter valid option!")
        question_8()  
def question_9():
    '''Function for third question and answer'''
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Leaderboard')
    s3_client = boto3.client(service_name='s3')
    #from quiz.txt file in S3 read ninth question
    result = s3_client.get_object(Bucket="bucket-week8", Key='quiz.txt')
    for line in result["Body"].readlines()[8:9]: #outputs the ninth line from the txt file
        each_line = line.decode('utf-8')
        print(each_line)
    #check for invalid input answers
    special_characters="@#$&*1234567890EFGHIJKLMNOPQRSTUVWXYZ"
    answer_9 = str(input("Enter your answer: "))
    if answer_9 == 'C':
        print("Correct!")
        print("+1 point")
        print("")
        increment()
        question_10()
    elif answer_9 == 'A' or answer_9 == 'B' or answer_9 == 'D':
        print("Incorrect! Correct answer was C. Chicago")
        question_10()
    else:
        print("Please enter valid option!")
        question_9()     
def question_10():
    '''Function for third question and answer'''
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Leaderboard')
    s3_client = boto3.client(service_name='s3')
    #from quiz.txt file in S3 read tenth question
    result = s3_client.get_object(Bucket="bucket-week8", Key='quiz.txt')
    for line in result["Body"].readlines()[9:10]: #outputs the tenth line from the txt file
        each_line = line.decode('utf-8')
        print(each_line)
    answer_10 = str(input("Enter your answer: "))
    if answer_10 == 'C':
        print("Correct!")
        print("+1 point")
        print("")
        increment()
        print("Your total score: " + str(score))
        if score == 10:
            print("Great job!")
        #puts the final score in the leaderboard table in dynamodb
        response = table.put_item(
            TableName='Leaderboard',
            Item={
                'Username': user_name,
                'Score': score
                }
            )
        print("")
        menu()
    elif answer_10 == 'A' or answer_10 == 'B' or answer_10 == 'D':
        print("Incorrect! Correct answer was C. Snow White")
        print("Your total score: " + str(score))
        #puts the final score in the leaderboard table in dynamodb
        response = table.put_item(
            TableName='Leaderboard',
            Item={
                'Username': user_name,
                'Score': score
                
            }
            )
        print("")
        menu()
    else:
        print("Please enter valid option!")
        question_9()    
def play_quiz():
    '''Allows user to enter their username and begin the quiz'''
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Leaderboard')
    global user_name
    user_name = str(input("Create your username: "))
    #add username to the dynamoDB table
    logging.info("New username created: " + user_name)
    #add username to the leaderboard table in dynamodb
    with table.batch_writer() as batch:
        batch.put_item(
            Item={
                'Username': user_name
                }
            )
    print("Username '{}' was successfully created!".format(user_name))
    #Begin quiz questions
    print("")
    question_1()
def view_scoreboard():
    '''Allows user to view the leaderboard table'''
    print("")
    print("SCOREBOARD")
    dynamodb = boto3.resource('dynamodb')
    table=dynamodb.Table('Leaderboard')
    response = table.scan()
    for item in response['Items']:
        print(item)
    menu()
def download_questions():
    '''Function to download questions file from the bucket'''
    bucket_name = 'bucket-week8'
    key = 'quiz.txt'
    s3 = boto3.resource('s3')
    try:
        s3.Bucket(bucket_name).download_file(key,'quiz.txt')
        logging.info("{} was downloaded".format('quiz.txt'))
        print("**** {} was downloaded successfully! ****".format('quiz.txt'))
        menu()
    except ClientError as exception_error:
        logging.error(exception_error)
        return False
    return True
def delete_user():
    '''Allows user to delete themselves from the table'''
    delete_username = str(input("Enter the username you would like to delete: "))
    s3_client = boto3.client('s3')
    dynamodb=boto3.resource("dynamodb")
    table = dynamodb.Table('Leaderboard')
    #deletes a username from the leaderboard table
    try:
        response = table.delete_item(
            Key={
                'Username': delete_username
                }
            )
        logging.info("Username: " + delete_username + " was deleted")
        print(" {} was successfully deleted from the table".format(delete_username))
        print("")
        menu()
    except ClientError as exception_error:
        logging.error(exception_error)
        return False
    return True
def view_userguide():
    '''Allows user to view userguide for the quiz program'''
    s3_client = boto3.client(service_name='s3')
    #outputs contents from userguide.txt file from S3 bucket
    print("")
    result = s3_client.get_object(Bucket="bucket-week8", Key='userguide.txt')
    for line in result["Body"].readlines(): 
        each_line = line.decode('utf-8')
        print(each_line)
    menu()
def menu():
    '''function for user input choices'''
    menu_choices()
    user_input = 0
    while user_input!= 'e':
        user_input = str(input())
        if user_input == 'a':
            play_quiz()
        elif user_input == 'b':
            view_scoreboard()
        elif user_input == 'c':
            download_questions()
        elif user_input == 'd':
            delete_user()
        elif user_input == 'e':
            view_userguide()
        elif user_input== 'f':
            print("Thank you for using the quiz program!")
        else:
            print("*******Invalid choice! Please try again******")
            print("")
            menu_choices()
def increment():
    '''Keeps score total for the user'''
    global score
    score = score + 1
    
score = 0
print("*** Hello, welcome to the quiz program! ***")
menu()
