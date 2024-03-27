# all-to-mdbook Automated Deployment of mdBook Repositories

English | [中文](README.md)

This repository aims to provide an automated way to deploy repositories containing Markdown file structures to mdBook. Utilizing GitHub Actions, it can automatically identify Markdown files in a specified repository and generate the corresponding mdBook. Furthermore, it supports custom configurations, such as the target repository link, ignoring specific folders, and enabling natural sorting, making the structure of the generated books more logical and aesthetically pleasing.

## Features

- Automated generation of the mdBook directory.
- Support for custom target repository links.
- Support for ignoring specific folders to avoid displaying empty folders in the directory.
- Support for natural sorting, allowing for correct ordering of numbers in the directory (e.g., `1, 2, ..., 10, 11`).
- Ability to set automatic trigger intervals through workflow configuration files.
- Recognition of `README.md` files and placing them at the top.
- Designed using the typography theme from the mdBook-tools repository.

## Configuration

The configuration of this project is done through the `config.ini` file, which contains two main sections: `src` and `repository`.

### Example Configuration

```ini
[src]
directory = ./src
output_file = ./src/SUMMARY.md
ignore_dirs = .git,figs,examples,figures,.github
use_natural_sort = True

[repository]
url = https://github.com/yourusername/yourrepository
```

- `directory`: Specifies the source directory of the md files.
- `output_file`: Specifies the generated directory file.
- `ignore_dirs`: Specifies a list of directories to ignore.
- `use_natural_sort`: Whether to enable natural sorting.
- `url`: The link to the target repository.

## Workflow Automation

This project configures a GitHub Actions workflow through the `.github/workflows/mdbook.yml` file to automate the generation and deployment of mdBook.

### Workflow Configuration

```yaml
schedule:
  - cron: '*/6 * * * *'
```

#### Meaning of the Interval

The `cron` expression `'*/6 * * * *'` means triggering the workflow every 6 minutes.

## How to Use

#### 1. Fork the Repository

- Click the "Fork" button in the top right corner to fork the repository to your GitHub account.

#### 2. Enable GitHub Pages

- Go to the "Settings" of your forked repository.
- Find the "Pages" section.
- In the "Build and deployment" option, select "GitHub Actions."

#### 3. Modify the Configuration File

##### a. `config.ini` - Customize directory structure, exclusion rules, target repository link

Find the `config.ini` file in your project and modify it according to the following template to suit your project needs:

```ini
[src]
ignore_dirs = .git,figs,examples,figures,.github
use_natural_sort = True

[repository]
url = https://github.com/your_target_repository
```

- `ignore_dirs`: Adjust `ignore_dirs` as needed to ignore folders not required to be included in the mdBook directory, separated by commas.
- `use_natural_sort`: Whether to enable natural sorting.
- **`url`: The link to the target repository for generating the mdbook.**

##### b. `book.toml` - Customize book information

Find the `[book]` section in `book.toml` and modify `title` to set your book title; in the `[output.html]` section, modify `git-repository-url` to set the GitHub icon redirect link:

```toml
[book]
title = "Your Book Title"
[output.html]
git-repository-url = "https://github.com/your_username/your_repository"
```

##### c. Customize Navigation

- Find the `theme/index.hbs` file.
- Around line 180, modify the HTML code as needed to customize the book's navigation bar. Or remove the navigation (`<a>` wrapped content).

#### 4. Configure `mdbook.yml` Trigger Events (Optional)

In the `.github/workflows/mdbook.yml` file, you can set trigger events:

```yaml
on:
  push:
    branches: ["main"]
  schedule:
    - cron: '0 1 * * *' # Trigger at 1 AM every day
  workflow_dispatch:
```

- This configures three trigger methods: when pushing to the `main` branch, automatically triggering once every hour, and manual triggering.
- Common settings:
  - Trigger every 30 minutes: `'*/30 * * * *'`
  - Trigger every hour: `'0 * * * *'`
  - Trigger at 1 AM every day: `'0 1 * * *'`

#### 5. Trigger GitHub Actions

##### a. Commit Changes

- Commit these changes to your repository. This can be done through GitHub's web interface or the git command line tool.

##### b. Trigger GitHub Actions

- Committing changes will automatically trigger GitHub Actions.
- If the GitHub Actions workflow does not start, follow these steps:
  1. Visit the page of your forked repository.
  2. Click on the "Actions" tab at the top of the repository.
  3. If you see a prompt from GitHub saying Actions need to be enabled, click the "I understand my workflows, go ahead and enable them" button.

#### 6. View Your mdBook

- After a few minutes, visit the URL of GitHub Pages to view your mdBook. The URL can be found in the "Settings" -> "Pages" section of the repository.

By following these steps, you can easily fork the repository, make the necessary configuration changes, and automatically deploy mdBook to GitHub Pages through GitHub Actions.

## Using with mdBook-tools

This project utilizes some tools and themes designed by the [mdBook-tools](https://github.com/lzzsG/mdBook-tools) repository. Deleting the theme folder will revert mdbook to its default state.

## Creating a New Markdown Repository

To fully leverage the features of this project, you can create a new repository specifically for storing Markdown files, organizing them with a numerical prefix and folder structure. Use this repository to automatically generate a directory and book online.