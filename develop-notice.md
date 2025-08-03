# Develop Notice

## 1 分支管理

### 1.1 两个基本分支

- `master`: 生产环境稳定分支，仅允许通过 Release PR 合并
- `dev`: 集成测试分支，所有功能/修复最终合并至此

### 1.2 branch 命名

1. 如果是某个新的部分[^1]，branch名称就是对应文件夹的名称，如 `permission`
2. 如果是 bug 修复，branch 名称为 `fix/*` 或 `hotfix/*`(紧急情况使用)
3. 如果是某个新部分(P)的某个功能(A)，branch 名称就为 `P/A`，如 `permission/manager`

## 2 提交规范

#### 2.1 信息格式

```text
<type>: <description>
```

- **常用type:**
  - feat: 新功能
  - fix: bug修复
  - docs: 文档更新
  - refactor: 重构代码
  - test: 测试相关

## 3 合并流程

1. 开新的部分时新开一个 [branch](#12-branch-命名)，并创建对应的文件夹
2. 新的部分产生的 branch 要从 dev 分支分出，初步审查通过后使用 `git merge` 合并在 `dev` 内，在 `dev` 内稳定之后才会推送到 `master`
   - 部分内的 feature 需要先 merge 到对应的部分
3. 如果是为修复 bug 而开启的新 branch，请在 bug 所在 branch 处开新 branch
   - 如果是紧急修复
     1. 创建新分支(见[命名规范](#12-branch-命名))，如果已经影响`master`就从 `master` 创建分支，还只是 `dev` 就在 `dev` 内创建
     2. 修复
     3. 提交 Pull Request 到 `master`/`dev`
4. 本地接受远端更改时使用 `git rebase`

## 4. 其他
1. 不准直接向 `master` 推送代码
2. 一般不允许直接向 `dev` 推送代码
3. 合并 Pull Request 时使用 **Squash Merge**










[^1]: `部分` 指的是 `pythontools` 下的一个文件夹(或者说模块、包，但必须是在 `src/pythontools` 目录下)
