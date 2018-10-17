#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:38:31 2018

@author: hanbo
"""

class student(object):
    '''self-defined class: student
        attributes: name, age, gender, class_no, program, courses, grades, level
        method: gets, sets, addCourses, delCourses, addGrades, getGrades'''
    def __init__(self,name="name",age="age",gender="gender",class_no="SXCX",courses=['courses'],grades=[],level={}):
        self.name=name
        self.age=age
        self.gender=gender
        self.class_no=class_no
        self.courses=courses
        self.grades=[]
        self.level={}
    def getName(self):
        '''Get the name'''
        return self.name
    def getAge(self):
        '''Get the age'''
        return self.age
    def getGender(self):
        '''Get the gender'''
        return self.gender
    def getClass_no(self):
        '''Get the class number'''
        return self.class_no
    def getCourses(self):
        '''Get the courses that have taken'''
        return self.courses
    def getProgram(self):
        x=int(self.class_no[-1])
        if x in [8,9]:
            return 'AP'
        elif x in [1,2,3,4,5]:
            return 'AL'
        elif x in [6,7]:
            return 'IB'
    def setName(self,newName):
        '''Set student's name'''
        self.name=newName
    def setAge(self,age):
        '''Set student's name'''
        self.age=age
    def setGender(self,gender):
        '''Set student's gender'''
        self.gender=gender
    def setClass_no(self,No):
        '''Set student's class number
            "No": str -> class number (defalt SXCX)'''
        self.class_no=No
    def addCourses(self,newCourse):
        '''Add one new course to the student'''
        self.courses.append(newCourse)
        return self.courses
    def delCourses(self,delCourse):
        '''Delete a existing course of the student'''
        try:
            self.courses.remove(delCourse)
        except ValueError:
            print("No such course")
        return self.courses
    def addGrades(self):
        '''Add grades to all courses'''
        x=len(self.courses)
        if not x==0:
            for i in range(x):
                addgrade=int(input(self.courses[i]+": "))
                self.grades.append(addgrade)
        return self.grades
    def getGrades(self):
        '''Get the level of grades'''
        n=len(self.grades)
        for i in range(n):
            g=self.grades[i]
            if g>=85:
                self.level.update({self.courses[i]:'A'})
            elif g>=75:
                self.level.update({self.courses[i]:'B'})
            elif g>=60:
                self.level.update({self.courses[i]:'C'})
            else:
                self.level.update({self.courses[i]:'D'})
        return self.level
    
def test():
    a=student('Hanbo','17','Male','S2C7',['Math','Eng','Econ','CS'])
    a.addGrades()
    data={
            'Name':a.getName(),
            'Age':a.getAge(),
            'Gender':a.getGender(),
            'Class':a.getClass_no(),
            'Program':a.getProgram(),
            'Courses':a.getCourses(),
            'Grades':a.getGrades()
            }
    return data

