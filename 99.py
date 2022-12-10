entry = input("Type something : ")
# print(f"<p> \033[1m{entry}\033[0m </p>")
output = f"<h1>{entry}</h1>"

open("Index.html", "w").write(output)
