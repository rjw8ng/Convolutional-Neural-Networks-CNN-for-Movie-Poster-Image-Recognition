# Convolutional Neural Networks (CNN) for Movie Poster Image Recognition

Team Members: Brennan Danek (bd4bk), Theodore Thormann (nbx5kp) , Royal Wang (rjw8ng)

## Folder structure
* `Data`: Contains SamplePosters, All Posters, and csv files with poster lists

* `Models`
  * `Deep Learning Final Project (Full Posters)`: CNN model using all poster data
  * `Deep Learning Final Project (Sample Posters)`: CNN model using sample poster data (subset)

## Motivation:

The motivation behind using movie posters to determine movie genres with deep learning is to develop an automated and efficient method for classifying movies into different genres. Movie posters are designed to convey information about the movie and attract an audience. One important piece of information that movie posters could possibly convey would be the style or genre of the movie. If we can see if a movie’s genre can be predicted by the movie’s poster, then using a movie poster as data may be helpful in other neural network processes like recommendation algorithms.

In addition, using movie posters for genre classification has practical applications in the movie industry, such as helping with marketing and advertising efforts. By accurately predicting the genre of a movie based on its poster, studios can better target their marketing campaigns and attract audiences who are interested in that genre. This is an application result since further research can be done to advise movie producers to use certain colors or patterns when creating posters. 

## Dataset:

The dataset contains information on movie posters and their respective genres. The dataset contains a total of 7,748 movie posters, each with a corresponding genre label. The dataset is intended to be used for machine learning tasks, such as image classification or genre prediction based on movie posters.

The dataset includes the following features:

* Poster_Path: a string representing the file path of the movie poster image
* Genre: a string representing the genre(s) of the movie, with multiple genres separated by a pipe (|) symbol

There are 17 movie genres: action, adventure, animation, comedy, crime, documentary, drama, family, fantasy, history, horror, music, mystery, romance, science fiction, thriller, and war.

The genre labels were assigned based on data available on IMDb and TMDb websites and may not accurately represent the actual genres of the movies. Additionally, some movie posters may contain multiple genres, while others may not have any genre information available.

The dataset is from Kaggle:
https://www.kaggle.com/datasets/neha1703/movie-genre-from-its-poster

## Related Work:

The article "Analysis of top box office film poster marketing schemes based on data mining and deep learning in the context of film marketing" discusses the use of data mining and deep learning techniques to analyze the effectiveness of film poster marketing strategies for top box office films. The authors collected data on the top 200 box office films from 2015-2019, including film posters, box office revenue, and critical ratings. They then used data mining and deep learning techniques to analyze the relationships between film poster features, such as color, font, and image content, and box office revenue and critical ratings. The article highlights the potential of data mining and deep learning techniques to provide insights into the effectiveness of film marketing strategies and inform decision-making in the film marketing industry.

The article is from the NIH:
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9879408/

## Technical Plan:

The inputs for the CNN model are the movie poster images, which are normalized to be the same dimensions. The outputs would be a multi classification where only genres whose softmax output is over a certain threshold are not zeroed out. Then, each genre who meets the threshold is given a value of 1 / (# of genres past threshold). This will allow our loss function to minimize loss. 

We could use a number of different ImageNet winning recognition: VGG, ResNet, AlexNet. ResNet performs the best in image recognition out of these while also being the most efficient. To observe the results of ResNet, we will be using both ResNet50 and ResNet152. In addition, a DenseNet model will be created to diversify our model group.

For the loss functions, we are using Binary Cross Entropy Loss with Logit transformation for multilabel classification. 

## Evaluation Plan:

We plan to run a CNN model with 10 - 50 epochs with three different models. With each model, we will observe accuracy and make changes to the model to increase accuracy. We plan on evaluating the machine learning algorithm through two main ways: accuracy and processing speed. We want a model that will provide the best result but also be able to get to that result in a reasonable time.

