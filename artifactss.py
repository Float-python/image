import discord
from discord.ext import commands

from PIL import Image
import cv2
from pyocr import builders
import pyocr
import os,re,math

def type_judge(image_path):
    im = cv2.imread(image_path)
    h, w, _ = im.shape
    x = (h,w)
    match x:
        case (1920,1080):
            return 0 #PC


def image_type(device_type,image_path):

    def recognize(crop):
        

    

    


class Evaluate_Artifacts():
    
    def __init__(self,device,type):
        self.device = device
        self.type = type


    def image_ocr(self):
        #>build & ocr
        path_tesseract = "C:\\Program Files\\Tesseract-OCR"
        if path_tesseract not in os.environ["PATH"].split(os.pathsep):
            os.environ["PATH"] += os.pathsep + path_tesseract

            
        tools = pyocr.get_available_tools()
        print(tools)
        tool = tools[0]

        img_org = Image.open("./Image/atf.png")
        trim_img = img_org.crop((1272,209,1792,432))
        ocr_img = trim_img.convert('L')

        builder = pyocr.builders.TextBuilder()
        result = tool.image_to_string(ocr_img, lang="jpn", builder=builder)
        result = [i for i in result.split('\n')if i != '']
        return result

        #---------------

        #>convert data
    def convert_data(self):
        data = self.image_ocr()
        conv = []
        for r in data:
            if '%' in r:
                s = re.sub(r"[^\d.]", "", r)
                conv.append((s,True))
            else:
                conv.append((r,False))



        def maybe_float(s):#change type
            try:
                return float(s)
            except (ValueError, TypeError):
                return s

        conv = [(maybe_float(v[0]),v[1]) for v in conv]


        print(conv)
        res = dict()

        #conv→[(opt or value,%judge T or F),(),(),...]
        #res → {opt:(value,T or F),...}
        for i in range(5):
            res[conv[i][0]] = (conv[i+5][0],conv[i+5][1])
        print(res)
        return res

    def culculate_score(self,base=0):
        """Baseは0が攻撃力,1が防御,2がHP,3が元チャ"""

        data = self.convert_data()

        main = list(data.keys())[0]
        main_score = f'{data[main][0]}%' if data[main][1] else f'{data[main][0]}'
        
        score = 0
        base_dict = ['攻撃力','防御力','HP','元素チャージ']

        del data[main]

        sub_op = data.keys()
        n = base_dict[base]

        if n in sub_op:
            if data[n][1]:
                score += data[n][0]
        if "会心率" in sub_op:
            score += data["会心率"][0]*2
        if "会心ダメージ" in sub_op:
            score += data["会心ダメージ"][0]

        return [round(score,1),data,main,main_score]


a = Evaluate_Artifacts('a','b')
type_judge('./Image/atf.png')
print(a.culculate_score(0))

"""def culculate_score(self,detail:dict):"""
        
