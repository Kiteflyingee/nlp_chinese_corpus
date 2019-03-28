#coding=utf-8

from tqdm import tqdm
from util import saveQA, read_conversation

FILE_PATH = r"./data/xiaohuangji-40w/xiaohuangji50w_nofenci.conv"
OUTPUT_FILE = r"./data/xiaohuangji.pkl"

def read_convs():

    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        conversations = []
        # 用一个标记来判断是否是一整个对话，因为小通可能连续说两句以上的话
        is_conversation = False
        # 明确该数据集不是多轮对话
        is_conversation = False
        lines = f.readlines()
        conv = []
        for line in tqdm(lines):
            if line.startswith('E'):
                is_conversation = not is_conversation
                if len(conv) > 0:
                    conversations.append(conv)
                    conv = []
                continue
            else:
                if is_conversation:
                    line = line.replace('\n','')
                    if line.startswith('M'):
                        conv.append(line[2:])
                    else:
                        conv.append(line)
        conversations.append(conv)

        return conversations


if __name__ == "__main__":
    conversations = read_convs()
    questions, answers = read_conversation(conversations)
    saveQA(OUTPUT_FILE, questions, answers)