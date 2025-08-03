# Develop Notice

1. 一个部分[^1]一个 branch
2. 新的部分产生的 branch 要从 dev 分支分出, 确定无误后使用 `git merge` 合并在 `dev` 内, 稳定之后再推送到 `master`
3. 如果是为修复 bug 而开启的新 branch, 请在 bug 所在 branch 处开新 branch
4. 接受远端更改时使用 `git rebase`

[^1]: `一个部分` 指的是 `pythontools` 下的一个文件夹
