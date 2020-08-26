$ErrorActionPreference = "Stop"
wsl bundle exec jekyll clean
wsl bundle exec jekyll build
Push-Location _site
git init
git add .
git commit -m "upload"
git remote add origin https://github.com/jzc/jzc.github.io.git
git push origin master:gh-pages --force
rm -r -force .git
Pop-Location