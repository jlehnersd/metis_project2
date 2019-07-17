
def basic_lr_model(y_idx):
    """
    Reads cleaned data set from clean_data.csv and runs it as is
    through an OLS linear regression model using statsmodels.api
    
    Input
    -----
    y_idx: column index of the clean data set that corresponds to the predicted variable
    
    Output
    ------
    model : the OLS model computed by statsmodel.api.OLS()
    fit   : best fit of the OLS model to the data 
    """
    
    # Import relevant modules
    import patsy
    import pandas as pd
    import statsmodel.api as sm
    
    # Read in clean data
    datadir = '/Users/jeremy_lehner/Documents/GitHub/metis_project2/data/processed/clean_data.csv'
    df = pd.read_csv(datadir)
    
    # Construct R formula style string
    colnames = list(df.columns)
    y_name = colnames[y_idx]
    colnames.remove(y_name)
    
    R_formula = y_name + ' ~ ' + ' + '.join(colnames)
    
    # Construct target vector y and feature matrix X
    y, X = patsy.dmatrices(R_formula, data = df, return_type = "dataframe")
    
    # Construct OLS model
    model = sm.OLS(y, X)

    # Fit model to training set
    fit = model.fit()
    
    # Return the model and the fit
    return model, fit

# write functions that form a data pipeline, 
# then run this cell to save them in src/obtain.py
