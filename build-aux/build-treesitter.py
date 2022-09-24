#!/usr/bin/env python3

from tree_sitter import Language

Language.build_library(
    "frida_tools/treesitter.so",
    [
        "vendor/tree-sitter-javascript",
    ],
)
