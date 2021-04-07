# coding: utf-8
# use py3 ya bro

from requests import *
import json, os, string, random, sys, re, time, platform, base64

clear = lambda: os.system("clear")
list_mail = ["@besttempmail.com","@bestlistbase.com","@meantinc.com","@powerencry.com","@truthfinderlogin.com","@chasefreedomactivate.com","@wellsfargocomcardholders.com"]

if platform.python_version().split(".")[0] != "3":
	exit("\n\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;92m Ketik:\x1b[1;97m python "+sys.argv[0]+"\n")

class Menu:
	def menu_2():
		print("""
\x1b[1;91m _ __ _  _ _  \x1b[1;97m_  _ __ _ _
\x1b[1;91m  |  |_ |\/| |_] \x1b[1;97m|\/| |_| | |
\x1b[1;91m  |  |_ |  | |    \x1b[1;97m|  | |  | | |_
\x1b[1;92m=====================================
\x1b[1;97m [\x1b[1;92m01\x1b[1;97m] \x1b[1;97mGERAR EMAIL ALEATORIO
\x1b[1;97m [\x1b[1;92m02\x1b[1;97m] \x1b[1;97mCUSTOMIZAR
\x1b[1;97m [\x1b[1;92m03\x1b[1;97m] \x1b[1;97mINFO
\x1b[1;97m [\x1b[1;91m00\x1b[1;97m] \x1b[1;91mSAIR
\x1b[1;92m=====================================""")
		pilih = input("\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Qual Opçao?:\x1b[1;92m ")
		while pilih == "":
			pilih = input("\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Qual Opçao?:\x1b[1;92m ")
		if pilih=="01" or pilih=="1":
			execution("".join(random.choice(string.ascii_letters) for x in range(10)), random.choice(list_mail))
		elif pilih=="02" or pilih=="2":
			custom()
		elif pilih=="03" or pilih=="3":
			clear()
			about()
		elif pilih=="00" or pilih=="0":
			exit("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] PARANDO ..\n")
		else:
			exit("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] NENHUM MENU ADEQUADO ..\n")

def about():
	print("""
\x1b[1;91m _ __ _  _ _  \x1b[1;97m_  _ __ _ _
\x1b[1;91m  |  |_ |\/| |_] \x1b[1;97m|\/| |_| | |
\x1b[1;91m  |  |_ |  | |    \x1b[1;97m|  | |  | | |_
\x1b[1;92m=====================================
 \x1b[1;92mAuthor \x1b[1;91m: \x1b[1;97mPato Maker
 \x1b[1;92mGithub \x1b[1;91m: \x1b[1;97mhttps://github.com/patulinomods
 \x1b[1;92m\x1b[1;91mSuporte: \x1b[1;97m+5531996891466 \x1b[1;91m| \x1b[1;97mAseC\x1b[1;91m | \x1b[1;97mKhairul
\x1b[1;92m=====================================
	""")
	input("\x1b[1;91m<< \x1b[1;97mCLIQUE ENTER PARA VOLTAR AO MENU \x1b[1;91m>> ")
	os.system("python " + sys.argv[0])

