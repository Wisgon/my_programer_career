1. npm install时出现：`husky - .git can't be found (see https://typicode.github.io/husky/#/?id=custom-directory)`，这是husky的问题，可以在package.json里，将`"prepare": "husky install",`改成`"prepare": "cd .. && husky install xxx/.husky",`,其中，xxx是前段项目所在文件夹；<br><br>
2. 
