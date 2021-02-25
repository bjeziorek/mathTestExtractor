import re

f=open("source.txt", encoding="utf8")
f.seek(0,2)
end=f.tell()
f.seek(0)
result=''
while(f.tell()<end):
 line=f.readline()
 start = line.find('<p>') + 2
 finish = line.find('</p>', start)
 line=line[start:finish]
# line=str.rstrip(line)
 line=re.sub('\</td>','',line)
 line=re.sub('\</span>','',line)
 line=re.sub('\</tr>','',line)
 line=re.sub('<td.*?>','',line)
 line=re.sub('<nobr.*?>','',line)
 line=re.sub('<span.*?>','',line)
 line=re.sub('<a.*?>','',line)
 line=re.sub('<i.*?>','',line)
 line=re.sub('<b.*?>','',line)
 line=re.sub('<sup.*?>','',line)
 line=re.sub('/ question.*','',line)
 line=re.sub('CATEGORY.*','',line)
 line=re.sub('\<tr>','',line)
 line=re.sub('\</nobr>','',line)
 line=re.sub('\</a>','',line)
 line=re.sub('\<br>','',line)
 line=re.sub('\</i>','',line)
 line=re.sub('\</b>','',line)
 line=re.sub('\<br>','',line)
 line=re.sub('\</sup>','',line)
 line=re.sub('\&nbsp;','',line)
 line=re.sub('\^0','°',line)
 line=re.sub("rightarrow",'→',line)
 line=re.sub(r'\\','',line)
 line=re.sub('alpha','α',line)
 line=re.sub('beta','β',line)
 line=re.sub('gamma','γ',line)
 
 result=result+line+'\n'

result=re.sub('\</p>','',result)
result=re.sub('\<p.*>','',result)
result=re.sub('\>','',result)

file=open("results.txt","w",encoding="utf8")
file.write(result)