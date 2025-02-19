from jinja2 import Template
name = "Anjali"
place = "Delhi"
profession = "Data Scientist"

temp = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
    <h1>{{name}}</h1>
    <h1>{{place}}</h1>
    <h1>{{profession}}</h1>
</body>
</html>
"""

made_temp = Template(temp)

output = made_temp.render(name=name, place=place, profession=profession)
print(output)