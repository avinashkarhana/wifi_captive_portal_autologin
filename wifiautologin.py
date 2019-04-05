import requests
import dukpy
from time import sleep
content=[]
with open ("/users/avinashkarhana/documents/pycode/wifiautologincreds.txt", "r") as myfile:
    for line in myfile:
        content.append(line)
url=content[0]
username=content[1]
pswd=content[2]
url=url[:-1]
username=username[:-1]
pswd=pswd[:-1]
lptitle=content[3]
print("Trying to login !\nPlease Wait...")
while requests.get(url).status_code!=200:
    print("Login Portal Still not Available")
    sleep(5)
r=requests.get(url);
if r.status_code == 200:
    x=r.text
    if(x[(int(x.find("<title>"))+7):int(x.find("</title>"))]==lptitle):
        tst=int(x.find("<title>"))+7
        tend=x.find("</title>")
        cid=x[(int(x.find("document.sendin.password.value = hexMD5('"))+41):(int(x.find(' + document.login.password.value + '))-1)]
        ch=x[(int(x.find(' + document.login.password.value + '))+36):(int(x.find("document.sendin.submit();")-7))]
        print("ChapID : "+str(cid))
        print("ChapChallenge: "+str(ch))
        pas=(cid+str(pswd)+ch)
        pas=pas.encode().decode('unicode-escape')
        cc='''function c(i,r){var n=(i&65535)+(r&65535);var u=(i>>16)+(r>>16)+(n>>16);return u<<16|n&65535}function o(i,r){return i<<r|i>>>32-r}function v(i,r,n,u,t,a){return c(o(c(c(r,i),c(u,a)),t),n)}function d(i,r,n,u,t,a,o){return v(r&n|~r&u,i,r,t,a,o)}function y(i,r,n,u,t,a,o){return v(r&u|n&~u,i,r,t,a,o)}function b(i,r,n,u,t,a,o){return v(r^n^u,i,r,t,a,o)}function k(i,r,n,u,t,a,o){return v(n^(r|~u),i,r,t,a,o)}function r(r){var n=1732584193;var u=-271733879;var t=-1732584194;var a=271733878;for(i=0;i<r.length;i+=16){var o=n;var v=u;var f=t;var e=a;n=d(n,u,t,a,r[i+0],7,-680876936);a=d(a,n,u,t,r[i+1],12,-389564586);t=d(t,a,n,u,r[i+2],17,606105819);u=d(u,t,a,n,r[i+3],22,-1044525330);n=d(n,u,t,a,r[i+4],7,-176418897);a=d(a,n,u,t,r[i+5],12,1200080426);t=d(t,a,n,u,r[i+6],17,-1473231341);u=d(u,t,a,n,r[i+7],22,-45705983);n=d(n,u,t,a,r[i+8],7,1770035416);a=d(a,n,u,t,r[i+9],12,-1958414417);t=d(t,a,n,u,r[i+10],17,-42063);u=d(u,t,a,n,r[i+11],22,-1990404162);n=d(n,u,t,a,r[i+12],7,1804603682);a=d(a,n,u,t,r[i+13],12,-40341101);t=d(t,a,n,u,r[i+14],17,-1502002290);u=d(u,t,a,n,r[i+15],22,1236535329);n=y(n,u,t,a,r[i+1],5,-165796510);a=y(a,n,u,t,r[i+6],9,-1069501632);t=y(t,a,n,u,r[i+11],14,643717713);u=y(u,t,a,n,r[i+0],20,-373897302);n=y(n,u,t,a,r[i+5],5,-701558691);a=y(a,n,u,t,r[i+10],9,38016083);t=y(t,a,n,u,r[i+15],14,-660478335);u=y(u,t,a,n,r[i+4],20,-405537848);n=y(n,u,t,a,r[i+9],5,568446438);a=y(a,n,u,t,r[i+14],9,-1019803690);t=y(t,a,n,u,r[i+3],14,-187363961);u=y(u,t,a,n,r[i+8],20,1163531501);n=y(n,u,t,a,r[i+13],5,-1444681467);a=y(a,n,u,t,r[i+2],9,-51403784);t=y(t,a,n,u,r[i+7],14,1735328473);u=y(u,t,a,n,r[i+12],20,-1926607734);n=b(n,u,t,a,r[i+5],4,-378558);a=b(a,n,u,t,r[i+8],11,-2022574463);t=b(t,a,n,u,r[i+11],16,1839030562);u=b(u,t,a,n,r[i+14],23,-35309556);n=b(n,u,t,a,r[i+1],4,-1530992060);a=b(a,n,u,t,r[i+4],11,1272893353);t=b(t,a,n,u,r[i+7],16,-155497632);u=b(u,t,a,n,r[i+10],23,-1094730640);n=b(n,u,t,a,r[i+13],4,681279174);a=b(a,n,u,t,r[i+0],11,-358537222);t=b(t,a,n,u,r[i+3],16,-722521979);u=b(u,t,a,n,r[i+6],23,76029189);n=b(n,u,t,a,r[i+9],4,-640364487);a=b(a,n,u,t,r[i+12],11,-421815835);t=b(t,a,n,u,r[i+15],16,530742520);u=b(u,t,a,n,r[i+2],23,-995338651);n=k(n,u,t,a,r[i+0],6,-198630844);a=k(a,n,u,t,r[i+7],10,1126891415);t=k(t,a,n,u,r[i+14],15,-1416354905);u=k(u,t,a,n,r[i+5],21,-57434055);n=k(n,u,t,a,r[i+12],6,1700485571);a=k(a,n,u,t,r[i+3],10,-1894986606);t=k(t,a,n,u,r[i+10],15,-1051523);u=k(u,t,a,n,r[i+1],21,-2054922799);n=k(n,u,t,a,r[i+8],6,1873313359);a=k(a,n,u,t,r[i+15],10,-30611744);t=k(t,a,n,u,r[i+6],15,-1560198380);u=k(u,t,a,n,r[i+13],21,1309151649);n=k(n,u,t,a,r[i+4],6,-145523070);a=k(a,n,u,t,r[i+11],10,-1120210379);t=k(t,a,n,u,r[i+2],15,718787259);u=k(u,t,a,n,r[i+9],21,-343485551);n=c(n,o);u=c(u,v);t=c(t,f);a=c(a,e)}return[n,u,t,a]}function n(i){var r="0123456789abcdef";var n="";for(var u=0;u<i.length*4;u++){n+=r.charAt(i[u>>2]>>u%4*8+4&15)+r.charAt(i[u>>2]>>u%4*8&15)}return n}function u(i){var r=(i.length+8>>6)+1;var n=new Array(r*16);for(var u=0;u<r*16;u++)n[u]=0;console.log(n);for(var u=0;u<i.length;u++)n[u>>2]|=(i.charCodeAt(u)&255)<<u%4*8;n[u>>2]|=128<<u%4*8;n[r*16-2]=i.length*8;return n}function t(i){return n(r(u(i)))}t(dukpy["value"]);'''
        pas=dukpy.evaljs(cc,value=pas)
        print("Password Hash : "+str(pas))
        zz={"username":username,"password":pas,"dst":"","popup":"true"}
        rr=requests.post(url,zz);
        xx=rr.text
        print("After Login Page Title : "+str(xx[(int(xx.find("<title>"))+7):int(xx.find("</title>"))]))
        exit(1)