import os

START = "<!-- PROJECTS_START -->"
END = "<!-- PROJECTS_END -->"

EXCLUDE = {
    ".git",
    ".github",
    "scripts"
}

# Obtener carpetas de proyectos
projects = sorted([
    d for d in os.listdir(".")
    if os.path.isdir(d) and d not in EXCLUDE
])

# Leer README actual
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Crear lista markdown
projects_md = "\n".join(
    f"- [{p}](./{p})" for p in projects
)

new_section = f"{START}\n{projects_md}\n{END}"

# Reemplazar sección
before = content.split(START)[0]
after = content.split(END)[1]

new_content = before + new_section + after

# Guardar README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print("README actualizado correctamente")
