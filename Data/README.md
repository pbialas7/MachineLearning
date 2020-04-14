# Data

## Content

### Height and Weight 

This directory contains data take from this [kaggle dataset](https://www.kaggle.com/mustafaali96/weight-height). This data set does not contain any  description of origin but use of inches and pounds suggests an american or english population. The data consists of 10000 data samples each specifying sex, height and weight of one person.

### A/B

Data taken from Kaggle [Mobile games: A/B Testing](https://www.kaggle.com/yufengsui/mobile-games-ab-testing) used in the bayesian_analysis notebook. It concerns an A/B test with a mobile game [Cookie Cats](https://tactilegames.com/cookie-cats/). The players were given two versions of the game differing by the level were the first gate that forced them to wait was placed. Measured was the retention on day one and  day seven as well as total number of game rounds played  during firts 14 days. 

### Cars

The [car evaluation dataset](http://archive.ics.uci.edu/ml/datasets/Car+Evaluation) from [UCI Machine Learning repository](http://archive.ics.uci.edu/ml/). It contains 1728 samples with six atttributes (features) each. The class label is the evaluation of the car: unacc, acc, good, vgood.

### Amazon reviews 

The Amazon review data set. This data set is very handy because it contains both documents (reviews) and labels (ratings). The original data set is HUGE  and can be  _e.g._ found [here](http://jmcauley.ucsd.edu/data/amazon/). We will use the preprocessed data from
[ Xiang Zhang's Google Drive dir](https://drive.google.com/open?id=0Bz8a_Dbh9Qhbfll6bVpmNUtUcFdjYmF2SEpmZUZUcVNiMUw1TWN6RDV3a0JHT3kxLVhVR2M) that can be downloaded as a tar archive. However it still has 1.5GB of data. So for the sake of this lecture I have prepared a smaller sample that I have additionally compressed with 'bz2' reducing the size to "only" 41MB. You can play with original file by downloading it directly from the above link. 

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