import sys
from pandas import read_csv

def findSubjectToppers(subjects, mark_list, total_list):
    '''Returns a dictionary with a list of subjectwise toppers'''
    max_marks = {subject: 0 for subject in subjects}
    toppers = {subject: [] for subject in subjects}
    for subject in subjects:
        for i in range(n):
            mark = mark_list.loc[i, subject]
            total_list[i] += mark
            if mark > max_marks[subject]:
                max_marks[subject] = mark
                toppers[subject] = [mark_list['Name'][i]]
            elif mark == max_marks[subject]:
                toppers[subject].append(mark_list['Name'][i])   
    return toppers

def findBestStudents(mark_list, total_list):
    '''Finds the best 3 students in total marks among the class'''
    m1, m2, m3 = 0, 0, 0
    best1, best2, best3 = '', '', ''
    for ind, total in enumerate(total_list):
        if total > m1:
            best3, m3 = best2, m2
            best2, m2 = best1, m1
            best1, m1 = mark_list['Name'][ind], total
        elif total > m2:
            best3, m3 = best2, m2
            best2, m2 = mark_list['Name'][ind], total
        elif total > m3:
            best3, m3 = mark_list['Name'][ind], total
    return best1, best2, best3

if __name__ == '__main__':
    if(len(sys.argv)) == 1:
        print('Error: Input file name required!')
        sys.exit(1)
    filename = sys.argv[1]
    mark_list = read_csv(filename)
    n = len(mark_list)                  # Total number of rows
    subjects = mark_list.keys()[1:]     # Subject names
    names = mark_list.index             # Student names

    total_list = [0 for _ in range(n)]

    toppers = findSubjectToppers(subjects, mark_list, total_list)
    best1, best2, best3 = findBestStudents(mark_list, total_list)

    for subject in subjects:
        n = len(toppers[subject])
        if n == 1:
            print('Topper in', subject, 'is ', end='')
        else:
            print('Toppers in', subject, 'are ', end='')
        print(*toppers[subject], sep=', ',  end='.\n\n')
    print('Best students in the class are {}, {} and {}.'.format(best1, best2, best3))
    

'''
Output:
PS D:\Academics\Clg\Placements\LeanKloud\part_2> python .\marklist.py
Topper in Maths is Manasa.

Topper in Biology is Sreeja.

Topper in English is Praneeta.

Toppers in Physics are Sagar, Mehuli.  

Toppers in Chemistry are Manasa, Vivek.

Topper in Hindi is Aravind.

Best students in the class are Manodhar, Bhavana and Sourav.
'''

'''
Time Complexity Analysis:
To find the subject toppers : O(N*M)
    where,  N is the number of students
            M is the number of subjects
    Generally, the number of subjects is a constant (6 in this case)
    therefore the complexity is to O(N).
    
To find the best students: O(N)
    Since we only want the best 3 students we can traverse through the total
    marks once while maintaining and updating the top 3 students.
    This logic can be easily extended to find the top k students using lists,
    which makes the complexity O(N*k)
    where,  N is the total number of students
            k is the number of best students to find.
    In this case k is a constant (k=3) therefore the complexity is O(N).

Overall complexity: O(N)
'''