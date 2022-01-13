# -*- coding: utf-8 -*-
import pandas as pd
from helpers import retail_data_prep, reduce_mem_usage
from mlxtend.frequent_patterns import apriori, association_rules

# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 500)
# pd.set_option('display.expand_frame_repr', False)

DATA_DIR = '/data/online_retail_II.xlsx' # check if it's correct
SHEET_NAME = 'Year 2010-2011'
MIN_SUPPORT_VALUE = 0.01
NUM_RECOMMEND = 5

raw_df = pd.read_excel(DATA_DIR, sheet_name=SHEET_NAME, engine='openpyxl')
raw_df = retail_data_prep(raw_df)  # preprocess
df = raw_df.copy()

# we want to recommend products to these user product ids
user_product_ids = [21987, 23235, 22747]

# just in France
df_fr = df[df['Country'] == 'France']

def get_product_name(df_, product_id):
    return df_fr[df_fr['StockCode'] == product_id]['Description'].values[0]

for id in user_product_ids:
  p_name = get_product_name(df_fr, id)
  print(f'product id: {id} name: {p_name}')

# convert invoice-stock code matrix
agg_df_fr = pd.pivot_table(df_fr, index='Invoice', columns='StockCode', values='Quantity', aggfunc='sum').fillna(0). \
                           applymap(lambda quantity: 1 if quantity > 0 else 0)

agg_df_fr_reduced = reduce_mem_usage(agg_df_fr) # reduce the memory usage of the dataframe

support_values = apriori(agg_df_fr_reduced, min_support=MIN_SUPPORT_VALUE, use_colnames=True)
support_values.sort_values('support', ascending=False).head(10)

rules = association_rules(support_values, metric="support", min_threshold=MIN_SUPPORT_VALUE)
rules.sort_values("support", ascending=False).head(10)

# get recommandations for given product_id
def arl_recommender(rules_df, product_id, num_item=1):
    sorted_rules = rules_df.sort_values("lift", ascending=False)

    recommend_list = []
    for i, product in sorted_rules["antecedents"].items():
        for j in list(product):
            if j == product_id:
                recommend_list.append(list(sorted_rules.iloc[i]["consequents"]))

    recommend_list = list({item for item_list in recommend_list for item in item_list})
    return recommend_list[:num_item]


for id in user_product_ids:
  recommend_list = arl_recommender(rules, id, NUM_RECOMMEND)
  print(f"Recommandations for product id: {id} name: {get_product_name(df_fr, id)}")
  for rec_id in recommend_list:
    print(f"  id: {rec_id} name: {get_product_name(df_fr, rec_id)}")
  print()

