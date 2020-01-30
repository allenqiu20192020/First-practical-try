import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
#data_frame['time'] = data_frame['time'].str.strip('')
data_frame.dropna(subset=['time'], inplace = True)
data_frame.to_csv(output_file, encoding='utf_8_sig')