# ArXiv_Classifier
Classify arXiv preprints by their meta-data

## supervised multiclass classification, NLP, imbalanced data 

ArXiv is an online repository of scientific pre-prints, see https://arxiv.org/help/general

Each paper comes with meta-data provided by one of the authors:
* **title**
* authors' names and forenames
* **abstract**
* one and only one **primary category** that can ba mapped into one of six classes: *mathematics*, *physics*, *computer science*, *statistics*, *quantitative biology*, *quantitative-finance* [^1]
* few (possibly none) secondary categories (with the same mapping as for the primary category)

The main objective of the project is to predict the **primary category** of a paper given it's **title** and **abstracts** (since with using authors' names the problem becomes uninteresting).

As a measure of success I choose the **macro f1 score**. I care both about *precision* and *recall*, and I like all my classes equally (regardless of imbalances in data).

### The project naturally splits into few tasks that correspond to standalone Jupyter notebooks:
desc | link | remarks 
--- | --- | ---
Harvest the data using the public API | [arXiv_metadata_harvester.ipynb](https://github.com/olszewskip/ArXiv_Classifier/blob/master/arXiv_metadata_harvester.ipynb)| there are 2 public APIs
Tidy up, have a closer look, strip down to chosen features | [arXiv_cleanup.ipynb](https://github.com/olszewskip/ArXiv_Classifier/blob/master/arXiv_cleanup.ipynb)| Large imbalance, mostly single-class
Build and test pipelines with shallow classifiers | [shallow/arXiv_shallow_clf.ipynb](https://github.com/olszewskip/ArXiv_Classifier/blob/master/shallow/arXiv_shallow_clf.ipynb)| reached 80% mF1
Preprocess data for deep learning | [keras_preprocessing.ipynb](https://github.com/olszewskip/ArXiv_Classifier/blob/master/keras_preprocessing.ipynb)| text -> fixed-len sequence of ints
Pretrain word-embeddings | [keras_simple_embeddings_50dim.ipynb](https://github.com/olszewskip/ArXiv_Classifier/blob/master/keras_simple_embeddings_50dim.ipynb) | custom loss functions are helpful
Test few neural-net architectures | []() | 

Beyond that, the dataset, being reasonably *big* and challenging, offers a practically endless TODO list, eg.
* examine topics modelled with LDA
* train fancier word-embeddings using gensim
* implement own CBOW and/or skipdram in keras and compare
* seperate titles and abstracts into seperate channels of a neural net
* implement real-life data-streaming, processing and learning
* train a network to generate new abstract given the title
...

[^1] Since 2017 there are two other classes of articles. They get harvested but I remove them from testing and training.
