# `wcp`: with-copy

Copy files from one directory to another.

## Usage

```bash
FROM=some/dir TO=some/other wcp [files...]
```

## Description

Avoid repeating long directory names by specifying them in
an environment variable.
Like with most command-line tools, omitting either `FROM` or `TO`
will default to the current directory.

## Installation

Clone the repo, and add an alias to your shell's startup script.
Using bash as an example:

```bash
git clone https://github.com/KyussCaesar/wcp.git
echo "alias wcp=`pwd`/wcp/main.py" >> ~/.bashrc
```

