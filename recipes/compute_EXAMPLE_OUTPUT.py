# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
example_output_df = pd.DataFrame(data = pd.date_range(start = '2022-01-25', end = '2022-11-30'))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
example_output_df

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
example_output = dataiku.Dataset("EXAMPLE_OUTPUT")
example_output.write_with_schema(example_output_df)