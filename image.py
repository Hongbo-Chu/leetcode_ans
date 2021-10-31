
# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()

    return int(data)




#先读图片





# numpy and scipy are available for use
import numpy
import scipy

class I2M:
    def __init__(self):
        self.a1 = get_number()
        self.b1 = get_number()
        self.mat1 = self.Image2vector(self.a1)
        self.a2 = get_number()
        self.b2 = get_number()
        self.mat2 = self.Image2vector(self.a2)
        # print(self.mat1)
        # print(self.mat2)
        self.bianli()


    def Image2vector(self,s):
        img = []
        for i in range(s):
            tt = input()
            temp = []
            for cha in tt:
                if cha == '.':
                    temp.append(0)
                else:
                    temp.append(1)
            img.append(temp)
        return img


    def turn90(self,data, i):

        kk = numpy.rot90(data, -1*i)
        return kk

    def bianli(self):#分别为两个矩阵的size
        max_res = 0
        if (self.a1*self.b1 < self.a2*self.b2):
            bigma = numpy.array(self.mat2)
            smama = numpy.array(self.mat1)
            sma = self.a1
            smb = self.b1
            bia = self.a2
            bib = self.b2
        else:
            bigma = numpy.array(self.mat1)
            smama = numpy.array(self.mat2)
            sma = self.a2
            smb = self.b2
            bia = self.a1
            bib = self.b1
        print(bigma)
        print("ss")
        print(smama)
        print("ss")
        i = 0
        while sma<bia:
            j = 0
            while smb<=bib:

                tempb = bigma[i:sma,j:smb]
                print(tempb)
                print("smb:")
                print(smb)
                for tur in range(4):
                    temps = self.turn90(smama,i)
                    kk = temps*tempb
                    res = kk.sum()
                    # print(res)
                    max_res = max(max_res,res)
                j+=1
                smb+=1
            i+=1
            sma+=1
            print("ddddd")
            print(sma)
            print(bia)


        self.maxres = max_res
        print(self.maxres)




I2M()