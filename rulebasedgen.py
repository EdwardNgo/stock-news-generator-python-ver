import pandas as pd
import random as rand

def ruleset():
    if float(df['Change'][randomNumber].split(' ')[0]) > 0:
        return "tăng "
    else:
        return 'giảm '
class Generator():
    def __init__(self):
        pass
    def general_rule(self):
        basic_rule = adverbs_set + day +", " + "VN-INDEX "
        rule_1 = basic_rule + verbs_set + str(finalPrice) + ' điểm'
        rule_2 = basic_rule + verbs_set + str(finalPrice) + ' điểm, ' + ruleset() + changed_point + " điểm"
        rule_3 = basic_rule +ruleset() + changed_point + " điểm thành " + str(finalPrice)+ ' điểm'
        return rule_3,rule_1,rule_2
    def price_rule(self):
        pass

if __name__ == "__main__":
    df = pd.read_csv("stockdata.csv")
    df_height = df.shape[0]
    adverbs_set = rand.choice(["Kết thúc phiên giao dịch ","Kết phiên ","Sau phiên hôm nay ","Đóng cửa ","Kết phiên chiều ","Kết phiên sáng ","Kết thúc ngày giao dịch ","đóng cửa thị trường tại "])
    verbs_set = rand.choice(["đóng cửa tại ","đóng cửa thị trường tại ","dừng ở ","đạt mức "])
    state_verbs = ('tăng','giảm')
    randomNumber = rand.randint(0,df_height-1)
    day = df['Date'][randomNumber]
    finalPrice = df['FinalPrice'][randomNumber]
    changed_point = str(abs(float(df['Change'][randomNumber].split(' ')[0])))
    newGenerator = Generator()
    text = Generator().general_rule()
    print(text)
