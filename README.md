# ArXiv_Classifier
Classify arXiv preprints by their meta-data

## supervised multiclass classification, NLP, imbalanced data 

ArXiv is an online repository of scientific pre-prints, see https://arxiv.org/help/general

Each paper comes with meta-data provided by one of the authors:
* **title**
* authors' names and forenames
* **abstract**
* one and only one **primary category** that can ba mapped into one of six classes: *mathematics*, *physics*, *computer science*, *statistics*, *quantitative biology*, *quantitative-finance* [^1]
* few (possibly none) secondary categories (with the same mapping for the primary category)

The main objective of the project is to predict the **primary category** of a paper given it's **title** and **abstracts** (since with using authors' names the problem becomes uninteresting).

As a measure of success I choose the **macro f1 score**. I care both about *precision* and *recall*, and I like all my classes equally (regardless of imbalances in data).

The project naturally splits into few tasks that co:
* Harvest the data using the public API
* Tidy up, have a closer look at the data, strip it down to the chosen features
* Build and test pipelines with shallow classifiers
* Have fun with keras
...

[^1] Since 2017 there are two other classes of articles. They get harvested but I remove them from testing and training.
