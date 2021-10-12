
class preprocessor:
    def __init__(self,df):
        self.df = df



    def eda(self):
        numericalColumns = self.df.select_dtypes(include = ["int64","float64","datetime64[ns]"]).columns 
        print(" Size of the data set is",self.df.shape,"\n")
        for column in self.df.columns:
            if(self.df[column].unique().shape[0] == 1 ):
                print("\ncolumn: ",column ) 
                print(column, " has zero variance")
            elif(self.df[column].unique().shape[0] > 1 and self.df[column].unique().shape[0] < 100):
                print("\ncolumn: ",column )
                #print("Unique values : ",self.df[column].unique().shape[0]) 
                print(f"Number of Unique values: {self.df[column].unique().shape[0]}")
                if column in numericalColumns:
                    print(f"min = {self.df[column].min()}, max = {self.df[column].max()}, range = {self.df[column].max() - self.df[column].min()}")
                print("List\n",self.df[column].unique())
            else:
                print("\ncolumn: ",column )
                print(f"Number of Unique values: {self.df[column].unique().shape[0]}")
                if column in numericalColumns:
                    print(f"min = {self.df[column].min()}, max = {self.df[column].max()}, range = {self.df[column].max() - self.df[column].min()}")



        