#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import random

nyuryoku = input("入力: ")

def ojisan(nyuryoku):
    global ojisanb
    ojisana = re.sub("あなた|そちら|お宅|おたく|オタク|貴官|貴職|貴兄|貴姉|卿|貴君|お前|おまえ|君|きみ|てめえ|てめぇ|貴様|きさま|汝|そなた|其方|貴君|貴殿|貴公|お兄|お姉|おじさん|おばさん|おじいさん|おばあさん|親父|お袋|兄貴|姉貴|おじき|あねさん|おっさん|おばはん|爺|じじい|婆|ばばあ|先生|師匠|師|老師|お師|お師様|尊師|せんぱい|先輩|陛下|殿下|閣下|猊下|主上|おかみ|上様|殿|お殿|王|姫|姫様|お姫|ひい|御前|御前様|ごぜん|ごぜんさま|だん|ごりょん|ぼんち|いと|お客様|小僧|こぞう|小童|こわっぱ|小娘|こむすめ", "おじさん", nyuryoku)
    ojisanb = re.sub("\?|!|\？|！|。|、|な|ね|んだ", "", ojisana)
    return ojisanb

def zako(ojisanb):
    global zakoo

    ct = len(re.findall("雑魚|ざこ|ザコ", ojisanb))
    #print(ct)
    ojisanb = re.sub("雑魚|ざこ|ザコ", "zako", ojisanb)
    while ct >= 0:
        zakohantei = random.randint(0, 2)
        if zakohantei == 0:
            zakko = "ざっこ〜♥"
        elif zakohantei == 1:
            zakko = "ざぁ〜こ♥"
        elif zakohantei == 2:
            zakko = "ざこ♥"
        ojisanb = ojisanb.replace("zako", zakko, 1)
        ct = ct - 1
        #print(ct)
    zakoo = ojisanb
    return zakoo

def kimo(zakoo):
    global kimooo
    kimohantei = random.randint(0, 2)
    if kimohantei == 0:
        kimoo = "きもちわる～♥"
    elif kimohantei == 1:
        kimoo = "きも～い♥"
    elif kimohantei == 2:
        kimoo = "きも～♥"

    kimooo = re.sub("きも.|キモ.", kimoo, zakoo)
    return kimooo

def suru(kimooo):
    global syuryu
    kimohantei = random.randint(0, 2)
    if kimohantei == 0:
        kimoo = "するんだ～♥"
    elif kimohantei == 1:
        kimoo = "しちゃうんだ～♥"
    elif kimohantei == 2:
        kimoo = "しちゃうの～？♥"
    syuryu = re.sub("する|の|してんの", kimoo, kimooo)
    return syuryu

def keru(syuryu):
    global keryu
    kimohantei = random.randint(0, 2)
    if kimohantei == 0:
        kimoo = "けるんだ～♥"
    elif kimohantei == 1:
        kimoo = "けちゃうんだ～♥"
    elif kimohantei == 2:
        kimoo = "けちゃうの～？♥"
    keryu = re.sub("ける", kimoo, syuryu)
    return keryu

def yaba(keryu):
    global yabayaba
    yabayaba = re.sub("やば.|ヤバ.", "やっば～♥", keryu)
    return yabayaba

def main():
    ojisan(nyuryoku)
    zako(ojisanb)
    kimo(zakoo)
    suru(kimooo)
    keru(syuryu)
    yaba(keryu)
    print(yabayaba)
main()
