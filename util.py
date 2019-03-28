#coding=utf-8
import pickle
import re

def saveQA(OUTPUT_FILE, questions, answers):
	# 转储成pkl文件，直接保存list方便
	f = open(OUTPUT_FILE,'wb')
	pickle.dump((questions, answers), f)
	f.close()
	print("dump finish")


def read_conversation(conversations):
	'''
	把对话数组分拆成问答对
	'''
	# 读取对话
	questions = []
	answers = []
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

# def bad_conversation(question, answer):

def regular(sen):
    """整理句子"""
    sen = re.sub(r'\.{3,100}', '…', sen)
    sen = re.sub(r'…{2,100}', '…', sen)
    sen = re.sub(r'[,]{1,100}', '，', sen)
    sen = re.sub(r'[\.]{1,100}', '。', sen)
    sen = re.sub(r'[\?]{1,100}', '？', sen)
    sen = re.sub(r'[*]{1,100}', '！', sen)
    sen = re.sub(r'[@]{2,}', '！', sen)
    sen = re.sub(r'[#]{2,}', '！', sen)
    sen = re.sub(r'[￥|$]{1,}', '！', sen)
    sen = re.sub(r'[|\^]{2,}', '！', sen)
    sen = re.sub(r'[|\&]{2,}', '！', sen)
    sen = re.sub(r'[|\*]{2,}', '！', sen)
    sen = re.sub(r'[!]{2,100}', '！', sen)
    sen = re.sub(r'[！]{2,100}', '！', sen)
    return sen