file = open("toc.html", "a")

for i in range(1, 242):
    file.write(f'<a href="Chapter{i}.html">Chapter {i}</a><br>\n')
