import random
import datetime


def shutudai(qa_lst):
    qa= random.choice(qa_lst)
    print("問題:" + qa["q"])
    return qa["a"]

def kaitou(ans_list):
    st = datetime.datetime.now()
    ans = input("答えるんだ：")
    ed = datetime.datetime.now()
    if ans in ans_list:
        print("正解！！")
    else:
        print("出直してこい")
    print("回答時間:"+str((ed-st).seconds)+"秒")

if __name__ == "__main__":
    qa_lst = [
        {"q":"サザエの旦那の名前は?","a":["マスオ","ますお"]},
        {"q":"カツオの妹の名前は?","a":["わかめ","ワカメ"]},
        {"q":"たらおはカツオから見てどんな関係?","a":["甥","おい","甥っ子","おいっこ"]}
    ]

    ans_list = shutudai(qa_lst)
    kaitou(ans_list)