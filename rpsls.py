#coding:gbk
#Ŀ��:С��ĿRock-paper-scissors-lizard-Spock
#����:�����

#0-ʯͷ
#1-ʷ����
#2-ֽ
#3-����
#4-����
import random
def name_to_number(name): 
    if name=="ʯͷ":
       return 0
    elif name=="ʷ����":
       return 1
    elif name=="ֽ":
       return 2
    elif name=="����":
       return 3
    elif name=="����":
       return 4
    else:
       return "Error: No Correct Name"
 # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������  
def number_to_name(number):
    if number==0:
       return "ʯͷ"
    elif number==1:
       return "ʷ����"
    elif number==2:
       return "ֽ"
    elif number==3:
       return "����"
    elif number==4:
       return "����"
    else:
       return "Error: No Correct Name"
# ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ���� 

def rpsls(player_choice):
#�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��   
    print ("���ѡ����:",player_choice)
    player_number=name_to_number(player_choice) # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    computer_number=random.randrange(0,5)    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    computer_choice=number_to_name(computer_number) # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    print ("�������ѡ����:",computer_choice)
    result=(computer_number-player_number)%5 #���бȽ���Ӯ��ʵ�ʹ�ϵ
    if result==1 or result==2:
       print("����Ӯ��")
    elif result==3 or result==4:
       print("��Ӯ��")
    elif result==0:
  
       print("ƽ��")
    else:
       print ("The wrong gam")
   # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
choice_name=input("����������ѡ��:")
rpsls(choice_name)
input()
