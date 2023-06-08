# Similar Names
Library for Standardizing names from a Pandas dataframe

## Description
Similar Names is basically a package for names manipulation. That is, if you have a Pandas dataframe with multiple names written in different ways (e.g.: John Doe, John E. Doe and John Edson Doe), the "close_matches" function will look for all similar names on that column and then add two columns: "Close Matches" (list of all close matches) and "standard_name" (shortest name of the list).

## Instalation
Similar Names can be installed directly through pip
```
pip install similarnames
```

## How to use?
If you have a pandas dataframe with the names that you want to standardize, or look for close matches, simply follow the steps described next. As for the "close_matches" parameters, they are basically 6:
```python
close_matches(obj, names, sep = ',', connectors = ['and','e','y'], languages = ['english', 'portuguese', 'spanish'], custom_words = None)
```
- obj (dataframe): The pandas dataframe
- names (str): The name of the pandas dataframe with the names that you want to analyze
- sep (str or None): The separator to be used to split multiple names
- connectors (str, list or None): Words to also be used as separators (e.g.: "and")
- languages (str, list or None): Lanaguages for the default stopwords config (All stopwords are not considered names)
- custom_words (str, list or None): Additional words that should not be considered as names (e.g.: "jr")

### 1st Scenario: 1 name per row
In case your dataframe is already formatted with one name per row, simply execute the following command setting the "sep" parameter to "None". In case you are having some trouble with the results, you can set the "languages" and "custom_words" parameters to include, or exclude, names from the analyses (by default, stopwords in english, portuguese and spanish are not considered names).

```python
'''
Input (df): df and the name of the column with the names to check

| Names          | ... |
|----------------|-----|
| John Doe       |     |
| John Edson Doe |     |
| John E. Doe    |     |
| John Edson D.  |     |
'''
from similarnames import close_matches

# Default config: sep = ',', connectors = ['and','e','y'], languages = ['english', 'portuguese', 'spanish'], custom_words = None
df_standard = close_matches(df, 'Names', sep = None)

'''
Output (df_standard)

| Names          | ... | close_matches                                                   | standard_name |
|----------------|-----|----------------------------------------------------------------|--------------|
| John Doe       |     | ['John Doe', 'John E. Doe', 'John Edson Doe', 'John Edson D.'] | John Doe     |
| John Edson Doe |     | ['John Doe', 'John E. Doe', 'John Edson Doe', 'John Edson D.'] | John Doe     |
| John E. Doe    |     | ['John Doe', 'John E. Doe', 'John Edson Doe', 'John Edson D.'] | John Doe     |
| John Edson D.  |     | ['John Doe', 'John E. Doe', 'John Edson Doe', 'John Edson D.'] | John Doe     |

'''
```
### 2nd Scenario: Multiple names per row
In case you have multiple names in a single row, the "explode" is automatically done for you. So, just provide the "sep" parameter to identify where we should use to split those names. By default, the connectors "and", "e" and "y" will also be considered as separators. Therefore, in case you are working in a different language, just set the "connectors" and "languagues" parameter as you wish.

```python
'''
Input (df): df and the name of the column with the names to check

| Names                                        | Other columns           | ... |
|----------------------------------------------|-------------------------|-----|
| John Doe, Jane Doe                           | Two names (sep = ',')   |     |
| John E. Doe and Michael Johnson              | Two names (without sep) |     |
| Jane A. Doe, Michael M. Johnson and John Doe | Three names (sep = ',') |     |
'''
from similarnames import close_matches

# Default config: sep = ',', connectors = ['and','e','y'], languages = ['english', 'portuguese', 'spanish'], custom_words = None
df_standard = close_matches(df, 'Names', sep = ',')

'''
Output (df_standard)

| Names              | Other columns           | ... | close_matches                              | standard_name    |
|--------------------|-------------------------|-----|-------------------------------------------|-----------------|
| John Doe           | Two names (sep = ',')   |     | ['John Doe', 'John E. Doe']               | John Doe        |
| Jane Doe           | Two names (sep = ',')   |     | ['Jane Doe', 'Jane A. Doe']               | Jane Doe        |
| John E. Doe        | Two names (without sep) |     | ['John Doe', 'John E. Doe']               | John Doe        |
| Michael Johnson    | Two names (without sep) |     | ['Michael Johnson', 'Michael M. Johnson'] | Michael Johnson |
| Jane A. Doe        | Three names (sep = ',') |     | ['Jane Doe', 'Jane A. Doe']               | Jane Doe        |
| Michael M. Johnson | Three names (sep = ',') |     | ['Michael Johnson', 'Michael M. Johnson'] | Michael Johnson |
| John Doe           | Three names (sep = ',') |     | ['John Doe', 'John E. Doe']               | John Doe        |

'''
```
