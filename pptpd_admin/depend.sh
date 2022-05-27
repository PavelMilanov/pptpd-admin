#!/bin/bash

sed -n (sh -c "cat ../pyproject.toml | grep -n '\[tool.poetry.dependencies\]' | cut -d : -f 1", 10) ../pyproject.toml
# cat ../pyproject.toml | grep -n '\[tool.poetry.dependencies\]' | cut -d : -f 1
# cat ../pyproject.toml | grep -n '\[tool.poetry.dev-dependencies\]' | cut -d : -f 1
