#coding:gbk
#目标:小项目Rock-paper-scissors-lizard-Spock
#作者:周雨果

#0-石头
#1-史波克
#2-纸
#3-蜥蜴
#4-剪刀
import random
def name_to_number(name): 
    if name=="石头":
       return 0
    elif name=="史波克":
       return 1
    elif name=="纸":
       return 2
    elif name=="蜥蜴":
       return 3
    elif name=="剪刀":
       return 4
    else:
       return "Error: No Correct Name"
 # 使用if/elif/else语句将各游戏对象对应到不同的整数  
def number_to_name(number):
    if number==0:
       return "石头"
    elif number==1:
       return "史波克"
    elif number==2:
       return "纸"
    elif number==3:
       return "蜥蜴"
    elif number==4:
       return "剪刀"
    else:
       return "Error: No Correct Name"
# 使用if/elif/else语句将不同的整数对应到游戏的不同对象 

def rpsls(player_choice):
#用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果   
    print ("你的选择是:",player_choice)
    player_number=name_to_number(player_choice) # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
    computer_number=random.randrange(0,5)    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
    computer_choice=number_to_name(computer_number) # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
    print ("计算机的选择是:",computer_choice)
    result=(computer_number-player_number)%5 #进行比较输赢的实质关系
    if result==1 or result==2:
       print("机器赢了")
    elif result==3 or result==4:
       print("您赢了")
    elif result==0:
  
       print("平局")
    else:
       print ("The wrong gam")
   # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

print("欢迎使用RPSLS游戏")
print("----------------")
choice_name=input("请输入您的选择:")
rpsls(choice_name)
input()
