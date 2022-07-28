import pandas as pd
from matplotlib import pyplot
from numpy import cov
from scipy.stats import pearsonr
from scipy import stats
from scipy.stats import spearmanr
from scipy.stats import ttest_ind


# importing the data as data frame
def importData(file):
  dataframe = pd.read_csv(file)
  df = dataframe[['Overall Rating','Compound']]
  print(df)

  return dataframe
  

# Calculate Covariance and Correlation
def correlation(overall_rating, avg_polarity):  
  print("======== Relation between variables ========")
  print()  
  covariance = cov(overall_rating, avg_polarity)[0][1]
  print('Covariance: ', covariance)

  # Pearson Correlation
  Pearsonscorr, _ = pearsonr(overall_rating, avg_polarity)
  print('Pearsons correlation: ', Pearsonscorr)

  # Spearman Correlation
  Spearmanscorr, _ = spearmanr(overall_rating, avg_polarity)
  print('Spearmans correlation: ', Spearmanscorr)



# Plotting the Scatterplot and Regression Slope (line of best fit)
def plotting(overall_rating,avg_polarity):

  pyplot.scatter(overall_rating, avg_polarity)
  pyplot.xlabel('Overall Hotel Rating')
  pyplot.ylabel('Average Polarity Score (Compound)')

  slope, intercept, _, _, _ = stats.linregress(overall_rating, avg_polarity)

  print("Slope: ",slope)

  #Calculating the Regression Slope
  def RegressionSlope(overall_rating):
    return slope * overall_rating + intercept

  slopeLine = list(map(RegressionSlope, overall_rating))
  pyplot.plot(overall_rating, slopeLine)
  
  #Save image as file
  pyplot.savefig('correlation.png')
  pyplot.show()


if __name__ == "__main__":

  #Import data for Average polarity of each hotel
  dataframe = importData('polarity_final.csv')
  #Take overall_rating and avg_polarity as dimentions
  overall_rating = dataframe['Overall Rating']
  avg_polarity = dataframe['Compound']
  #Call correlation function to get covariance and correlation
  
  correlation(overall_rating,avg_polarity)
  # Plot the scatterplot and regression line
  plotting(overall_rating,avg_polarity)
  