import re
import pickle
f=open('PoemClass.py')
code=f.read()
#print code
found=re.findall("'''(.+?)'''",code,re.DOTALL)
poems=[found[i] for i in range(1, len(found), 2)] 
f.close()
titles=["I don't know what to say" ,"The light in my world","I Wanna" ,"I Want You Here", "Not As Strong As An Oak"]
anthology= dict(zip(titles,poems))
pickle.dump( anthology, open( "poems.p", "wb" ) )
