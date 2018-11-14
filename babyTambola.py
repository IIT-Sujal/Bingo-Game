#remember to keep unique elements in the set of one ticket also ensure no two tickets become same
#515x680 picture dimension
from PIL import Image, ImageDraw, ImageFont
from random import randint,shuffle
 
count=0
def match(l1,l2):
	for i in range(15):
		if l1[i]==l2[i]:
			return False
	return True
def set_generator(num):
	total_ticket=list()
	while len(total_ticket)<num:
		ticket_numbers=set()
		while len(ticket_numbers)<15: #keep unique elements in the set
			ticket_numbers.add(randint(1, 90))
		ticket_numbers=list(ticket_numbers)
		ticket_numbers.sort()
		not_match=True
		for i in total_ticket:
			if match(i,ticket_numbers)==True:
				not_match=False
		if not_match==True:
			total_ticket.append(ticket_numbers)
		else:
			global count
			count+=1
	return total_ticket

total_ticket=list(set_generator(200))
for x in range(1,200):
	img = Image.open("baby.png")
	d = ImageDraw.Draw(img)
	fnt = ImageFont.truetype('arial.ttf', 15)
	ticket_numbers=total_ticket[x]
	shuffle(ticket_numbers)
	#face
	d.text((388,355), str(ticket_numbers[1]), font=fnt, fill=(0,0,0))
	d.text((434,428), str(ticket_numbers[2]), font=fnt, fill=(0,0,0))
	d.text((505	,358), str(ticket_numbers[3]), font=fnt, fill=(0,0,0))

	#body
	d.text((298,548), str(ticket_numbers[4]), font=fnt, fill=(0,0,0))
	d.text((275,620), str(ticket_numbers[0]), font=fnt, fill=(0,0,0))
	d.text((305,688), str(ticket_numbers[5]), font=fnt, fill=(0,0,0))

	#hand
	d.text((400,670), str(ticket_numbers[6]), font=fnt, fill=(0,0,0))
	d.text((415,726), str(ticket_numbers[7]), font=fnt, fill=(0,0,0))
	d.text((436,780), str(ticket_numbers[8]), font=fnt, fill=(0,0,0))

	#diaper
	d.text((138,548), str(ticket_numbers[9]), font=fnt, fill=(0,0,0))
	d.text((163,605), str(ticket_numbers[10]), font=fnt, fill=(0,0,0))
	d.text((105,632), str(ticket_numbers[11]), font=fnt, fill=(0,0,0))

	#leg
	d.text((195,763), str(ticket_numbers[12]), font=fnt, fill=(0,0,0))
	d.text((192,690), str(ticket_numbers[13]), font=fnt, fill=(0,0,0))
	d.text((76,715), str(ticket_numbers[14]), font=fnt, fill=(0,0,0))
	img.save('tickets/'+str(x)+'.png')
