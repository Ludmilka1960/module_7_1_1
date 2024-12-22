from fileinput import close

__file_name = "E:\products.txt"
f = open(__file_name,'r',encoding='utf-8')
s = f.read()
print(s)
f.close()

f = open(__file_name,'a',encoding='utf-8')


close()


