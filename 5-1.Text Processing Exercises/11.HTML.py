title = input()
content = input()
comment = input()
print("<h1>")
print(f"\t{title}")
print("</h1>")
print("<article>")
print(f"\t{content}")
print("</article>")
while comment != "end of comments":
    print("<div>")
    print(f"\t{comment}")
    print("</div>")
    comment = input()