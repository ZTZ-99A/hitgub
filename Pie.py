import pygal

piechart = pygal.Pie()
barchart = pygal.Bar()

file = open("pets.txt", "r")

for line in file.read().splitlines():
  label, value = line.split()
  piechart.add(label, int(value))
  barchart.add(label, int(value))

piechart.render()
barchart.render()
