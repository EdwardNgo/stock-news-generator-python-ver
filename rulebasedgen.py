import pandas as pd
import random as rand
import math


class Generator():



    def __init__(self,verbs_set,adverbs_set):
        self.verbs_set = verbs_set
        self.adverbs_set = adverbs_set

    def general_rule(self,day):
        basic_rule = self.adverbs_set + day +", " + "VN-INDEX "

        rule_1 = basic_rule + self.verbs_set + str(finalPrice) + ' điểm'
        rule_2 = basic_rule + self.verbs_set + str(finalPrice) + ' điểm, ' + Generator.ruleset(changed_point) + changed_point_str + " điểm"
        rule_3 = basic_rule + Generator.ruleset(changed_point) + changed_point_str + " điểm thành " + str(finalPrice)+ ' điểm'

        return rule_3,rule_1,rule_2

    def compare(self, day_1, day_2):
        rule = "VN-INDEX " + "ngày " + day_1 + Generator.ruleset(diff) + str(round(abs(diff),2)) + " điểm so với ngày " + day_2
        return rule


    @staticmethod
    def ruleset(change):
        if change > 0:
            return " tăng "
        else:
            return ' giảm '

if __name__ == "__main__":

    df = pd.read_csv("stockdata.csv")
    df_height = df.shape[0]
    randomNumber = rand.randint(0,df_height-1)

    adverbs_set = rand.choice(["Kết thúc phiên giao dịch ","Kết phiên ","Sau phiên hôm nay ","Đóng cửa ","Kết phiên chiều ","Kết phiên sáng ","Kết thúc ngày giao dịch ","đóng cửa thị trường tại ","Tại giờ đóng cửa"])
    verbs_set = rand.choice(["đóng cửa tại ","đóng cửa thị trường tại ","dừng ở ","đạt mức ","tạm dừng ở "])
    day = df['Date'][randomNumber]
    finalPrice = df['FinalPrice'][randomNumber]
    changed_point = float(df['Change'][randomNumber].split(' ')[0])
    changed_point_str = str(abs(changed_point))

    newGenerator = Generator(verbs_set,adverbs_set)
    text = newGenerator.general_rule(day)
    print(text[1])
    day_1 = df['Date'][randomNumber]
    day_2 = df['Date'][randomNumber + 1]
    price_1 = df[df['Date'] == day_1]['FinalPrice']
    price_2 = df[df['Date'] == day_2]['FinalPrice']
    diff = float(price_1) - float(price_2)

    text_0 = newGenerator.compare(day_1,day_2)
    print(text_0)