def execution(nam, mail):
	name = nam.lower()
	regis = get("https://www.temporary-mail.net/change")
	cfduid = re.search("__cfduid=(.*?)\sfor", str(regis.cookies)).group(1)
	temp   = re.search("tempmail=(.*?)\sfor", str(regis.cookies)).group(1)
	ts = "&_ts={}".format(int(time.time()))
	gett = get("https://www.temporary-mail.net/api/v1/mailbox/keepalive?force_change=1&mailbox="+name+ts, data={"mailhost":mail},  headers={"x-requested-with":"XMLHttpRequest","user-agent":"Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36"}, cookies={"__cfduid":cfduid,"tempmail":temp}).text
	print("\x1b[1;92m=====================================")
	print(" \x1b[1;92m[\x1b[1;97mSEU EMAIL\x1b[1;92m]=> \x1b[1;97m"+name+mail)
	print("   \x1b[1;97mESPERANDO ALGUM EMAIL CHEGAR\x1b[1;91m ..")
	while True:
		try:
			cek = get("https://www.temporary-mail.net/api/v1/mailbox/"+name).text
			if "[]" in cek:
				continue
			elif "mailbox" in cek:
				js = json.loads(cek)
				print("\n\x1b[1;92m+--------|\x1b[1;97mNOVO EMAIL\x1b[1;92m|---------+")
				for jos in js:
					list = jos["id"]
				try:
					got = get("https://www.temporary-mail.net/api/v1/mailbox/"+name+"/"+list).text
					gud = json.loads(got)
					fr = gud["from"]
					froM = re.search('"(.*?)"', fr).group(1)
					from_email = re.search("<(.*?)>", fr).group(1)
					tggl = gud["date"]
					subj = gud["subject"]
					pesan = gud["body"]["text"].replace("\n","")
					print(" \x1b[1;92mENVIADO POR  \x1b[1;91m:\x1b[1;97m "+froM)
					print(" \x1b[1;92mEMAIL: \x1b[1;91m:\x1b[1;97m "+from_email)
					print(" \x1b[1;92mTITULO       \x1b[1;91m:\x1b[1;97m "+subj)
					print(" \x1b[1;92mDATA E HORA   \x1b[1;91m:\x1b[1;97m "+tggl)
					print(" \x1b[1;92mOUTROS     \x1b[1;91m:\x1b[1;97m "+pesan)
					for file in gud["attachments"]:
						if re.search("image/(\w+)", file["content-type"]).group(1) in file["content-type"]:
							print(" \x1b[1;92mARQUIVO  \x1b[1;91m:\x1b[1;93m - \x1b[1;97m"+file["filename"])
							cuk = get(file["view-link"]).content
							cik = base64.b64encode(cuk)
							cak = post("https://api.imgbb.com/1/upload?expiration=15552000&key=7a787a0e3e96926f2f75569bb77f6a3b", data={"image":cik}).text
							jsn = json.loads(cak)
							print("                  \x1b[1;93m-\x1b[1;97m "+jsn["data"]["medium"]["url"])
						else:
							continue
					print("\x1b[1;92m+-----------------------------------+")
					chek = delete("https://www.temporary-mail.net/api/v1/mailbox/"+name+"/"+list)
					continue
				except:
					continue
			else:
				continue
		except (KeyboardInterrupt,EOFError):
			exit("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] SAINDO..\n")

def custom():
	clear()
	print("""
\x1b[1;91m _ __ _  _ _  \x1b[1;97m_  _ __ _ _
\x1b[1;91m  |  |_ |\/| |_] \x1b[1;97m|\/| |_| | |
\x1b[1;91m  |  |_ |  | |    \x1b[1;97m|  | |  | | |_
\x1b[1;92m=====================================""")
	for list in range(len(list_mail)):
		print("\x1b[1;97m [\x1b[1;92m"+str(list+1)+"\x1b[1;97m]",list_mail[list])
	print("\x1b[1;92m=====================================")
	name = input("\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] DEFINA UM NOME: ")
	while name == "":
		print("  \x1b[1;97m(\x1b[1;91m--\x1b[1;97m) \x1b[1;97mDEFINA UM NOME PORRA(\x1b[1;91m--\x1b[1;97m)")
		name = input("\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] DEFINA UM NOME PARA O EMAIL: ")
	mall = input("\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] ESCOLHA UMA DAS OPÇOES ( 1 A 6 ): ")
	while mall == "":
		print("  \x1b[1;97m(\x1b[1;91m--\x1b[1;97m) \x1b[1;97mNAO PODE TAR VASIO PORRA(\x1b[1;91m--\x1b[1;97m)")
		mall = input("\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] ESCOLHA UMA DAS 6 OPÇOES : ")
	try:
		mal = list_mail[int(mall)-1]
	except Exception as er:
		exit("\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] ERRO:\x1b[1;91m "+str(er)+"\n")
	execution(name, mal)

if _name=="main_":
	clear()
	try:
		Menu.menu_2()
	except Exception as er:
		exit("\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] ERRO:\x1b[1;91m "+str(er)+"\n")
