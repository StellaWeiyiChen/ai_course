import glob
import os, json
import pandas as pd
import numpy as np
from datetime import date

def get_data(path):
	all_files=glob.glob(os.path.join(path,"*.json"))
	rename_dictionary={"StreamID":"stream_id","TimesViewed":"times_viewed","total_price":"price"}
	dfs=[pd.read_json(f).rename(columns=rename_dictionary) for f in all_files]
	df=pd.concat(dfs)
	df["date"]=df.year.astype(str)+"-"+df.month.astype(str).str.zfill(2)+"-"+df.day.astype(str).str.zfill(2)
	df.invoice=df.invoice.astype(str).str.replace("[a-zA-Z]","")

	return df.drop_duplicates()


