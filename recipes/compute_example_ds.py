# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu



# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

example_ds_df = pd.DataFrame(data = pd.date_range(start = '2022-01-25', end = '2022-05-01'))

print("this is a random line")
print("another line :/")

# entered a few more lines

# Write recipe outputs
example_ds = dataiku.Dataset("example_ds")
example_ds.write_with_schema(example_ds_df)

print("if you want to, I can be with youuu")

# this comment should take precedence