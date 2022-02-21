import pandas as pd

# Load Origin Data
df_ic = pd.read_pickle('../data/IC_1m.pkl')
df_if = pd.read_pickle('../data/IF_1m.pkl')
df_ih = pd.read_pickle('../data/IH_1m.pkl')


#Calc Return
def calc_return(df):
    return df['close'].pct_change().fillna(method='bfill')

#Create the label
def generate_label(df, label_func, label):
    df_labeled = df.copy(deep=True)
    df_labeled[label] = label_func(df_labeled)
    return df_labeled

df_ic = generate_label(df_ic, calc_return, 'return')
df_if = generate_label(df_if, calc_return, 'return')
df_ih = generate_label(df_ih, calc_return, 'return')

df_ic.to_pickle('../data/data_processed/ic_processed.pkl')
df_if.to_pickle('../data/data_processed/if_processed.pkl')
df_ih.to_pickle('../data/data_processed/ih_processed.pkl')


