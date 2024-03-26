# all-to-mdbook 自动化部署 mdBook 仓库

本仓库旨在提供一种自动化的方式来部署包含 Markdown 文件结构的仓库到 mdBook。利用 GitHub Actions，它能够自动识别仓库中的 Markdown 文件，并生成相应的 mdBook。此外，它支持自定义配置，如目标仓库链接、忽略特定文件夹、启用自然排序等，使得生成的书籍结构更加合理和美观。

## 特性

- 自动化生成 mdBook 目录。
- 支持自定义目标仓库链接。
- 支持忽略特定文件夹，避免在目录中显示空文件夹。
- 支持自然排序，以便在目录中正确排序数字（如 `1, 2, ..., 10, 11`）。
- 可以通过工作流配置文件设置自动触发时间间隔。
- 识别 `README.md` 文件并将其置顶。
- 使用 mdBook-tools 仓库设计的排版主题。

## 配置

本项目的配置通过 `config.ini` 文件进行，该文件包含两个主要部分：`src` 和 `repository`。

### 示例配置

```ini
[src]
directory = ./src
output_file = ./src/SUMMARY.md
ignore_dirs = .git,figs,examples,figures,.github
use_natural_sort = True

[repository]
url = https://github.com/yourusername/yourrepository
```

- `directory`: 指定 md 文件的源目录。
- `output_file`: 指定生成的目录文件。
- `ignore_dirs`: 指定需要忽略的目录列表。
- `use_natural_sort`: 是否启用自然排序。
- `url`: 目标仓库的链接。

## 工作流自动化

本项目通过 `.github/workflows/mdbook.yml` 文件配置 GitHub Actions 工作流，以自动化 mdBook 的生成和部署。

### 工作流配置

```yaml
schedule:
  - cron: '*/6 * * * *'
```

#### 时间间隔含义

`cron` 表达式 `'*/6 * * * *'` 表示每小时的每 6 分钟触发一次工作流。

## 使用方法

#### 1. Fork 仓库

- 点击右上角的 "Fork" 按钮，将仓库 Fork 到你的 GitHub 账户下。

#### 2. 启用 GitHub Pages

- 进入你 Fork 后的仓库的 "Settings"。
- 找到 "Pages" 部分。
- 在 "Build and deployment" 选项中，选择"GitHub Actions"

#### 3. 修改配置文件

##### a. `config.ini` - 定制目录结构 排除规则 目标仓库链接

在你的项目中找到 `config.ini` 文件，并按照以下模板进行修改以适应你的项目需求：

```ini
[src]
ignore_dirs = .git,figs,examples,figures,.github
use_natural_sort = True

[repository]
url = https://github.com/yourusername/yourrepository
```

- `ignore_dirs`: 根据需要调整 `ignore_dirs` 以忽略不需要包含在 mdBook 目录中的文件夹，使用逗号分隔即可。
- `use_natural_sort`: 是否启用自然排序。
- **`url`: 用于生成 mdbook 的目标仓库的链接。**

##### b. `book.toml` - 定制书籍信息

在 `book.toml` 中找到 `[book]` 部分，修改 `title` 以设置你的书籍标题：

```toml
[book]
title = "Your Book Title"
```

##### c. 自定义导航

- 找到 `theme/index.hbs` 文件。
- 在大约第 180 行，根据需要修改 HTML 代码来自定义书籍的导航栏。或删除导航（'\<a>'包裹的内容）。

#### 4. 配置 `mdbook.yml` 触发事件（可选）

在 `.github/workflows/mdbook.yml` 文件中，你可以设置触发事件：

```yaml
on:
  push:
    branches: ["main"]
  schedule:
    - cron: '0 1 * * *' # 每天凌晨 1 点触发
  workflow_dispatch:
```

- 这配置了三种触发方式：当推送到 `main` 分支时、每 30 分钟自动一次、以及手动触发。默认每天凌晨 1 点触发。
- **常用设置**
  - 每 30 分钟触发一次：`'*/30 * * * *'`
  - 每小时触发：`'0 * * * *'`
  - 每天凌晨 1 点触发：`'0 1 * * *'`

#### 5. 触发 GitHub Actions

##### a. 提交更改

- 提交这些更改到你的仓库。这可以通过 GitHub 的网页界面或 git 命令行工具来完成。

##### b. 触发 GitHub Actions

- 提交更改将自动触发 GitHub Actions

- 如果没有启动 GitHub Actions 工作流，请按照以下步骤操作：
  1. 访问你 fork 后的仓库页面。
  2. 点击仓库顶部的 "Actions" 选项卡。
  3. 如果看到 GitHub 提示说 Actions 需要被启用，请点击 "I understand my workflows, go ahead and enable them" 按钮。

#### 6. 查看你的 mdBook

- 在几分钟后，访问 GitHub Pages 的 URL 查看你的 mdBook。URL 可以在仓库的 "Settings" -> "Pages" 部分找到。

通过遵循上述步骤，你可以轻松地 Fork 仓库、进行必要的配置更改，并通过 GitHub Actions 自动部署 mdBook 到 GitHub Pages。

## 与 mdBook-tools 配合使用

本项目使用了 [mdBook-tools](https://github.com/lzzsG/mdBook-tools) 仓库设计的一些工具和主题。删除theme文件夹可以使 mdbook 退回默认状态。

## 创建新的 Markdown 仓库

为了充分利用本项目的功能，你可以创建一个新的仓库专门用于存放 Markdown 文件，并组织一定的层次结构。使用本仓库自动生成目录和书籍并上线。
