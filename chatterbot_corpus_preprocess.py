#coding=utf-8
import yaml
import os
import pickle

DATA_DIR = "./data/chatterbot/"
OUTPUT_FILE = "./data/chatterbot.pkl"

def read_conversion(path):
	# 读取对话
	path = os.path.join(DATA_DIR, path)
	# print(path)
	with open(path, 'r',encoding='utf-8') as f:
		yaml_file = yaml.load(f.read())
		questions = []
		answers = []
		conversations = yaml_file['conversations']
		# print(conversations)
		print("nums of conversations:", len(conversations))
		for conv in conversations:
			conv_len = len(conv)
			# 对话并不是只有两句
			if len(conv) % 2 != 0:
				# only think double qa
				conv_len = len(conv) - 1
				#  make the last 2th an question
				questions.append(conv[-2])
				#  make the last one an answer
				answers.append(conv[-1])
		
			for i in range(conv_len):
				if i % 2 == 0:
					questions.append(conv[0])
				else:
					answers.append(conv[1])    
		return questions, answers
        
def list_file():
	# 列出所有对话文件
	filelist = os.listdir(DATA_DIR)
	return filelist

def saveQA(questions, answers):
	# 转储成pkl文件，直接保存list方便
	f = open(OUTPUT_FILE,'wb')
	pickle.dump((questions, answers), f)
	f.close()
	print("dump finish")

if __name__ == "__main__":
	# load all file
	files = list_file()

	questions = []
	answers = []
	for file_path in files:
		Q, A = read_conversion(file_path)
		questions.extend(Q)
		answers.extend(A)
	saveQA(questions, answers)
	print("nums of questions:{0:d},nums of answers:{1:d}".format(len(questions), len(answers)))