def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
	if fastest:
		redShirtSpeeds.sort()
		blueShirtSpeeds.sort(reverse=True)
	else:
		redShirtSpeeds.sort()
		blueShirtSpeeds.sort()
	speeds = []
	for i, item in enumerate(redShirtSpeeds):
		speed = max(item, blueShirtSpeeds[i])
		speeds.append(speed)
	total = sum(speeds)
    return total

