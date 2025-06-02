import pandas as pd

if __name__ == "__main__":

  # Create a DataFrame with 8 columns and 8 rows, all integers numbered off
  data = [[i * 8 + j + 1 for j in range(8)] for i in range(8)]
  columns = [f"Col{j+1}" for j in range(8)]

  df = pd.DataFrame(data, columns=columns)
  print("Original DataFrame:")
  print(df)

  # Swap columns 4 and 5 (Col4 and Col5)
  cols = df.columns.tolist()

  n = 4
  rotated = cols[n:] + cols[:n]

  # for i in range(len(cols)):
  #   print(cols[i])

  #cols[3], cols[4] = cols[4], cols[3]
  
  df = df[rotated]

  print("\nAfter swapping columns 4 and 5:")
  print(df)

# interesting! what I actually learnt here wasn't pandas but list slicing and multivalue assignment!
# (ok so I also learnt that you can reorder columns with the [] operator on the dataframe)

