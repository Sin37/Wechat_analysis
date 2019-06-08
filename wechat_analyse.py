#!/usr/bin/python
# -*- coding: UTF-8 -*-
from wxpy import *
from os import remove
from pandas import DataFrame

try:
    os.remove("myFriends.csv")
    os.remove("myGroups.csv")
except:
    print("file not exist")

bot=Bot(cache_path=True)
bot.enable_puid(path='wxpy_puid.pkl')
friends=bot.friends()[1:]
groups=bot.groups()


NickName=[]
Remark=[]
Sex=[]
puid=[]
province=[]
city=[]
signature=[]

for friend in friends:
    NickName.append(friend.nick_name)
    Remark.append(friend.remark_name)
    puid.append(friend.puid)
    if (friend.sex==1):
        Sex.append('男')
    elif(friend.sex==2):
        Sex.append('女')
    elif(friend.sex==0):
        Sex.append('未知')
    province.append(friend.province)
    city.append(friend.city)
    signature.append(friend.signature)






group_names=[]
group_size=[]
group_puid=[]
group_owner_nickname=[]
group_owner_displayname=[]
for group in groups:
    group_names.append(group.name)
    group_size.append(len(group))
    group_puid.append(group.puid)
    group_owner_nickname.append(group.owner.nick_name)
    group_owner_displayname.append(group.owner.display_name)
    # for member in group:

shared_groups=[]
for friend in friends:
    count=0
    for group in groups:
        if friend in group:
            count=count+1
    shared_groups.append(count)

group_data={'群名称':group_names,'PUID':group_puid,'人数':group_size,'群主呢称':group_owner_nickname,'群主群内名称':group_owner_displayname}
frame = DataFrame(group_data)
frame.to_csv('myGroups.csv',encoding='utf_8_sig')

friend_data={'昵称' : NickName,'备注名称': Remark,'PUID':puid, '性别' : Sex,'省份':province,'城市':city,'共同群聊数量':shared_groups,'签名':signature}
frame = DataFrame(friend_data)
frame.to_csv('myFriends.csv',encoding='utf_8_sig')