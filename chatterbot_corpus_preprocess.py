#coding=utf-8
import yaml
import os
import pickle

DATA_DIR = "./data/chatterbot/"
OUTPUT_FILE = "./data/chatterbot.pkl"

def read_conversion(path, questions, answers):
	# 读取对话
	path = os.path.join(DATA_DIR, path)
	print(path)
	with open(path, 'r',encoding='utf-8') as f:
		yaml_file = yaml.load(f.read())
		conversations = yaml_file['conversations']
		# print(conversations)
		print("nums of conversations:", len(conversations))
		for conv in conversations:
			# 对话并不是只有两句
			assert len(conv) == 2
			questions.append(conv[0])
			answers.append(conv[1])    
		return questions, answers
        
def list_file():
	# 列出所有对话文件
	filelist = os.listdir(DATA_DIR)
	return filelist

def saveQA(questions, answers):
	# 转储成pkl文件，直接保存list方便
	pickle.dump((questions, answers), OUTPUT_FILE)

if __name__ == "__main__":
	files = list_file()
	questions = []
	answers = []
	for file_path in files:
		Q, A = read_conversion(file_path, questions, answers)
		questions.extend(Q)
		answers.extend(A)
	saveQA(questions, answers)