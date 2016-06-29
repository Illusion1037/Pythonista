import scene

def rect(rectangle, borderw=0, borderclr=(0, 0, 0)):
	scene.stroke(*borderclr)
	scene.stroke_weight(borderw)
	scene.rect(*rectangle)
	
def ellipse(rectangle, borderw=0, borderclr=(0, 0, 0)):
	scene.stroke(*borderclr)
	scene.stroke_weight(borderw)
	scene.ellipse(*rectangle)

def line(pt1, pt2, w=1):
	scene.stroke_weight(w)
	scene.line(*pt1 + pt2)

def poly(points):
	for index in range(len(points) - 1):
		scene.line(*points[index] + points[index + 1])
	scene.line(*points[0] + points[len(points) - 1])
		

