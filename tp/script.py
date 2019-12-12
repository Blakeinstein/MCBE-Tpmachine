import subprocess

def script():
    try:
        subprocess.call(f'screen -S mcpe -X stuff \'list\\n\'',shell=True)
    finally:
        f=open('~/mcpe/screenlog.0','r+')
        lis=f.readlines()
        out=[]
        buff=''
        if len(lis) < 2:
            return out
        else:
            n=len(lis)-1
            for i in reversed(lis):
                if i == 'list':
                    break
                n-=1
            try:
                for i in lis[n+3]:
                    if i == ',':
                        out.append(buff.strip())
                        buff=''
                    elif i=='[':
                        break
                    else:
                        buff+=i
                else:   
                    out.append(buff.strip())
                return out
            except IndexError:
                return out
        _=f.truncate(0)
        f.close()  
              
players = script()
choices = dict(zip(players,players))
# choices2={'':''}
# for i in choices:
#     choices2[i]=i

