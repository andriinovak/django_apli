from random import shuffle

def students_names(request):
    students = ['sergiy', 'andrii', 'vasyl', 'bohdan', 'ira', 'sasha']
    shuffle(students)
    return {'students': students}
