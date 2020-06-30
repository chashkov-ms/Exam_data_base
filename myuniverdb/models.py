from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """
    Class for Students
    """
    __tablename__ = "Student"
    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String(255))
    last_name = Column('last_name', String(255))
    group_id = Column('group_id', Integer, ForeignKey('FGroup.id'), nullable=True)

    exam_records = relationship('Exam_record')

    def __init__(self, first_name, last_name, group=None):
        self.first_name = first_name
        self.last_name = last_name
        if group is not None:
            self.group = group
    def __repr__(self):
        return '%s %s' % (self.first_name, self.last_name)

class FGroup(Base):
    """
    Class for Group
    """
    __tablename__ = "FGroup"
    id = Column('id', Integer, primary_key=True)
    number = Column('number', Integer)
    faculty_id = Column('faculty_id', Integer, ForeignKey('Faculty.id'), nullable=True)

    students = relationship('Student')

    def __init__(self, number, faculty=None):
        self.number = number
        if faculty is not None:
            self.faculty = faculty
    def __repr__(self):
        return 'Group # %s' % (self.number)

class Faculty(Base):
    """
    Class for Faculty
    """
    __tablename__ = "Faculty"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255))

    groups = relationship('FGroup')
    hr_records = relationship('HR_record')

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Faculty # %s' % (self.number)

class Exam(Base):
    """
    Class for Exam
    """
    __tablename__ = "Exam"
    id = Column('id', Integer, primary_key=True)
    discipline = Column('discipline', String(255))
    staff_id = Column('staff_id', Integer, ForeignKey('Staff.id'), nullable=True)

    exam_records = relationship('Exam_record')

    def __init__(self, discipline, staff = None):
        self.discipline = discipline
        if staff is not None:
            self.staff = staff
    def __repr__(self):
        return 'Faculty # %s' % (self.number)

class Staff(Base):
    """
    Class for Staff
    """
    __tablename__ = "Staff"
    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String(255))
    last_name = Column('last_name', String(255))

    exams = relationship('Exam')
    hr_records = relationship('HR_record')

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '%s %s' % (self.first_name, self.last_name)

class HR_record(Base):
    """
    Class for HR-record
    """
    __tablename__ = 'HR_record'
    id = Column('id', Integer, primary_key=True)
    position = Column('position', String(255))
    staff_id = Column('staff_id', Integer, ForeignKey('Staff.id'), nullable=True)
    faculty_id = Column('faculty_id', Integer, ForeignKey('Faculty.id'), nullable=True)

    def __init__(self, position, staff=None, faculty=None):
        self.position = position
        if staff is not None:
            self.staff = staff
        if faculty is not None:
            self.faculty = faculty
    def __repr__(self):
        return '%s' % (self.position)


class Exam_record(Base):
    """
    Class for HR-record
    """
    __tablename__ = 'Exam_record'
    id = Column('id', Integer, primary_key=True)
    date = Column('date', String(255))
    grade = Column('grade', Integer)
    exam_id = Column('exam_id', Integer, ForeignKey('Exam.id'), nullable=True)
    student_id = Column('student_id', Integer, ForeignKey('Student.id'), nullable=True)

    def __init__(self, date, grade, exam=None, student=None):
        self.date = date
        self.grade = grade
        if exam is not None:
            self.exam = exam
        if student is not None:
            self.student = student
    def __repr__(self):
        return 'Date: %s Grade: %s' % (self.date, self.grade)


