from jinja2 import Template
name = "Anjali"
place = "Delhi"
profession = "Date Scientist"

#Step1
temp = "My name is {{name}}, I am from {{place}} and I am a {{profession}}."
#temp = "My name is {{name}}."

#Step2
made_temp = Template(temp)

#Step3
output = made_temp.render(name=name, place=place, profession=profession)
print(output)
