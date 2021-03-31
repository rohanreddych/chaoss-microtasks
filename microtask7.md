# Create a script that can parse the gitdm developer affiliation files and load the data in a SortingHat database using GraphQL.

I obtained the gitdm file from [github.com/cncf/gitdm/developers_affiliations1.txt](https://github.com/cncf/gitdm/blob/master/developers_affiliations1.txt)


```python
f = open("developer.txt","r")
content = f.read()
```


```python
content[:100]
```




    "# This is the main developers affiliations file.\n# If you see your name with asterisk '*' sign - it "




```python
content.replace("\n\t","\t").split("\n")
```


```python
c = content.replace("\n\t", "\t")
```


```python
c = c.split("\n")
```


```python
c = c[7:]
```


```python
k = [i.split("\t") for i in c]
```


```python
# remove the comments, lines starting with # hashtag symbol 
#c = c[1:]
```


```python
for i in k:
    print("name  ",i[0].split(":")[0])
    print("emails  ",i[0].split(":")[1])
    print("organisations ",i[1:])
```


```python
import requests
# query = "mutation{ addIdentity(name:"+i[0].split(":")[0]+ ", email:"+ i[0].split(":")[1].split(",")[0]+ ",source:" + "git"+",username:"+ i[0].split(":")[0]+"){uuid}}"

for i in k:
    url = "http://localhost:8000/graphql/"
    try:
        query = "mutation{ addIdentity(name:"+'"'+str(i[0].split(":")[0])+'"'+", email:"+'"'+ i[0].split(":")[1].split(",")[0]+'"'+ ",source:" +'"'+ "git"+'"'+",username:"+'"'+str(i[0].split(":")[0])+'"'+"){uuid}}"
        print(query)
    except IndexError:
        query = "mutation{ addIdentity(name:"+i[0].split(":")[0]+ ", email:"+"na"+ ",source:" + "git"+",username:"+ i[0].split(":")[0]+"){uuid}}"
    res = requests.post(url, json={'query': query})
    
    if (res.status_code != 200):
        print("error ")
        print(res.text)
        break
    
```


```python
# currently gives 403 request code, because django security validation. 
# if we include this in urls in django we can successfully exeute url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
```


```python
# data = {'name': 'YunSangJun','email': ' YunSangJun!users.noreply.github.com',  'source': 'git', 'username': 'YunSangJun'}
url = "http://localhost:8000/graphql/"
res = requests.post(url, json={'query': query})
```


```python
print(res.text)
```

    {"data":{"addIdentity":{"uuid":"032e3f8110875bdf295780edf39bad74df1b0f79"}}}


![Screenshot%20from%202021-03-31%2016-20-56.png](attachment:Screenshot%20from%202021-03-31%2016-20-56.png)
