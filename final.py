print("WELCOME TO THE QUIZ!")
score = 0
print("===USER REGISTRATION===")

# USER DETAILS
username = input("Enter the username/Gamer's name: ")
first_name = input("Enter First Name: ")
# PASSWORD CONFIRMATION
attempts = 3
while attempts > 0:
    password = input("Enter Password: ")
    confirm_password = input("Confirm password: ")
    
    if password == confirm_password:
        print("Passwords match!")
        
        age = int(input("Please enter your age: "))
        if age >= 18:
            print("You can play the quiz...")
            
            # TERMS AND CONDITIONS
            print("=== Terms and Conditions ===")
            print("1. You must be at least 13 years old to play this quiz.")
            print("2. Do not use external help during the quiz.")
            print("3. You will get 1 point for each correct answer.")
            print("4. The quiz consists of 7 IT-based questions.")
            print("5. Your score will be displayed at the end.")
            print("6. No negative marking.")
            print("7. You must answer all the questions.")
            
            # AGREEMENT FOR TERMS AND CONDITIONS
            agree = input("Do you agree to the terms and conditions? (yes/no): ")

            if agree == 'yes':
                print("Great! Let's begin with the quiz...")
                
                # Quiz Instructions (only shown if they agree to terms)
                print("=== Quiz Instructions ===")
                print("1. You will be asked 7 multiple-choice questions.")
                print("2. Type the letter (a, b, c, or d) to select your answer.")
                print("3. Each correct answer gives you 1 point.")
                print("4. No negative marking for incorrect answers.")
                print("5. Your final score will be displayed at the end.")
                
                input("Press Enter to start the quiz...")

                # Score and questions
                score = 0
                total_questions = 7
                print("===QUESTIONS===")
                # Question 1
                
                print("1.) What does CPU stand for?")
                print("a) Central processing unit")
                print("b) Central process unit")
                print("c) Computer personal unit")
                print("d) Central processor unit")
                answer = input("Enter your answer (a, b, c or d): ")
                attempts=3
                while attempts>0:
                     if answer == "a":
                       print("Correct answer!")
                       score += 1
                       break
                     else:
                       attempts-=1                    
                       if attempts > 0:
                         print(f"Wrong answer, try again. Only {attempts} attempt(s) left.")
                         print("1.) What does CPU stand for?")
                         print("a) Central processing unit")
                         print("b) Central process unit")
                         print("c) Computer personal unit")
                         print("d) Central processor unit")
                         answer = input("Enter your answer (a, b, c or d): ")
                         
                       else:
                          print("Wrong!No attempts left now...")
                         

                # Question 2
                print("2.) Which language is known as the mother of all programming languages?")
                print("a) C++")
                print("b) Python")
                print("c) Assembly")
                print("d) Fortran")
                answer = input("Enter your answer (a, b, c or d): ")
                attempts=3
                while attempts>0:
                     if answer == "d":
                       print("Correct answer!")
                       score += 1
                       break
                     else:
                       attempts-=1                    
                       if attempts > 0:
                         print(f"Wrong answer, try again. Only {attempts} attempt(s) left.")
                         print("2.) Which language is known as the mother of all programming languages?")
                         print("a) C++")
                         print("b) Python")
                         print("c) Assembly")
                         print("d) Fortran")
                         answer=input("Enter your answer (a,b,c or d):")
                       else:
                         print("Wrong!No attempts left now...")
                
                # Question 3
                print("3.) What does HTML stand for?")
                print("a) Hypertext markup language")
                print("b) High technology modern language")
                print("c) Home tool management language")
                print("d) Hyperlink text language")
                answer = input("Enter your answer (a, b, c or d): ")
                attempts=3
                while attempts>0:
                     if answer == "a":
                       print("Correct answer!")
                       score += 1
                       break
                     else:
                       attempts-=1                    
                       if attempts > 0:
                         print(f"Wrong answer, try again. Only {attempts} attempt(s) left.")
                         print("3.) What does HTML stand for?")
                         print("a) Hypertext markup language")
                         print("b) High technology modern language")
                         print("c) Home tool management language")
                         print("d) Hyperlink text language")
                         answer = input("Enter your answer (a, b, c or d): ")
                       else:
                         print("Wrong!No attempts left now...")
                         
                
                # Question 4    
                print("4.) Which company created the Python programming language?")
                print("a) Microsoft")
                print("b) Google")
                print("c) Bell Labs")
                print("d) Python Software Foundation")
                answer = input("Enter your answer (a, b, c or d): ")
                attempts=3
                while attempts>0:
                     if answer == "d":
                       print("Correct answer!")
                       score += 1
                       break
                     else:
                       attempts-=1                    
                       if attempts > 0:
                         print(f"Wrong answer, try again. Only {attempts} attempt(s) left.")
                         print("4.) Which company created the Python programming language?")
                         print("a) Microsoft")
                         print("b) Google")
                         print("c) Bell Labs")
                         print("d) Python Software Foundation")
                         answer = input("Enter your answer (a, b, c or d): ")
                       else:
                         print("Wrong!No attempts left now...")
                         
                # Question 5
                print("5.) Which data structure uses LIFO (Last In, First Out) principle?")
                print("a) Queue")
                print("b) Stack")
                print("c) Array")
                print("d) Linked List")
                answer = input("Enter your answer (a, b, c or d): ")
                attempts=3
                while attempts>0:
                     if answer == "b":
                       print("Correct answer!")
                       score += 1
                       break
                     else:
                       attempts-=1                    
                       if attempts > 0:
                         print(f"Wrong answer, try again. Only {attempts} attempt(s) left.")
                         print("5.) Which data structure uses LIFO (Last In, First Out) principle?")
                         print("a) Queue")
                         print("b) Stack")
                         print("c) Array")
                         print("d) Linked List")
                         answer = input("Enter your answer (a, b, c or d): ")
                       else:
                         print("Wrong!No attempts left now...")
                
                # Question 6
                print("6.) Which is the extension for a Python file?")
                print("a) .java")
                print("b) .py")
                print("c) .txt")
                print("d) .cpp")
                answer = input("Enter your answer (a, b, c or d): ")
                attempts=3
                while attempts>0:
                     if answer == "b":
                       print("Correct answer!")
                       score += 1
                       break
                     else:
                       attempts-=1                    
                       if attempts > 0:
                         print(f"Wrong answer, try again. Only {attempts} attempt(s) left.")
                         print("6.) Which is the extension for a Python file?")
                         print("a) .java")
                         print("b) .py")
                         print("c) .txt")
                         print("d) .cpp")
                         answer = input("Enter your answer (a, b, c or d): ")
                       else:
                         print("Wrong!No attempts left now...")
                
                # Question 7
                print("7.) Which protocol is used to send emails?")
                print("a) FTP")
                print("b) HTTP")
                print("c) SMTP")
                print("d) SSH")
                answer = input("Enter your answer (a, b, c or d): ")
                attempts=3
                while attempts>0:
                     if answer == "c":
                       print("Correct answer!")
                       score += 1
                       break
                     else:
                       attempts-=1                    
                       if attempts > 0:
                         print(f"Wrong answer, try again. Only {attempts} attempt(s) left.")
                         print("7.) Which protocol is used to send emails?")
                         print("a) FTP")
                         print("b) HTTP")
                         print("c) SMTP")
                         print("d) SSH")
                         answer = input("Enter your answer (a, b, c or d): ")
                       else:
                         print("Wrong!No attempts left now...")  
                
                        # Final score 
                print(f"QUIZ COMPLETED! Your final score is: {score}/7")
                
                # Result based on score
                if score == 7:
                    print("EXCELLENT! You got all answers correct...")
                elif score >= 5:
                    print("Good job! You did well...")
                else:
                    print("Better luck next time!")
                break  

            elif agree == 'no':
                print("You must agree to participate. TRY AGAIN!!")
                break 

            else:
                print("Invalid input! Please type 'yes' or 'no'")

        else:
            print("You must be at least 18 years or older to play the quiz...")
        break 
    
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Passwords don't match, try again. Only {attempts} attempt(s) left.")
        else:
            print("Passwords don't match, no attempts left... EXITING!!")
            


# Certificate message
if score > 0:
    print("Congratulations on completing the quiz!")
    print("===Certificate of Achievement===")
    print("------------------------------------------------")
    print(f"Participant:{username}")
    print(f"*Score: {score}/7")
    print("------------------------------------------------")
    print("Congratulations! You have successfully completed the IT Quiz! You have demonstrated your knowledge in computer fundamentals and earned this certificate.")
    print("*Well done! Keep up the great work!")
    print("------------------------------------------------")
else:
    print("Better luck next time! Keep practicing!")