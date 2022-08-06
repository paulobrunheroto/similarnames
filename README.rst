# Similar Names
Library for Standardizing names from a Pandas dataframe

## Description
Similar Names is basically a package for names manipulation. That is, if you have a Pandas dataframe with multiple names written in different ways (e.g.: John Doe, John E. Doe and John Edson Doe), the "closeMatches" function will look for all similar names on that column and then add two columns: "Close Matches" (list of all close matches) and "StandardName" (shortest name of the list).

## Instalation
Similar Names can be installed directly through pip
`pip install similarnames`

## How to use?
If you have a pandas dataframe with the names that you want to standardize, or look for close matches, simply execute the following command.

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
from similarnames import closeMatches

df_standard = closeMatches(df, 'Names')

'''
Output (df_standard)

| Names          | ... | CloseMatches                                                   | StandardName |
|----------------|-----|----------------------------------------------------------------|--------------|
| John Doe       |     | ['John Doe', 'John E. Doe', 'John Edson Doe', 'John Edson D.'] | John Doe     |
| John Edson Doe |     | ['John Doe', 'John E. Doe', 'John Edson Doe', 'John Edson D.'] | John Doe     |
| John E. Doe    |     | ['John Doe', 'John E. Doe', 'John Edson Doe', 'John Edson D.'] | John Doe     |
| John Edson D.  |     | ['John Doe', 'John E. Doe', 'John Edson Doe', 'John Edson D.'] | John Doe     |

'''
```

In case you have multiple names in a single row, the "explode" is automatically done for you. So, just provide the "sep" parameter to identify where we should use to split those names. Note: If you have an "and" (e.g.: Jon and Jane), it will be automatically replaced by the "sep" parameter before the split.

```python
'''
Input (df): df and the name of the column with the names to check

| Names                                        | Other columns           | ... |
|----------------------------------------------|-------------------------|-----|
| John Doe, Jane Doe                           | Two names (sep = ',')   |     |
| John E. Doe and Michael Johnson              | Two names (without sep) |     |
| Jane A. Doe, Michael M. Johnson and John Doe | Three names (sep = ',') |     |
'''
from similarnames import closeMatches

df_standard = closeMatches(df, 'Names', sep = ',')

'''
Output (df_standard)

| Names              | Other columns           | ... | CloseMatches                              | StandardName    |
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