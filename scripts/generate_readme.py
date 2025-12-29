import os
import re

COURSES_START = "<!-- COURSES_START -->"
COURSES_END = "<!-- COURSES_END -->"
GAMES_START = "<!-- GAMES_START -->"
GAMES_END = "<!-- GAMES_END -->"

EXCLUDE = {".git", ".github", "scripts"}

def read_info(folder):
    info_path = os.path.join(folder, "info.txt")
    if os.path.exists(info_path):
        return open(info_path, encoding="utf-8").read().strip()
    return "Sin descripción."

def count_scripts(folder):
    return len([
        f for f in os.listdir(folder)
        if f.endswith(".py")
    ])

def get_courses():
    courses = []
    for d in os.listdir("."):
        if d.startswith("CursoPython") and os.path.isdir(d):
            # Intentamos extraer número, si no hay ponemos 0
            nums = re.findall(r"\d+", d)
            number = int(nums[0]) if nums else 0
            courses.append((number, d))
    # Ordenamos por número
    courses.sort(key=lambda x: x[0])
    # Devolvemos solo los nombres
    return [d for _, d in courses]

def get_games():
    if not os.path.isdir("Juegos"):
        return []
    return sorted([
        d for d in os.listdir("Juegos")
        if os.path.isdir(os.path.join("Juegos", d))
    ])

def generate_section(items, base_path=""):
    lines = []
    for item in items:
        path = os.path.join(base_path, item).replace("\\", "/")  # Para Windows
        scripts = count_scripts(path)
        info = read_info(path)
        # Aquí añadimos el enlace clicable
        lines.append(
            f"- 📁 **[{item}]({path})** ({scripts} scripts)  \n"
            f"  {info}\n"
        )
    return "\n".join(lines)

with open("README.md", encoding="utf-8") as f:
    content = f.read()

courses_md = generate_section(get_courses())
games_md = generate_section(get_games(), "Juegos")

content = re.sub(
    f"{COURSES_START}.*?{COURSES_END}",
    f"{COURSES_START}\n{courses_md}\n{COURSES_END}",
    content,
    flags=re.S
)

content = re.sub(
    f"{GAMES_START}.*?{GAMES_END}",
    f"{GAMES_START}\n{games_md}\n{GAMES_END}",
    content,
    flags=re.S
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("✔ README actualizado con cursos y juegos y enlaces")
