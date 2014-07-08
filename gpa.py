import urllib2
import re

subjects = ['0821101','0821102','0121019','0241001',
			'0341001','0341002','0341003','0341022',
			'0721001','0241006','0341006','0341007',
			'0341008','0341009','0341011','0341012',
			'0341013','0341014','0341015','0341016',
			'0341017','0341018','0341020','0341024',
			'0341029','0342209']

def production(series, subject):
	targtUrl = 'http://210.27.12.1:90/queryDegreeScoreAction.do?studentid=xdleess20130621zq%s&degreecourseno=%s'%(series,subject)
	content = urllib2.urlopen(targtUrl).read()
	match = re.findall('<td width="7%" align="left">(.+?)</td>', content, re.S)
	if match:
		num = match[1].strip()
		if len(num) == 0:
			return (0, 0, False)
		print subject + ' -> ' + num
		score = float(match[1].strip())
		#score = float(num)
		credit = float(match[2].strip())
		return (score*credit, credit, True)
	else:
		return (0, 0, False)

def average(series):
	scores = 0
	credits = 0
	for i in range(len(subjects)):
		(midscores,credit,exist) = production(series, subjects[i])
		if exist:
			scores += midscores
			credits += credit
	#	else:
			#print 'not chosen'
	if credits:
		ave = scores / credits
	else:
		return 0
	#print 'Your average score: %.2f'%ave
	return ave

def main():
	length = len(subjects)
	for i in range(length):
		if subjects[i][2] == '2':
			continue
		else:
			apd=subjects[i][0:2] + '2' + subjects[i][3:]
		subjects.append(apd)

	allScores = []
	for series in range(1755, 1903):
		if (series+21) == 1902:
			ave = average(str(series))
			stuID = '130312' + str(series+21)
			print stuID + '\t-> %.2f'%ave
			allScores.append((ave, stuID))

	#f = open("rank.txt", "w")
	#rank = 1
	#allScores.sort()
	#for item in allScores:
	#	print >> f, str(rank) + '\t' + item[1] + '\t-> %.2f'%item[0]
	#	rank += 1
	#f.close()

if __name__ == '__main__':
	main()
