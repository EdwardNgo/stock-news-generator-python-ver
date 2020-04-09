import random
import numpy as np

class StockGenerator(object):
    
    def __init__(self,n):
        self.order = n
        self.ngram_context={}
        
    def generateDictFromText(self,data):
        wordDict=self.ngram_context
        k=self.order
        for i in range(len(data)-k):
            X = data[i:i+k]
            Y = data[i+k]
            if wordDict.get(X) is None:
                wordDict[X] = {}
                wordDict[X][Y] = 1
            elif wordDict[X].get(Y) is None:
                wordDict[X][Y] = 1
            else:
                wordDict[X][Y] = 1
        return wordDict
    
    def prob(self):
        wordDictFromText=self.generateDictFromText(data)
        for kx in wordDictFromText.keys():
            norm_factor = sum(wordDictFromText[kx].values())
            for val in wordDictFromText[kx].keys():
                wordDictFromText[kx][val] = wordDictFromText[kx][val]/norm_factor
        probdict=wordDictFromText
        return probdict
    
    def predict(self, text_input, probdict):
        if probdict.get(text_input) is None:
            return " "
        keys = list(probdict[text_input].keys())
        prob = list(probdict[text_input].values())
        print('ha')
        return np.random.choice(keys,p=prob)
        
        
    
    
if __name__ == "__main__":
    data=open('/home/viethoang/petproject/OOP/STOCKNEWS_GENERATOR/test.txt','r',encoding='utf-8').read().replace(u'\xa0', u' ')       

    generator = StockGenerator(4)
    probdict = generator.prob()
    # print(probdict)
    input_statement="lệ ổ"
    for _ in range(100):
        predicted_char = generator.predict(input_statement, probdict)
        input_statement+=predicted_char
    print(input_statement)