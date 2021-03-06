# ArXiv_Classifier
Classify arXiv preprints by their meta-data

## supervised multiclass classification, NLP, imbalanced data 

ArXiv is an online repository of scientific pre-prints, see https://arxiv.org/help/general

Each paper comes with meta-data provided by one of the authors:
* **title**
* authors' names and forenames
* **abstract**
* one and only one **primary category** that can be mapped into one of six **classes**: *mathematics*, *physics*, *computer science*, *statistics*, *quantitative biology*, *quantitative-finance* [^1]
* few (possibly none) secondary categories (with the same mapping as for the primary category)

The main objective of the project is to predict the **class** associated with primary category of a paper given it's **title** and **abstracts** (since with using authors' names the problem becomes uninteresting).

As a measure of success I choose the **macro f1 score**. I care both about *precision* and *recall*, and I like all my classes equally (regardless of imbalances in data).

### The project naturally splits into few tasks that correspond to standalone Jupyter notebooks:
desc | link | remarks 
--- | --- | ---
Harvest the data using the public API | [arXiv_metadata_harvester.ipynb](https://github.com/olszewskip/ArXiv_Classifier/blob/master/arXiv_metadata_harvester.ipynb)| There are 2 public APIs
Tidy up, have a closer look, strip down to chosen features | [arXiv_cleanup.ipynb](https://github.com/olszewskip/ArXiv_Classifier/blob/master/arXiv_cleanup.ipynb)| Large imbalance, mostly single-class
Build and test pipelines with shallow classifiers | [shallow/arXiv_shallow_clf.ipynb](https://github.com/olszewskip/ArXiv_Classifier/blob/master/shallow/arXiv_shallow_clf.ipynb)| Handle LaTeX expression using Regex with custom feature transformer. Grid search through classifiers. Reached 80% macF1
Preprocess data for deep learning | [keras_preprocessing.ipynb](https://github.com/olszewskip/ArXiv_Classifier/blob/master/keras_preprocessing.ipynb)| Text -> fixed-len (zero-padded) sequence of ints
Compare loss-functions/batch-sizes/optimizers and pretrain word-embeddings | [keras_GlobalAvg_GridSearch.ipynb](https://github.com/olszewskip/ArXiv_Classifier/blob/master/keras_GlobalAvg_GridSearch.ipynb) | Simple net reproduces the 80% on validation. Custom loss functions are helpful. Custom metric functions are informative.
Examine a couple of neural-net architectures | [keras_RNN_LSTM.ipynb](https://github.com/olszewskip/ArXiv_Classifier/blob/master/keras_RNN_LSTM.ipynb) | Neural nets generically do worse than 80%
Get final score of neural-nets on test-data | [keras_evaluate.ipynb](https://github.com/olszewskip/ArXiv_Classifier/blob/master/keras_evaluate.ipynb) | **The winner climbed to 81% macF1**, it uses GlobalAveragePooling and a custom loss function

Models in the last three notebooks were fit using **Colab** (link to the google-directory: [ArXiv_Classifier](https://drive.google.com/open?id=1Z-NeXJ0D4t0FB9i5yPY_KyvA8m60JeWR)).

Final conclusion of the project is that the data makes it relatively easy to obtain more than ~75% macro-F1, and hard to go beyond 80%.

Beyond that, the dataset, being reasonably *big* and challenging, offers a practically endless TODO list, eg.
* examine topics modelled with LDA
* examine more neural-net architectures
* train fancier word-embeddings using gensim
* implement own CBOW and/or skipdram in keras and compare
* seperate titles and abstracts into seperate channels of a neural net
* implement real-life data-streaming, processing and learning (also: use generators for fitting in keras)
* train a network to generate new abstract given the title
...

[^1] Since 2017 there are two other classes of articles. They get harvested but I remove them from testing and training.
