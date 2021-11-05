import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
soup = BeautifulSoup(webpage.content, "html.parser")
ratings = []
turtle = soup.find_all(attrs={"class": "Rating"})
for row in turtle[1:]:
  ratings.append(float(row.get_text()))
plt.hist(ratings)
plt.show()
company_names = soup.select(".Company")
# The way of using .find_all
list_of_company = []
company = soup.find_all(attrs={"class": "Company"})
for row in company[1:]:
  list_of_company.append(row.get_text())
print(list_of_company)
# The way of using .select (but it can be dangerous)
d = {"Ratings": ratings, "List of company": list_of_company}
my_df = pd.DataFrame.from_dict(d)
mean_ratings = my_df.groupby("List of company").Ratings.mean()
ten_best = mean_ratings.nlargest(10)
print(ten_best)

cocoa_percentage = []
cocoa_staff = soup.find_all(attrs={'class': 'CocoaPercent'})
for element in cocoa_staff[1:]:
  cocoa_percentage.append(element.get_text().strip('%'))
print(cocoa_percentage)
d.update({"CocoaPercentage": cocoa_percentage})
my_df = pd.DataFrame.from_dict(d)
print(my_df)
#Make a scatterplot of ratings
plt.scatter(df.my_df, df.my_df)
plt.show()
z = np.polyfit(df.my_df, df.my_df, 1)
line_function = np.poly1d(z)
plt.plot(df.my_df, line_function(df.my_df), "r--")