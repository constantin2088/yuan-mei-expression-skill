"""Local deterministic aid; never a factual or model behavior certificate."""
def analyze(p):
 text=p['text'];changes=sorted(p['changes'],key=lambda c:c['start']);last=0;out=[]
 for c in changes:
  start,end=c['start'],c['end']
  if type(start)!=int or type(end)!=int or start<last or end<=start or end>len(text):raise ValueError('overlap or invalid Unicode character bounds')
  if text[start:end]!=c['old']:raise ValueError('original span mismatch')
  if not isinstance(c.get('reason'),str) or not c['reason'].strip():raise ValueError('revision reason required')
  if not isinstance(c['new'],str):raise ValueError('replacement must be text')
  out.extend([text[last:start],c['new']]);last=end
 out.append(text[last:]);return {'text':''.join(out),'revisions':len(changes),'note':'Character positions use the original text; author must confirm meaning and facts.'}

if __name__=='__main__':
 import json,sys
 print(json.dumps(analyze(json.loads(open(sys.argv[1],encoding='utf-8').read())),ensure_ascii=False,indent=2))
