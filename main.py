import wikipedia
theme=input("A word:")
wikipedia.set_lang('uz')
result=wikipedia.search(theme)
res=wikipedia.summary(theme, sentences=10)
print(result)
print(res)
