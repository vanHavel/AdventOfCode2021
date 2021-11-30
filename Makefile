DAY=1
day:
	cat template.py | sed "s/%DAY%/${DAY}/g" > days/day${DAY}.py
