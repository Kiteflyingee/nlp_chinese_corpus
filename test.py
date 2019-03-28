#coding=utf-8

import pickle

f = open(r"./data/chatterbot.pkl",'rb')
questions, answers=pickle.load(f)
print(len(questions), len(answers))
print(questions[19:25])
print(answers[19:25])