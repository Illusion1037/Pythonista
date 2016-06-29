import editor
import console

text = editor.get_text()

text = text.splitlines()

console.alert('Line Count', 'There are ' + str(len(text)) + ' lines in this program.')

