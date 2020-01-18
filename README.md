# Wechat Analysis

### Overview
This is a little program that utilized wxpy library to export your friend list and group chat into csv files. Exported files could be use for generating statistic reports or managing friend lists across multiple accounts.

### Usage
*If you are using Windows:*
1. run **wechat_analyse.exe**
2. Scan QR code to login

*Otherwise:*
1. use **python wechat_analyse.py** command to run
2. Scan QR code to login

### Exported Files

**myGroups.csv** includes:
Group chat name, PUID, Number of people in the chat, Owner's name, Owner's alias

**myFriends.csv** includes:
name, alias, PUID, gender, province, city, number of common group chat, headline

\* PUID is used as a thirdparty unique identifior for every user and group chat

### Future Works
1. statistic report generation
2. Word Cloud generation


wxpy reference: https://wxpy.readthedocs.io/zh/latest/index.html

Thanks @王悦 for inspired me to create such export tool.
