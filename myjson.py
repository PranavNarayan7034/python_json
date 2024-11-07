import json
import math
with open(r'C:\Users\prana\Downloads\phones\data.json','r')as f:
    data = json.load(f)
    new = []
    for i in data:
        p = i['price']
        if p!=None:
            if 'About' in p:
                a = p.split()
                b = a[1]
                if b.isdigit():
                    b = float(b)
                    # inr = f'{i["phone_brand"]}--{i["phone_model"]}--₹ {math.floor(b*90.48)}'
                    inr = {'phone_brand':i["phone_brand"],'phone_model':i["phone_model"],'price':math.floor(b*90.48)}
                    new.append(inr)
                    # print(inr)
            else:
                a = p.split('/')
                # print(a)
                for j in a:
                    if '₹' in j:
                        # inr = f'{i["phone_brand"]}--{i["phone_model"]}--{j}'
                        inr = {'phone_brand':i["phone_brand"],'phone_model':i["phone_model"],'price':j}
                        new.append(inr)
                        # print(inr)
                        break
                    elif '£' in j:
                        a = j.strip(' £')
                        b = float(a.replace(',',""))
                        c = math.floor(b*109.04)
                        # inr = f'{i["phone_brand"]}--{i["phone_model"]}--₹{c}'
                        inr = {'phone_brand': i["phone_brand"], 'phone_model': i["phone_model"],'price': c}
                        new.append(inr)
                        # print(inr)
                        break
                    elif '€' in j:
                        a = j.strip(' €')
                        b = float(a.replace(',', ""))
                        c = math.floor(b * 90.48)
                        # inr = f'{i["phone_brand"]}--{i["phone_model"]}--₹{c}'
                        inr = {'phone_brand': i["phone_brand"], 'phone_model': i["phone_model"],'price': j}
                        new.append(inr)
                        # print(inr)
                        break
                    elif '$' in j:
                        a = j.strip('AC$ ')
                        b = float(a.replace(',', ""))
                        c = math.floor(b *84.35)
                        # inr = f'{i["phone_brand"]}--{i["phone_model"]}--₹{c}'
                        inr = {'phone_brand': i["phone_brand"], 'phone_model': i["phone_model"],'price': j}
                        # print(inr)
                        new.append(inr)
                        break
    # print(new)
    with open('mobiles_inr.json','w')as w:
        json.dump(new,w,indent=1)