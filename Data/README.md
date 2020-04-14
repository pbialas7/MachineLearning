# Data

## Content

### Height and Weight 

This directory contains data take from this [kaggle dataset](https://www.kaggle.com/mustafaali96/weight-height). This data set does not contain any  description of origin but use of inches and pounds suggests an american or english population. The data consists of 10000 data samples each specifying sex, height and weight of one person.

### A/B

Data taken from Kaggle [Mobile games: A/B Testing](https://www.kaggle.com/yufengsui/mobile-games-ab-testing) used in the bayesian_analysis notebook. It concerns an A/B test with a mobile game [Cookie Cats](https://tactilegames.com/cookie-cats/). The players were given two versions of the game differing by the level were the first gate that forced them to wait was placed. Measured was the retention on day one and  day seven as well as total number of game rounds played  during firts 14 days. 

### Cars

The [car evaluation dataset](http://archive.ics.uci.edu/ml/datasets/Car+Evaluation) from [UCI Machine Learning repository](http://archive.ics.uci.edu/ml/). It contains 1728 samples with six atttributes (features) each. The class label is the evaluation of the car: unacc, acc, good, vgood.

### Amazon reviews 

As an example we will use the [car evaluation dataset](http://archive.ics.uci.edu/ml/datasets/Car+Evaluation) from [UCI Machine Learning repository](http://archive.ics.uci.edu/ml/). It contains 1728 samples with six atttributes (features) each. The class label is the evaluation of the car: unacc, acc, good, vgood.

The data was selected using the code below. 

```
from sklearn.model_selection import train_test_split
seed = 85865
data = pd.read_csv("../../Data/amazon_reviews/train.csv",
                   names=["rating", "title", "review"])
small_data,_ = train_test_split(data,train_size=300000,  stratify=data['rating'], random_state=seed)
small_data.to_csv("../../Data/amazon_reviews/small.csv.bz2", index=False, compression='bz2')
```

Use of the 'stratify' argument  guarantee that proportion of each ratings will be  preserved. In this case we will have same number of documents with each rating. The smaller file can be read in using:

```
import pandas
data = pd.read_csv("../../Data/amazon_reviews/small.csv.bz2", compression='bz2')
```