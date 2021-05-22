from pandas import read_csv

def findSubjectToppers(subjects, mark_list, total_list):
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
    mark_list = read_csv('Student_marks_list.csv')
    n = len(mark_list) # Total number of rows
    subjects = mark_list.keys()[1:] # Subject names
    names = mark_list.index # Student names

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