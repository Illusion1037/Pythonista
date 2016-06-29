import ui
from time import sleep

# Init vars
money = 0
click_value = 1
simple = 0
simple_value = 1
silver = 0
silver_value = 2
gold = 0
gold_value = 5

# Save func
# Writes money and num of clickers to a file
def save(text,filename):
	f = open(filename,'w')
	f.write(text)
	f.close()

# Reset func
# Sets vars to 0 and updates the labels
def reset():
	
	# Make vars global
	global money
	global simple
	global silver
	global gold
	
	# Set vars to 0/update labels
	money = 0
	textlabel = v['score']
	textlabel.text = '$' + str(money)
	simple = 0
	textlabel = v['simplesub']
	textlabel.text = 'You have ' + str(simple) + ' | Price: $' + str(simple_value * 100) + ' | $' + str(simple_value) + '/sec'
	silver = 0
	textlabel = v['silversub']
	textlabel.text = 'You have ' + str(silver) + ' | Price: $' + str(silver_value * 100) + ' | $' + str(silver_value) + '/sec'
	gold = 0
	textlabel = v['goldsub']
	textlabel.text = 'You have ' + str(gold) + ' | Price: $' + str(gold_value * 100) +' | $' + str(gold_value) + '/sec'
		
# Upload func
# Takes money/num of clickers from file
def upload(name):
	
	# Make vars global
	global money
	global simple
	global silver
	global gold
	
	# Open file
	f = open(str(name) + '.txt','r')
	
	# Loop for each line
	line_number = 1
	for line in f:
		if line_number == 1:
			line1 = line
		elif line_number == 2:
			line2 = line
		elif line_number == 3:
			line3 = line
		elif line_number == 4:
			line4 = line
		line_number += 1
	
	# Close file
	f.close()
	
	# Update vars
	saved_money = line1
	saved_simple = line2
	saved_silver = line3
	saved_gold = line4
	money = int(saved_money)
	simple = int(saved_simple)
	silver = int(saved_silver)
	gold = int(saved_gold)

# Func for button click
def button_tapped(sender):
	
	# Make vars global
	global money
	global simple
	global silver
	global gold
	
	# Get button name
	n = sender.name
	
	if n == 'clicker':
		
		# Add to money for click
		money = int(money)
		money += int(click_value)
		textlabel = v['score'] 
		textlabel.text = '$' + str(money)
		
	elif n == 'simple' and money >= 100:
		
		# Buy a simple clicker with enough money
		simple += 1
		money -= 100
		textlabel = v['score']
		textlabel.text = '$' + str(money)
		textlabel = v['simplesub']
		textlabel.text = 'You have ' + str(simple) + ' | Price: $' + str(simple_value * 100) + ' | $' + str(simple_value) +'/sec'
		
	elif n == 'silver' and money >= 200:
		
		# Buy a silver clicker with enough money
		silver += 1
		money -= 200
		textlabel = v['score']
		textlabel.text = '$' + str(money)
		textlabel = v['silversub']
		textlabel.text = 'You have ' + str(silver) + ' | Price: $' + str(silver_value * 100) + ' | $' + str(silver_value) + '/sec'
		
	elif n == 'gold' and money >= 500:
		
		# Buy a gold clicker with enough money
		gold += 1
		money -= 500
		textlabel = v['score']
		textlabel.text = '$' + str(money)
		textlabel = v['goldsub']
		textlabel.text = 'You have ' + str(gold) + ' | Price: $' + str(gold_value * 100) + ' | $' + str(gold_value) + '/sec'
		
	elif n == 'save':
		
		# Execute save() func
		name = v['game'].selected_index + 1
		f = open(str(name) + '.txt','w')
		f.write(str(money) + '\n' + str(simple) + '\n' + str(silver) + '\n' + str(gold))
		f.close()
		
	elif n == 'reset':
		
		# Execute reset() func
		reset()
		
	elif n == 'upload':
		
		# Execute upload() func
		name = v['game'].selected_index + 1
		upload(name)
		
		# Update labels
		textlabel = v['score']
		textlabel.text = '$' + str(money)
		textlabel = v['simplesub']
		textlabel.text = 'You have ' + str(simple) + ' | Price: $' + str(simple_value * 100) + ' | $' + str(simple_value) + '/sec'
		textlabel = v['silversub']
		textlabel.text = 'You have ' + str(silver) + ' | Price: $' + str(silver_value * 100) + ' | $' + str(silver_value) + '/sec'
		textlabel = v['goldsub']
		textlabel.text = 'You have ' + str(gold) + ' | Price: $' + str(gold_value * 100) + ' | $' + str(gold_value) + '/sec'
		
# Load ui
v = ui.load_view('Clicker')
v.present(orientations=['portrait'])

# Game loop
while True:
	
	# Update money every second
	sleep(1)
	for clicker in range(int(simple)):
		money += 1
	for clicker in range(int(silver)):
		money += 2
	for clicker in range(int(gold)):
		money += 5
	textlabel = v['score']
	textlabel.text = '$' + str(money)

