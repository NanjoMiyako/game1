import datetime
import time
import random

riverBreadth = 0;
forestBreadth = 0;
seaBreadth = 0;
desertBreadth = 0;
planeBreadth = 0;
craterBreadth = 0;

UserExp = 0;

prevCmdTime = datetime.datetime.now() - datetime.timedelta(minutes = 60);
prevCmd = 0;

nextCmdExecTime = datetime.datetime.now() - datetime.timedelta(minutes=60);

searchCostTime = 1;

def cmdSts(cmdNo, subVal):
	retVal = ""
	if cmdNo == 1:
		retVal = "島の探索"
	elif cmdNo == 2:
		retVal = "休息"
	elif cmdNo == 3:
		retVal = "移動"
	elif cmdNo == 4:
		retVal = "セーブデータロード"
	elif cmdNo == 5:
		retVal = "時刻の更新"
	elif cmdNo == 6:
		retVal = "パラメータの確認"
	else:
		retVal = ""
		
	return retVal

def init():
	global riverBreadth
	global forestBreadth
	global seaBreadth
	global desertBreadth
	global planeBreadth
	global craterBreadth
	
	riverBreadth = 0;
	forestBreadth = 0;
	seaBreadth = 0;
	desertBreadth = 0;
	planeBreadth = 0;
	craterBreadth = 0;
	
	global UserExp;
	
	UserExp = 0;
	
def searchIsland():
	global riverBreadth
	global forestBreadth
	global seaBreadth
	global desertBreadth
	global planeBreadth
	global craterBreadth
	
	rndIdx1 = random.randint(0,5);
	rndIdx2 = random.randint(1,10);

	searchedArea = "";
	
	if rndIdx1 == 0:
		searchedArea = "川"
		riverBreadth += rndIdx2
		
	elif rndIdx1 == 1:
		searchedArea = "森"
		forestBreadth += rndIdx2
		
	elif rndIdx1 == 2:
		searchedArea = "海"
		seaBreadth += rndIdx2
		
	elif rndIdx1 == 3:
		searchedArea = "砂漠"
		desertBreadth += rndIdx2
		
	elif rndIdx1 == 4:
		searchedArea = "平地"
		planeBreadth += rndIdx2
		
	elif rndIdx1 == 5:
		searchedArea = "火口"
		craterBreadth += rndIdx2
		
	msg = searchedArea + "を発見した!(広さ:" + str(rndIdx2) + ")" 
	print(msg);
	
def execCmd(cmd):
	global prevCmd
	global prevCmdTime
	global searchCostTime
	global nextCmdExecTime
	
	CmdTime = datetime.datetime.now();

	
	if prevCmd == 1:
		if prevCmdTime + datetime.timedelta(minutes = searchCostTime) <= CmdTime:
			print("---")
			print("島の探索が完了しました")
			
			searchIsland()
			prevCmd = 0
			
			print("---");
	
	if(nextCmdExecTime > CmdTime and cmd != 5):
		print("---")
		
		CmdSts = cmdSts(prevCmd, "")
		msg = "まだ" + CmdSts + "中です"
		print(msg);
		
		if prevCmd == 1:
			diffTime = CmdTime - prevCmdTime;
			diffSec = (60 * searchCostTime) - diffTime.seconds;
			msg = "あと" + str(diffSec)
			msg += "秒ほどかかります"
			print(msg)
			
		elif prevCmd == 2:
	 		print("test")
		
		print("---")
		
		return
	
	if cmd == 1:
		if nextCmdExecTime <= CmdTime:
			prevCmd = 1;
			print("---")
			msg = "島を探索します" + str(searchCostTime) + "分ほどかかります";
			print(msg)
			prevCmdTime = CmdTime;
			nextCmdExecTime = CmdTime + datetime.timedelta(minutes = searchCostTime)

			
	elif cmd == 5:
		print("---")
		msg = "現在時刻:"+ str(CmdTime)
		print(msg);
		
		diffTime = CmdTime - prevCmdTime;
		msg = "前回のコマンドからの経過秒:" + str(diffTime.seconds);
		print(msg);
		
	
	print("---")


exitFlg = False
print("---START---")

init()
while exitFlg == False:

	print("何をしますか")
	print("1:島を探索, 2: 休息をとる, 3:移動")
	print("4:セーブデータをロード, 5:時刻を更新")
	print("6:パラメータの確認")
	print("99:終了")
	
	#str = "userExp:" + str(UserExp)
	#print(str);
	
	value = input()
	value = int(value)

	if value == 99:	
		exitFlg = True
	else:
		execCmd(value)

print("---END---")


