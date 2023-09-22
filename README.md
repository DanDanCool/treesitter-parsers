# treesitter-parsers

## this is for my fellow neglected windows users

how to build parsers:

- clone recursively
- optional
  - in each submodule, `npm install` + `npx tree-sitter --generate {vim.treesitter.language\_version}`
  - do this if you encounter problems
- `pip install jmake` (python build c/c++ build system)
- `python parsers.py` (generates visual studio project files)
- open the sln file under the newly created bin folder in visual studio and build each project
- copy and rename each dll to `{lang}.so` under the parser folder in your nvim configs
- use the up to date scheme files from https://github.com/nvim-treesitter/nvim-treesitter
