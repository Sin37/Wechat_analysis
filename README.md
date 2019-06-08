# Wechat_analysis

**这是一个基于wxpy库写成的小小程序**

目的在于拉取好友信息和群聊信息并储存在csv文件中以备进一步(mang)(mu)分析



### 使用

双击**wechat_analyse.exe**或使用 **python wechat_analyse.py** 运行

使用微信扫一扫扫描二维码登录

目录下会生成myGroups.csv 和 myFriends.csv两个csv文件



### myGroups.csv 包含

群名称	PUID	人数	群主呢称	群主群内名称



### myFriends.csv包含

昵称	备注名称	PUID	性别	省份	城市	共同群聊数量	签名



### Note

群聊不一定会拉取所有的群聊,有一些不活动的群聊可能会不被拉取

下一步可能会增加更多的统计数据 (咕咕咕)



### 致谢

@王悦	提出了这个需求