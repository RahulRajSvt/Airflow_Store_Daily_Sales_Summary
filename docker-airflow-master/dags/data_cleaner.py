
import pandas as pd
import re 

def data_cleaner():
	# read data 
	df = pd.read_csv("~/store_files_airflow/raw_store_transactions.csv")
	# Convert the date column
	df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')

	def clean_store_location(st_loc):
		return re.sub(r'[^\w\s]', '', st_loc).strip()

	def clean_product_id(pd_id):
		matches = re.findall(r'\d+', pd_id)
		if matches:
			return matches[0]
		return pd_id

	def remove_dollar(x):
		return float(x.replace("$", ""))

	# remove store location 
	df['STORE_LOCATION'] = df['STORE_LOCATION'].apply(lambda x: clean_store_location(x))

	# cleanup product id 
	df['PRODUCT_ID'] = df['PRODUCT_ID'].apply(lambda x: clean_product_id(x))

	# remove dollar from MRP, CP, DISCOUNT, SP 
	for to_clean in ['MRP', 'CP', 'DISCOUNT', 'SP']:
		df[to_clean] = df[to_clean].apply(lambda x: remove_dollar(x))

	df.to_csv("~/store_files_airflow/clean_raw_store_transactions.csv", index=False)