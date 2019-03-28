#coding=utf-8

from util import *
import re


FILE_PATH = r"./data/qingyun-11w/12万对话语料青云库.csv"
OUTPUT_FILE = r"./data/qingyun.pkl"

def fix_sequence(sequence):
    '''
    去除句子中的一些非法字符
    '''
    sequence = sequence.strip()
    pattern = r"\{.*\}"
    sequence = re.sub(pattern, '', sequence)
    sequence=regular(sequence)
    return sequence


def read_file(file):
    with open(file, 'r', encoding="utf-8") as f:
        conversations = []
        lines = f.readlines()
        # 每行是一段对话，以|分割
        for conv in lines:
            conv = conv.split(r"|")
            newconv = []
            for seq in conv:
                newconv.append(fix_sequence(seq))
            conversations.append(newconv)
        return conversations

if __name__ == "__main__":
    conversations = read_file(FILE_PATH )
    questions, answers = read_conversation(conversations)
    saveQA(OUTPUT_FILE, questions, answers)
    print("questions:{0}, answers:{1}"\
                            .format(len(questions), len(answers)))
