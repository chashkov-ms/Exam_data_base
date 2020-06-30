# -*- coding: cp1251 -*-
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import *

DB_NAME = r'univer_network.db'
# Открываем базу данных
engine = create_engine('sqlite:///%s' % DB_NAME)
Session = sessionmaker(bind=engine)
session = Session()

# Делаем тестовые запросы
len1 = len(session.query(Student).join(Exam_record).all())
len2 = len(session.query(Exam_record).join(Exam).filter(Exam.discipline.like('Math')).all())
len3 = len(session.query(Exam_record).join(Exam).join(Staff).filter(Staff.last_name.like('Gavrilova')).all())

# Печатаем результат для проверки
print(len1*len2*len3)