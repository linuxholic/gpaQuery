#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import re
import sys

subjects = [('0821101','中国特色'),
			('0821102','自然辩证法概论'),
			('0121019','有限域及其应用'),
			('0241001','矩阵论'),
			('0341001','计算机科学使用的数理逻辑'),
			('0341002','组合数学'),
			('0341003','数论算法'),
			('0341022','工程优化算法'),
			('0721001','随机过程'),
			('0241006','数字信号处理(二)'),
			('0341006','计算机网络(二)'),
			('0341007','人工智能'),
			('0341008','模式识别'),
			('0341009','数字图像处理'),
			('0341011','面向对象技术'),
			('0341012','算法分析与设计'),
			('0341013','分布处理系统'),
			('0341014','形式语言与自动机'),
			('0341015','网络安全'),
			('0341016','计算机系统结构(二)'),
			('0341017','计算机图形学'),
			('0341018','计算机控制'),
			('0341020','基于互联网的计算'),
			('0341024','软件体系结构'),
			('0341029','人工神经网络基础'),
			('0342209','软件工程'),
			('0821005','英语学位考试')]

def production(series, subject):
	targtUrl = 'http://210.27.12.1:90/queryDegreeScoreAction.do?studentid=xdleess20130621zq%s&degreecourseno=%s'%(series,subject[0])
	content = urllib2.urlopen(targtUrl).read()
	match = re.findall('<td width="7%" align="left">(.+?)</td>', content, re.S)
	if match:
		num = match[1].strip()
		if len(num) == 0:
			return (0, 0, False)
		print subject[1] + '\t(%s)'%subject[0] + '\t-> ' + num
		score = float(match[1].strip())
		credit = float(match[2].strip())
		return (score*credit, credit, True)
	else:
		return (0, 0, False)

def average(series):
	scores = 0
	credits = 0
	print
	for i in range(len(subjects)):
		(midscores,credit,exist) = production(series, subjects[i])
		if exist:
			scores += midscores
			credits += credit
	if credits:
		ave = scores / credits
	else:
		ave = 0
	print
	print '\tYour average score: %.2f'%ave
	print

def usage():
	print
	print 'usage:'
	print '\tpython gpa.py your_stuID'
	print
	sys.exit(1)

def main(argv):
	length = len(subjects)
	for i in range(length):
		if subjects[i][0][2] == '2':
			continue
		else:
			apd=subjects[i][0][0:2] + '2' + subjects[i][0][3:]
			subjects.append((apd, subjects[i][1]))

	if not argv:
		usage()

	targetStu = argv[0]
	if len(targetStu) != 10:
		print 'Warning: bad ID'
		sys.exit(1)
	series = int(targetStu[6:])-21
	average(str(series))

if __name__ == '__main__':
	main(sys.argv[1:])
