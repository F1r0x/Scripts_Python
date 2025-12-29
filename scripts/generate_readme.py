import os

START = "<!-- PROJECTS_START -->"
END = "<!-- PROJECTS_END -->"

# Carpetas que no queremos listar
EXCLUDE = {
    ".git", ".github", "scripts"
}

# Detectar carpetas de nivel superior
projects = sorted([
    d for d in os.listdir(".")
    if os.path.isdir(d) and d not in EXCLUDE
])

# Leer README.md actual
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Generar lista en Markdown
projects_md = "\n".join(
    f"- [{p}](./{p})" for p in projects
)

new_section = f"{START}\n{projects_md}\n{END}"

before = content.split(START)[0]
after = content.split(END)[1]

new_content = before + new_section + after

# Escribir README.md actualizado
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print("✔ README.md actualizado correctamente")
