import re,sys,hashlib

def blocks(s, pat):
    return [hashlib.md5(m.encode()).hexdigest() for m in re.findall(pat, s, re.S)]

def cp(s):
    return re.findall(r'<p[^>]*>.*?</p>|<li[^>]*>.*?</li>', s, re.S)

for f in sys.argv[1:]:
    a=open('.pre-humanizer/lessons/'+f,encoding='utf-8').read()
    b=open('lessons/'+f,encoding='utf-8').read()
    out=[]
    for name,pat in [
        ('excerpt', r'<div class="excerpt">.*?</div>'),
        ('pre', r'<pre>.*?</pre>'),
        ('table', r'<table>.*?</table>'),
        ('h', r'<h[1-4][^>]*>.*?</h[1-4]>'),
        ('button', r'<button[^>]*>.*?</button>'),
        ('href', r'href="[^"]*"'),
        ('class', r'class="[^"]*"'),
        ('id', r'id="[^"]*"'),
        ('data', r'data-[a-z]+="[^"]*"'),
        ('anti', r'<div class="anti">.*?</div>\s*</div>'),
        ('gloss', r'<div class="gloss">.*?</div>'),
        ('blockquote', r'<blockquote>.*?</blockquote>'),
    ]:
        if blocks(a,pat)!=blocks(b,pat):
            out.append(name)
    print(f, 'PROTECT-DIFF:', out if out else 'none')
