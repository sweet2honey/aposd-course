import re, sys
from html.parser import HTMLParser

VOID = {'meta','link','br','hr','img','input','source','area','base','col','embed','param','track','wbr'}

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack=[]; self.errs=[]
    def handle_starttag(self, tag, attrs):
        if tag in VOID: return
        self.stack.append((tag,self.getpos()))
    def handle_endtag(self, tag):
        if tag in VOID: return
        if not self.stack:
            self.errs.append(('extra close',tag,self.getpos())); return
        if self.stack[-1][0]==tag: self.stack.pop()
        else:
            self.errs.append(('mismatch',tag,'expected '+self.stack[-1][0],self.getpos()))
            for i in range(len(self.stack)-1,-1,-1):
                if self.stack[i][0]==tag:
                    del self.stack[i:]; break

for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read()
    body=re.sub(r'<pre>.*?</pre>','',s,flags=re.S)
    body=re.sub(r'<code>.*?</code>','',body,flags=re.S)
    han=len(re.findall(r'[\u4e00-\u9fff]',body))
    print(f,'han=',han,'excerpt=',s.count('class="excerpt"'),'anti=',len(re.findall(r'class="anti\b',s)),'dataok=',s.count('data-ok'),'dash=',s.count('——'))
    p=P(); p.feed(s); errs=list(p.errs)
    if p.stack: errs.append(('unclosed',[t for t,_ in p.stack]))
    print('   tagerr=',len(errs))
    for e in errs[:8]: print('   ',e)
