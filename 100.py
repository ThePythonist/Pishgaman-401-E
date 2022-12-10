people = [
    {"Name": "Alireza", "Age": 25, "Job": "Front-End"},
    {"Name": "Mohammadreza", "Age": 14, "Job": "Back-End"},
    {"Name": "Mohammad", "Age": 21, "Job": "Security-Engineer"},
]

html = """
<!DOCTYPE html>
<html>
<head>
<style>

html {
  font-family: sans-serif;
}
#customers {
  font-family: sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #b94137;
  color: white;
}
</style>
</head>
<body>

<h1>A Fancy Table</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Age</th>
    <th>Job</th>
  </tr>

"""

for person in people:
    html += f"""
  <tr>
    <td>{person["Name"]}</td>
    <td>{person["Age"]}</td>
    <td>{person["Job"]}</td>
  </tr>
  """

html += """
</table>
</body>
</html>
"""

open("Table.html", "w").write(html)
print("Done")
