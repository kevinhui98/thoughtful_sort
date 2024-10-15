def sort(width, height,length,mass):
	# width, height, length will have to be in cm
	# mass is kg
	dimensions = (width * height)* length
	size = "clear"
	if width == 150 or height == 150 or length == 150 or dimensions >= 1000000:
		size = "bulky"
	if size == "clear" and mass < 20:
		return "STANDARD"
	elif size =="bulky" and mass >= 20:
		return "REJECTED"
	else:
		return "SPECIAL"
print(sort(100,100,230,19)) # SPECIAL
print(sort(100,100,23,19)) # STANDARD
print(sort(100,100,23,20)) # SPECIAL
print(sort(100,100,230,20)) # REJECTED
