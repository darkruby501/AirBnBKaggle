
# coding: utf-8

# In[ ]:

def preprocess_users(df):
    ##AGE
    #Remove all ages outside of range, set to -1 for separate categorisation
    df.loc[df.age > 95, 'age'] = -1
    df.loc[df.age < 13, 'age'] = -1
    df.fillna(-1,inplace=True)

    ## GENDER
    # Set missing values to own category
    df['gender'].replace('-unknown-',np.nan, inplace=True)
    df['gender'].fillna('MISSING',inplace=True)

    ## FIRST AFFILIATE TRACKED
    # Set missing to untracked, hopefully the same
    df['first_affiliate_tracked'].fillna('untracked',inplace=True)
    
    return df

