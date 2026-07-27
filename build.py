# Regenerate the derived entry pages from index.html (single source of truth).
c=open('index.html').read()
key='&quot;default&quot;:&quot;splash&quot;'
assert c.count(key)==1, "startScreen marker not found/unique"
open('home.html','w').write(c.replace(key,'&quot;default&quot;:&quot;home&quot;',1))
open('onboarding.html','w').write(c.replace(key,'&quot;default&quot;:&quot;onboarding&quot;',1))
print("built home.html + onboarding.html from index.html")
