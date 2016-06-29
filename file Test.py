import file

content = file.read('file Test.txt')

print(content)

file.write('file Test.txt',content + '\n\nFooter')

content = file.read('file Test.txt')

print(content)

file.append('file Test.txt','\nLegal|Copyright')

content = file.read('file Test.txt')

print(content)
