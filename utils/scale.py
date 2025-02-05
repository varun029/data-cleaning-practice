from mlxtend.preprocessing import minmax_scaling

def minmax(df,x):
    scaled_df=minmax_scaling(df,columns=[x])
    return scaled_df

def compare_data(df,scaled_df):
    print(f'preview of original data:\n {df.head()}')
    print(f'Minimum value: {df.min()}')
    print(f'Maximum value: {df.max()}')
    print('\n')

    print(f"preview of scaled data:\n {scaled_df.head()}")
    print(f'Minimum value: {scaled_df.min()}')
    print(f'Maximum value: {scaled_df.max()}')
    print('\n')


    
