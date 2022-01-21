import pyperclip

tags = input(str('Enter tags you want: '))
tags = tags.split(" ")
list = []
for x in tags:
   x = '#' + x
   list.append(x)
   final = " ".join(list)

print(final)
pyperclip.copy(final)
print('Tags copied to clipboard.')
input()
    
