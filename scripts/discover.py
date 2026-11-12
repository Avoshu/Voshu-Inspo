#!/usr/bin/env python3
import datetime as dt,json,os,pathlib,urllib.request,urllib.parse,math
root=pathlib.Path(__file__).resolve().parents[1]
today=dt.datetime.now(dt.timezone.utc).date().isoformat()
seeds=['vercel-labs/agent-desktop','vercel-labs/agent-browser','vercel-labs/open-agents','vercel-labs/durable-harness','vercel-labs/portless','vercel-labs/dev3000','vercel-labs/mcp-handler','vercel-labs/agent-eval','vercel-labs/json-render','vercel-labs/design-systems-to-agent-skills']
queries=['topic:ai-agents','topic:mcp','topic:computer-use','topic:browser-automation','topic:voice-ai','topic:llm-inference','topic:design-system','topic:self-hosted','topic:developer-tools']
def api(path,params=None):
 url='https://api.github.com/'+path
 if params:url+='?'+urllib.parse.urlencode(params)
 headers={'Accept':'application/vnd.github+json','User-Agent':'voshu-inspo','X-GitHub-Api-Version':'2022-11-28'}
 if os.getenv('GITHUB_TOKEN'):headers['Authorization']='Bearer '+os.environ['GITHUB_TOKEN']
 with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=30) as r:return json.load(r)
def cat(r):
 s=(' '.join([r['name'],r.get('description') or '',' '.join(r.get('topics') or [])])).lower()
 for k,terms in [('Desktop & Browser',['desktop','browser','computer-use']),('Voice & Audio',['voice','speech','audio']),('MCP & Integrations',['mcp','connector']),('Models & Inference',['inference','model-serving','llm']),('Design & UX',['design','ui','frontend']),('Security',['security','sandbox']),('Infrastructure',['self-host','infra','deploy']),('Developer Tools',['developer','terminal','cli','debug']),('Agent Frameworks',['agent','orchestration'])]:
  if any(t in s for t in terms):return k
 return 'Other'
def table(rows):
 out=['| Repository | Purpose | Category | Stars | Last push | Voshu use |','|---|---|---|---:|---|---|']
 for r in rows:
  clean=lambda x:str(x or '—').replace('|','/').replace('\n',' ')[:120]
  out.append(f"| [{r['repo']}]({r['url']}) | {clean(r['purpose'])} | {r['category']} | {r['stars']:,} | {str(r['last_push'] or '')[:10]} | {clean(r['voshu_use'])} |")
 return '\n'.join(out)+'\n'
def main():
 file=root/'data/repositories.json'; old={r['repo']:r for r in json.loads(file.read_text())} if file.exists() else {}; found={};errors=[]
 for name in seeds:
  try:
   r=api('repos/'+name);found[r['full_name']]=r
  except Exception as e:errors.append(name+': '+str(e))
 for q in queries:
  try:
   for r in api('search/repositories',{'q':q+' archived:false stars:>100','sort':'updated','per_page':30})['items']:
    if not r.get('fork') and not r.get('archived'):found[r['full_name']]=r
  except Exception as e:errors.append(q+': '+str(e))
 if not found:raise RuntimeError('All GitHub discovery requests failed; preserving catalog')
 merged=old.copy()
 for name,r in found.items():
  prev=old.get(name,{});age=max(0,(dt.datetime.now(dt.timezone.utc)-dt.datetime.fromisoformat((r.get('pushed_at') or '2000-01-01T00:00:00Z').replace('Z','+00:00'))).days)
  merged[name]={'repo':name,'url':r['html_url'],'purpose':r.get('description') or '','category':prev.get('category') or cat(r),'stars':r.get('stargazers_count',0),'language':r.get('language'),'license':(r.get('license') or {}).get('spdx_id'),'last_push':r.get('pushed_at'),'last_checked':today,'score':round(math.log1p(r.get('stargazers_count',0))*2+max(0,20-age/7),1),'voshu_use':prev.get('voshu_use','Needs review'),'review_status':prev.get('review_status','Unreviewed'),'notes':prev.get('notes','')}
 rows=sorted(merged.values(),key=lambda r:r.get('score',0),reverse=True)
 file.parent.mkdir(parents=True,exist_ok=True);file.write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
 (root/'CATALOG.md').write_text('# Voshu Inspo — Repository Catalog\\n\\nAuto-refreshed metadata; scores are discovery heuristics, not endorsements.\\n\\n'+table(rows))
 new=[merged[n] for n in found if n not in old];reports=root/'reports/daily';reports.mkdir(parents=True,exist_ok=True)
 (reports/(today+'.md')).write_text(f'# Discovery — {today}\\n\\nScanned {len(found)} repositories; {len(new)} new; {len(errors)} API errors.\\n\\n'+(table(new) if new else 'No new discoveries.\\n')+'\\n## Errors\\n\\n'+('\n'.join('- '+e for e in errors) if errors else 'None')+'\n')
 print(f'{len(rows)} indexed, {len(new)} new, {len(errors)} errors')
if __name__=='__main__':main()
