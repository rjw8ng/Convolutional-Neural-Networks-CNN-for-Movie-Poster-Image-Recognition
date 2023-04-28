# Convolutional Neural Networks (CNN) for Movie Poster Image Recognition

Team Members: Brennan Danek (bd4bk), Theodore Thormann (nbx5kp) , Royal Wang (rjw8ng)

## Folder structure
* `Data`: Contains SamplePosters, All Posters, and csv files with poster lists

* `Test Models`
  * `Deep Learning Final Project (Full Posters)`: CNN model using all poster data
  * `Deep Learning Final Project (Sample Posters)`: CNN model using sample poster data (subset)

## Motivation:

The motivation behind using movie posters to determine movie genres with deep learning is to develop an automated and efficient method for classifying movies into different genres. Movie posters are designed to convey information about the movie and attract an audience. One important piece of information that movie posters could possibly convey would be the style or genre of the movie. If we can see if a movie’s genre can be predicted by the movie’s poster, then using a movie poster as data may be helpful in other neural network processes like recommendation algorithms.

In addition, using movie posters for genre classification has practical applications in the movie industry, such as helping with marketing and advertising efforts. By accurately predicting the genre of a movie based on its poster, studios can better target their marketing campaigns and attract audiences who are interested in that genre. This is an application result since further research can be done to advise movie producers to use certain colors or patterns when creating posters. 

## Dataset:

The data set is from Kaggle, a platform for data science and machine learning competitions where companies or individuals can host challenges. The data set contains information on movie posters and their respective genres. Kaggle provides two files: an image data file and a movie CSV file. The posters themselves are high-quality images in JPEG format, with varying sizes and aspect ratios. The data set also includes a CSV file containing the image filenames marked with a movie ID and their corresponding genre labels. The original data set contains around 40,000 movie posters, each with corresponding genre labels. The data set is intended to be used for machine learning tasks, such as image classification or genre prediction based on movie posters.

The dataset includes the following features:

* imdbId: a numeric string representing the Id associated with the film pulled from the film website
* imdb Link: a URL to the associated film's IMDB page
* Title: the title of the movie and the year of its release
* IMDB Score: the audience rating from
* Genre: a string representing the genre(s) of the movie, with multiple genres separated by a pipe (|) symbol
* Poster_Path: a string representing the file path of the movie poster image

There are 28 unique movie genres in the original data set: Action, Adult, Adventure, Animation, Biography, Comedy, Crime, Documentary, Drama, Family, Fantasy, Film-Noir, Game-Show, History, Horror, Music, Musical, Mystery, News, Reality-TV, Romance, Sci-F, Short, Sport, Talk-Show, Thriller, War, Western.

The genre labels were assigned based on data available on IMDb and TMDb websites and may not accurately represent the actual genres of the movies. Additionally, some movie posters may contain multiple genres, while others may not have any genre information available. Each movie had between one to three different unique genres.

The dataset from Kaggle:
https://www.kaggle.com/datasets/neha1703/movie-genre-from-its-poster

## Related Work:

The article "Analysis of top box office film poster marketing schemes based on data mining and deep learning in the context of film marketing" discusses the use of data mining and deep learning techniques to analyze the effectiveness of film poster marketing strategies for top box office films. The authors collected data on the top 200 box office films from 2015-2019, including film posters, box office revenue, and critical ratings. They then used data mining and deep learning techniques to analyze the relationships between film poster features, such as color, font, and image content, and box office revenue and critical ratings. The article highlights the potential of data mining and deep learning techniques to provide insights into the effectiveness of film marketing strategies and inform decision-making in the film marketing industry.

The article is from the NIH:
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9879408/

## Technical Plan:

The inputs for the CNN model are the movie poster images, which are normalized to be the same dimensions. The outputs would be a multi classification where only genres whose softmax output is over a certain threshold are not zeroed out. Then, each genre who meets the threshold is given a value of 1 / (# of genres past threshold). This will allow our loss function to minimize loss. 

We could use a number of different ImageNet winning recognition: VGG, ResNet, AlexNet. ResNet performs the best in image recognition out of these while also being the most efficient. To observe the results of ResNet, we will be using both ResNet50 and ResNet18. In addition, a DenseNet model will be created to diversify our model group.

For the loss functions, we are using Binary Cross Entropy Loss with Logit transformation for multilabel classification. 

## Evaluation Plan:

We plan to run a CNN model with 5 - 10 epochs with three different models. With each model, we will observe accuracy and make changes to the model to increase accuracy. We plan on evaluating the machine learning algorithm through two main ways: accuracy and processing speed. We want a model that will provide the best result but also be able to get to that result in a reasonable time.

