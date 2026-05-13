import json

with open("materi/analisa-data-menggunakan-random-forest.ipynb", "r") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    if cell["cell_type"] == "markdown":
        src = "".join(cell["source"])
        if "$$ \hat{y} =" in src or "$$ \\hat{y}" in src:
            new_src = src.replace("$$ \\hat{y} = \\text{mode} \\{ h_1(x), h_2(x), \\dots, h_K(x) \\} $$", 
"""
$$
\\hat{y} = \\text{mode} \\{ h_1(x), h_2(x), \\dots, h_K(x) \\}
$$
""")
            # Fix error rate formula if needed
            new_src = new_src.replace("$$ \\text{Accuracy} = \\frac{2}{3} = 0.666 \\; (66.67\\%) $$",
"""
$$ 
\\text{Accuracy} = \\frac{2}{3} = 0.666 \\; (66.67\\%) 
$$
""")
            new_src = new_src.replace("$$ \\text{Error Rate} = \\frac{1}{3} = 0.333 \\; (33.33\\%) $$",
"""
$$ 
\\text{Error Rate} = \\frac{1}{3} = 0.333 \\; (33.33\\%) 
$$
""")
            # Split back into lines
            lines = new_src.splitlines(True)
            cell["source"] = lines

with open("materi/analisa-data-menggunakan-random-forest.ipynb", "w") as f:
    json.dump(nb, f, indent=2)
