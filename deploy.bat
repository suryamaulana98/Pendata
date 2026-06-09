@echo off
git add .
git commit -m "Add modeling, evaluation, and deployment notebooks"
git push
jupyter-book build materi
ghp-import -n -p -f materi/_build/html
