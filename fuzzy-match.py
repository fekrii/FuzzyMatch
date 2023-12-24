# Importing the 'fuzz' module from the 'fuzzywuzzy' library for fuzzy string matching
from fuzzywuzzy import fuzz

# Function to perform partial fuzzy matching
def partial_fuzzy_match(term, database):
    # Splitting the input
    term_chunks = term.split(" - ")
    matches = []  

    # Iterating through each entry in the database
    for entry in database:
        # Splitting each entry into chunks using the separator " - "
        entry_chunks = entry.split(" - ")
        
        # Calculating the maximum similarity between chunks of the term and entry
        max_similarity = max(
            fuzz.token_sort_ratio(chunk, entry_chunk)
            for chunk in term_chunks
            for entry_chunk in entry_chunks
        )
        
        # Checking if the maximum similarity exceeds a predefined threshold
        if max_similarity > SIMILARITY_THRESHOLD:
            # Appending the matching entry and its similarity to the list
            matches.append({'entry': entry, 'similarity': max_similarity})
    
    return matches

# Function to process a list of input strings against a database
def process_input(input_strings, database):
    results = {}

    # Iterating through each input term in the list
    for term in input_strings:
        # Performing partial fuzzy matching for the current term
        matches = partial_fuzzy_match(term, database)
        
        # Checking if there are any matches for the current term
        if matches:
            results[term] = matches
    
    return results



# Example usage
input_strings = ["ahmed - karim - ali"]
database = ["osss", "ohgn - kari", "oikk - hgnjs"]
SIMILARITY_THRESHOLD = 70  # Threshold for considering a match


results = process_input(input_strings, database)


print(results)
