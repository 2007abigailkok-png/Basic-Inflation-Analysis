import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("cpi_data.xlsx")

# Cleaning data
data_long = data.melt(
    id_vars=["Division",
        "DivisionDescription",
        "Group",
        "GroupDescription",
        "Class",
        "ClassDescription",
        "Subclass",
        "SubclassDescription",
        "Old code",
        "Eight digit code",
        "Product name",
        "Weight",
        "Base period"
    ],
    var_name="Month" ,
    value_name="Index"
)

data_long["Month"] = data_long["Month"].str.replace("M" , "")
data_long["Month"] = pd.to_datetime(data_long["Month"] , format = "%Y%m")

data_long = data_long.set_index("Month")
yearly_average_per_product = data_long.groupby("Product name").resample("YE")["Index"].mean()

data_long["Year"] = data_long.index.year

print(data_long.info())
print(data_long.head(5))
print(data_long.describe())

# Calculating Cost Price Index Over Time
yearly = data_long.groupby("Year")["Index"].mean()

yearly.plot(kind="line")
plt.title("Cost Price Index Over Time")
plt.show()

# The average Inflation
yearly = yearly.reset_index()
yearly["YoY Total Change"] = yearly["Index"].pct_change(fill_method = None)
print("The average inflation from 01/01/2008 to 01/04/2026:")
print(yearly["YoY Total Change"].mean())

# Calculating Average Cost by Divsion
division_index = data_long.groupby("DivisionDescription")["Index"].mean()

division_index.plot(kind='bar')
plt.title("Average Cost by Divsion")
plt.show()

# Calculating Cost Trends by Division
for division in data_long["DivisionDescription"].unique():
    subset = data_long[data_long["DivisionDescription"] == division]
    divsion_average = subset.groupby("Year")["Index"].mean()
    plt.plot(divsion_average.index, divsion_average.values, label=division)


plt.legend(loc="best")
plt.title("Cost Trends by Division")
plt.tight_layout()
plt.show()

# Calculating relationship between food and transport indices
comparison_div = ["Food and non-alcoholic beverages" , "Transport"]

for division in comparison_div:
    subset = data_long[data_long["DivisionDescription"] == division]
    divsion_average = subset.groupby("Year")["Index"].mean()
    plt.plot(divsion_average.index, divsion_average.values, label=division)


plt.legend(loc="best")
plt.title("Food vs. Transport")
plt.tight_layout()
plt.show()


# Calculating products with most volatile indices
product_price_dev = data_long.groupby("Product name")["Index"].std()
product_price_dev_df = product_price_dev.reset_index(name="Standard Deviation of Index")
print()
print("The products with the most volatile indices:")
print(product_price_dev_df.nlargest(5 , "Standard Deviation of Index")
      [["Product name" , "Standard Deviation of Index"]])

# Calculating divisions with most volatile indices
div_price_dev = data_long.groupby("DivisionDescription")["Index"].std()
div_price_dev_df = div_price_dev.reset_index(name="Standard Deviation of Index")
print()
print("The divisions with the most volatile indices:")
print(div_price_dev_df.nlargest(5 , "Standard Deviation of Index")
      [["DivisionDescription" , "Standard Deviation of Index"]])

# Calculating products that experienced the greatest growth in their index
data_sorted = data_long.sort_values(["Product name" , "Month"])
first_val = data_sorted.groupby("Product name")["Index"].first()
last_val = data_sorted.groupby("Product name")["Index"].last()
growth = ((last_val / first_val) - 1)
growth_df = growth.reset_index(name="Total Growth")
print()
print("The products which experienced the most decimal growth:")
print(growth_df.nlargest(5 , "Total Growth")
      [["Product name" , "Total Growth"]])

# Calculating divisions that experienced the greatest growth in their index
first_val = data_sorted.groupby("DivisionDescription")["Index"].first()
last_val = data_sorted.groupby("DivisionDescription")["Index"].last()
growth = ((last_val / first_val) - 1)
growth_df = growth.reset_index(name="Total Growth")
print()
print("The divisions which experienced the most decimal growth:")
print(growth_df.nlargest(5 , "Total Growth") 
      [["DivisionDescription" ,"Total Growth"]])

# Calculating Month-by-Month and Year-on-Year Product Index Change
data_long = data_long.sort_values(
    ["DivisionDescription" , "Product name" , "Month"]
)

data_long["MoM product Change"] = (
    data_long.groupby(["DivisionDescription" , "Product name"])["Index"].pct_change(fill_method=None)
)

print()
print("The items with the largest Month-by-Month decimal change:")
print(data_long.nlargest(5, "MoM product Change")
      [['Product name' , 'MoM product Change']])

yearly_avg = (
    data_long.groupby(["Product name" , "Year"])["Index"].mean()
    .reset_index()
)

yearly_avg = yearly_avg.sort_values(["Product name" , "Year"])

yearly_avg["YoY product Change"] = yearly_avg.groupby("Product name")["Index"].pct_change(fill_method = None)

print()
print("The items with the largest Year-on-Year decimal change:")
print(yearly_avg.nlargest(5, "YoY product Change")
      [['Year' , 'Product name' , 'YoY product Change']])

# Calculating Month-by-Month and Year-on-Year Average Division Index Change
division_mom = (
    data_long.groupby(["DivisionDescription", "Month"])["MoM product Change"]
    .mean()
    .reset_index()
    .set_index("Month")
    .rename(columns={"MoM product Change" : "MoM division Change"})
)

print()
print("The divisions with the largest Month-by-Month decimal change:")
print(division_mom.nlargest(5 , "MoM division Change"))

yearly_avg = (
    data_long.groupby(["DivisionDescription", "Year"])["Index"]
    .mean()
    .reset_index()
)

yearly_avg = yearly_avg.sort_values(["DivisionDescription" , "Year"])

yearly_avg["YoY division Change"] = yearly_avg.groupby("DivisionDescription")["Index"].pct_change(fill_method = None)

print()
print("The divisions with the largest year-on-year decimal change:")
print(yearly_avg.nlargest(5 , "YoY division Change"))
