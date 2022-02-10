def os_grade():
    quizzes = []
    tests = []
    labs = []

    while True:
        quizmark = input('Enter QUIZ marks (be sure to include both windows and linux quizzes), blank to exit: ')
        if quizmark == '':
            break
        quizzes.append(float(quizmark))

    print()

    while True:
        testmark = input('Enter TEST marks, blank to exit: ')
        if testmark == '':
            break
        tests.append(float(testmark))

    print()

    while True:
        labmark = input('Enter LAB marks (include both linux/win labs), blank to exit: ')
        if labmark == '':
            break
        labs.append(float(labmark))

    quizweight = (sum(quizzes) / len(quizzes)) / 100 * 15
    testweight = (sum(tests) / len(tests)) / 100 * 30
    labweight = (sum(labs) / len(labs)) / 100 * 15

    print()
    print('Grade Breakdown\n--------------- \nTests- 30%\nLabs- 15%%\nQuizzes- 15%\nFinal Exam- 40%\n')
    grade_so_far = round((quizweight + testweight + labweight) / 60 * 100, 2)
    grade_to_pass = round((60 - (quizweight + testweight + labweight)) / 40 * 100, 2)

    print(f'Grade heading into exam: {grade_so_far}')
    print()
    print(f'Exam grade needed to pass course: {grade_to_pass}')
    pick = input('Continue? Y/N: ')
    if pick == 'Y' or pick == 'y':
        menu()
    else:
        print('Suit yourself')


def pp_grade():
    quizzes = []
    assignments = []

    while True:
        quizmark = input('Enter QUIZ marks (enter separate grades for MCQs and coding parts), blank to exit: ')
        if quizmark == '':
            break
        quizzes.append(float(quizmark))

    print()

    while True:
        assignmentmark = input('Enter assignment marks, blank to exit: ')
        if assignmentmark == '':
            break
        assignments.append(float(assignmentmark))

    print()

    quizweight = (sum(quizzes) / len(quizzes)) / 100 * 40
    assignmentweight = (sum(assignments) / len(assignments)) / 100 * 30
    print()
    print('Grade Breakdown\n--------------- \nQuizzes- 40%\nAssignments- 30%\nFinal Exam- 30%\n')
    grade_so_far = round((quizweight + assignmentweight) / 70 * 100, 2)
    grade_to_pass = round((70 - (quizweight + assignmentweight)) / 30 * 100, 2)

    print(f'Grade heading into exam: {grade_so_far}')
    print()
    print(f'Exam grade needed to pass course: {grade_to_pass}')
    pick = input('Continue? Y/N: ')
    if pick == 'Y' or pick == 'y':
        menu()
    else:
        print('Suit yourself')


def rd_grade():
    tests = []
    assignments = []

    while True:
        testmark = input('Enter test marks, blank to exit: ')
        if testmark == '':
            break
        tests.append(float(testmark))

    print()

    while True:
        assignmentmark = input('Enter assignment marks, blank to exit: ')
        if assignmentmark == '':
            break
        assignments.append(float(assignmentmark))

    print()

    testweight = (sum(tests) / len(tests)) / 100 * 25
    assignmentweight = (sum(assignments) / len(assignments)) / 100 * 40

    print()
    print('Grade Breakdown\n--------------- \nTests- 25%\nAssignments- 40%\nFinal Exam- 35%\n')
    grade_so_far = round((testweight + assignmentweight) / 65 * 100, 2)
    grade_to_pass = round((65 - (testweight + assignmentweight)) / 35 * 100, 2)

    print(f'Grade heading into exam: {grade_so_far}')
    print()
    print(f'Exam grade needed to pass course: {grade_to_pass}')
    pick = input('\nContinue? Y/N: ')
    if pick == 'Y' or pick == 'y':
        menu()
    else:
        print('Suit yourself')


def wmad_grade():
    labs = []
    websitemark = float(input('Enter your mark on the website assignment: '))

    while True:
        labmark = input('Enter lab marks, blank to exit: ')
        if labmark == '':
            break
        labs.append(float(labmark))

    print()

    labweight = (sum(labs) / len(labs)) / 100 * 35
    websiteweight = websitemark / 100 * 35
    print()
    print('Grade Breakdown\n--------------- \nLabs- 35%\nWeb Site Assignment- 35%\nThunkable App Assignment- 30%\n')
    grade_so_far = round((labweight + websiteweight) / 70 * 100, 2)
    grade_to_pass = round((70 - (labweight + websiteweight)) / 30 * 100, 2)

    print(f'Grade prior to Thunkable App mark: {grade_so_far}')
    print()
    print(f'Thunkable grade needed to pass course: {grade_to_pass}')
    pick = input('\nContinue? Y/N: ')
    if pick == 'Y' or pick == 'y':
        menu()
    else:
        print('Suit yourself')


def ma_grade():
    tests = []
    assignments = []

    while True:
        testmark = input('Enter test marks, blank to exit: ')
        if testmark == '':
            break
        tests.append(float(testmark))

    print()

    while True:
        assignmentmark = input('Enter assignment marks, blank to exit: ')
        if assignmentmark == '':
            break
        assignments.append(float(assignmentmark))

    print()

    testweight = (sum(tests) / len(tests)) / 100 * 40
    assignmentweight = (sum(assignments) / len(assignments)) / 100 * 20

    print()
    print('Grade Breakdown\n--------------- \nTests- 40%\nAssignments- 20%\nFinal Exam- 40%\n')
    grade_so_far = round((testweight + assignmentweight) / 60 * 100, 2)
    grade_to_pass = round((60 - (testweight + assignmentweight)) / 40 * 100, 2)

    print(f'Grade heading into exam: {grade_so_far}')
    print()
    print(f'Exam grade needed to pass course: {grade_to_pass}')
    pick = input('Continue? Y/N: ')
    if pick == 'Y' or pick == 'y':
        menu()
    else:
        print('Suit yourself')


def menu():
    print("************Welcome to the GRADEULATOR**************")
    print()

    choice = input("""
                Pick the course you want to see your current grade average
                and exam passing grade

                      A: Procedural Programming
                      B: Operating Systems
                      C: Relational Databases
                      D: Math
                      E: Mobile Web and App Dev
                      Q: I'm afraid to know, get me outta here

                      Please enter your choice: """)

    if choice == "A" or choice == "a":
        pp_grade()
    elif choice == "B" or choice == "b":
        os_grade()
    elif choice == "C" or choice == "c":
        rd_grade()
    elif choice == "D" or choice == "d":
        ma_grade()
    elif choice == "E" or choice == "e":
        wmad_grade()
    elif choice == "Q" or choice == "q":
        print('Ignorance is bliss :)')
        sys.exit
    else:
        print("Pick a letter")
        print("Please try again")
        menu()


menu()
