#!/usr/bin/env python
# coding: utf-8

# # Create a script that can parse the gitdm developer affiliation files and load the data in a SortingHat database using GraphQL.

# I obtained the gitdm file from [github.com/cncf/gitdm/developers_affiliations1.txt](https://github.com/cncf/gitdm/blob/master/developers_affiliations1.txt)

# In[1]:


f = open("developer.txt","r")
content = f.read()


# In[2]:


content[:100]


# In[3]:


content.replace("\n\t","\t").split("\n")


# In[4]:


c = content.replace("\n\t", "\t")


# In[5]:


c = c.split("\n")


# In[6]:


c = c[7:]


# In[7]:


k = [i.split("\t") for i in c]


# In[8]:


# remove the comments, lines starting with # hashtag symbol 
#c = c[1:]


# In[9]:


for i in k:
    print("name  ",i[0].split(":")[0])
    print("emails  ",i[0].split(":")[1])
    print("organisations ",i[1:])


# In[11]:


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
    


#  currently gives 403 request code, because django security validation. 
#  if we include this in urls in django we can successfully exeute url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
#  
#  config.urls should look like this
#  
# ```python
# from django.contrib import admin
# from django.urls import path
# 
# from sortinghat.core.views import SortingHatGraphQLView
# from django.views.decorators.csrf import csrf_exempt
# 
# from .schema import schema
# 
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('graphql/', csrf_exempt(SortingHatGraphQLView.as_view(graphiql=True,
#                                                    schema=schema))),
# ]
# 
# ```
# 

# In[36]:


# data = {'name': 'YunSangJun','email': ' YunSangJun!users.noreply.github.com',  'source': 'git', 'username': 'YunSangJun'}
url = "http://localhost:8000/graphql/"
res = requests.post(url, json={'query': query})


# In[37]:


print(res.text)


# ![Screenshot%20from%202021-03-31%2016-20-56.png](attachment:Screenshot%20from%202021-03-31%2016-20-56.png)
