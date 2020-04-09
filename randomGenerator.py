
import string
import random
import math
import collections
from pyvi import ViTokenizer


#--------------------------------------------------------------------
# Function:     tokenize(text)
# Objection:    to tokenize a sentence - break down a sentence in words
# Input:        a sentence in string
# Output:       a word(symbol) list
def tokenize(text):
    token_list = ViTokenizer.tokenize(text).split(' ')
    return token_list
print(tokenize(content))

#--------------------------------------------------------------------
# Function:     ngrams(n,tokens)
# Objection:    to make ngram features
# Input:        a token list from a sentence
# Output:       ngram features of the input sentence
def ngrams(n, tokens):
    tokens+=["<END>"]
    result=[]
    for i in range(len(tokens)):
        prev=[]
        for j in range(1,n):
            if (i-j) < 0: prev.append("<START>")
            else:         prev.append(tokens[i-j])
        prev.reverse()
        result.append((tuple(prev),tokens[i]))
    return result
print(ngrams(3,tokenize(content)))


class NgramModel(object):

    def __init__(self, n):
        self.order=n
        self.ngrams_context={}

    #--------------------------------------------------------------------
    # Function:     update(sentence)
    # Objection:    the update is a learning process which would update the Markov Model by feeding new sentence
    # Input:        new sentence
    # Output:       ?
    def update(self, sentence):
        ngrams_list=ngrams(self.order,tokenize(sentence))

        for item in ngrams_list:
            if str(item[0]) not in self.ngrams_context:
                self.ngrams_context[str(item[0])]={}
                self.ngrams_context[str(item[0])][item[1]]=1
            else:
                if item[1] not in self.ngrams_context[str(item[0])]:
                    self.ngrams_context[str(item[0])][item[1]]=1
                else:
                    self.ngrams_context[str(item[0])][item[1]]+= 1

    def get_info(self):
        print (self.ngrams_context)
    #--------------------------------------------------------------------
    # Function:     prob
    # Objection:    the update is a learning process which would update the Markov Model by feeding new sentence
    # Input:        new sentence
    # Output:       ?
    def prob(self, context, token):
        key = str(context)
        if key not in self.ngrams_context:
            return 0
        env=self.ngrams_context[key].copy()
        if token not in env:
            return 0
        return float(env[token])/sum([env[i] for i in env])

    #--------------------------------------------------------------------
    # Function:     random_token
    # Objection:    This function will pickup a random token from context
    # Input:        context
    # Output:       a token
    def random_token(self, context):
        r=random.random()
        env=self.ngrams_context[str(context)].copy()
        token_list=list(env)
        token_list.sort()
        #token_list=collections.OrderedDict(env)
        env_sum=sum([env[i] for i in env])
        sum1=0
        for i in range(len(token_list)):
            sum1+=env[token_list[i]]/float(env_sum)
            if (sum1>r):
                return token_list[i]



    #--------------------------------------------------------------------
    # Function:     random_text
    # Objection:    to generate a random sentence
    # Input:        the token count
    # Output:       the random sentence
    def random_text(self, token_count):
        result=[]
        start=["<START>"]*(self.order-1)
        next=start
        print(next)
        for i in range(token_count):
            result.append(self.random_token(tuple(next)))
            if result[-1] == "<END>":
                next=["<START>"]*(self.order-1)
            elif next != []:
                next.pop(0)
                next.append(result[-1])

        return " ".join(result)

def create_ngram_model(n, path):
    nm=NgramModel(n)
    # nm.get_info()
    with open(path) as file:
        for line in file:
            nm.update(line)
    print(nm.random_token(('HNX', 'giảm', 'mạnh')))
    # nm.get_info()
    # print(nm.prob(('HNX', 'giảm', 'mạnh'),'đến'))
    return nm
if __name__ == "__main__":
    # myGenerator= randomGenerator.create_ngram_model(4,"/home/viethoang/petproject/OOP/STOCKNEWS_GENERATOR/vnexpress_crawler/new.txt")
    myGenerator= create_ngram_model(4,"/home/viethoang/petproject/OOP/STOCKNEWS_GENERATOR/test.txt")
    contents=myGenerator.random_text(500).split('<END>')
    print(content)
