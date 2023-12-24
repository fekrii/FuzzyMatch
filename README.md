# Fuzzy String Matching Tool

## Overview

This Python script provides a versatile tool for performing partial fuzzy matching of input terms against a given database. The functionality is implemented using the `fuzzywuzzy` library, which offers robust fuzzy string matching capabilities.

## Features

1. **Partial Fuzzy Matching**: The `partial_fuzzy_match` function takes a term and a database of entries, splitting them into chunks and calculating the maximum similarity between chunks. Entries with a similarity score exceeding a predefined threshold are considered matches.

2. **Input Processing**: The `process_input` function processes a list of input strings against the database, utilizing the partial fuzzy matching function. It returns a dictionary of input terms with corresponding matching entries and their similarities.

## Usage

### 1. Install Dependencies

Make sure to install the required dependencies by running:

```bash
pip install fuzzywuzzy

```


## Example
With the provided example input, the script will output a dictionary containing the input term and a list of matching entries along with their similarity scores.