# Task 1 code template for FIT9136 Assignment 2.
# Instructions to students:
# 1. Where required, replace the *pass* statements with your own method and
#   function definitions. Your submission must comply with the specification:
#   do not rename specified functions or change the number or type of arguments
#   or return values; otherwise you will be deemed not to have demonstrated
#   clear comprehension of the specified instructions. (You may define
#   your own additional functions and instance variables if you wish, as long
#   as these don't contradict the specified requirements. You may also
#   import any libraries allowed by the assignment specification.)
# 2. Complete task 1 within the framework of this template file.
# 3. Modify the filename (AND import statement(s), where required) to replace
#   the xxxxxxxx with your student ID number.
# 4. Complete tasks 2 and 3 within the other template files. The finished
#   program is split into three files, linked together by import statements.
# 5. In this file, you may define your own testing code within the 'main'
#   block to check if your simulation is working when running this script file
#   directly. Code in the main block will not be run by the auto marker algorithm,
#   which will instead test the specified functions/methods by attempting to
#   call them directly according to how they are defined in the assignment 
#   requirements specification.
# 6. Before submission, you should remove these instructions from this
#   template file and add your own program comments instead. This template file
#   has omitted program comments, which are your responsibility to add. Any
#   other 'placeholder' comments should be removed from your final submission.

import pandas as pd


class Person:
    # all with unique names => use Set instead of List

    
    def __init__(self, first_name, last_name):
        self.friends = []
        self.first_name = first_name
        self.last_name = last_name
    
    def add_friend(self, friend_person):
        self.friends.append(friend_person)
    
    def get_name(self):
        return self.first_name + ' ' + self.last_name
    
    def get_friends(self):
        # returns a list of Person objects for the social connections that have been added.
        return list(self.friends)
    
    def __repr__(self):
        result = self.get_name() + ': '
        for f in self.friends:
            result += f.get_name() + ','
        return result + '\n'
    
    def __str__(self):
        return self.get_name()


def get_firstname(name):
    return name.split()[0]


def get_lastname(name):
    return name.split()[1]


def load_people2():
    # pd.set_option('display.max_rows', 1000)
    df = pd.read_csv('a2_sample_set.txt',
                     header=None,
                     sep='[:]',
                     index_col=0,
                     names=['person', 'friends'],
                     engine='python')
    
    # data = df.to_numpy()
    friends = df['friends']
    df['friends'] = friends.str.split(',')
    people = {}
    for index, value in df.iterrows():
        person = Person(get_firstname(index), get_lastname(index))
        people[person.get_name().strip()] = person
    
    for index, value in df.iterrows():
        person = people[index]
        for friend_name in value[0]:
            person.add_friend(people[friend_name.strip()])
    print(type([v for k, v in people.items()]))
    return [v for k, v in people.items()]


# def load_people():
#     file = open('a2_sample_set.txt', 'r')
#     for line in file:
#         name_and_friends = line.split(':')
#         person = Person(get_firstname(name_and_friends[0]), get_lastname(name_and_friends[0]))
#         print(person)


def main():
    print(load_people2())
    # load_people2()


if __name__ == '__main__':
    main()
    # placeholder only. You may add your own testing code within this
    # main block to check if the code is working the way you expect.

# do not add code here (outside the main block).


# columns = df.columns
# print(columns)
# print(df.describe())
# print(data[0])
# for d in data:
#     print(d)
#     print(d.str.split(','))

# friends = df['friends']
# print(friends.str.split(','))
# df['friends'] = friends.str.split(',')
# print(df)
# print(tabulate(df, tablefmt="pipe", headers="keys"))
# friends = df.friends
# print(friends)
# df.head()
# print(type(df.values))
# print(df.columns)
# print(df.loc['Jom Tones'])
# for _ in df:
#        print(_)
# for _ in df:
#     print(type(_))
# for i in range(2):
# print(df.iloc[i])
# for index, value in df.iterrows():
#     print(index)
#     print(value)
# print(type(_))
# print(type(df.iterrows()))
# for i in range(df.shape[0]):
#     print(df.iloc[i])
#     # For printing more than one columns
#     # print(df.iloc[i, [0, 2]])
