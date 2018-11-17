# ArXiv_Classifier
Classify arXiv preprints by their meta-data

## supervised multiclass classification, NLP, imbalanced data 

ArXiv is an online repository of scientific pre-prints, see https://arxiv.org/help/general

Each paper comes with meta-data provided by one of the authors:
* **title**
* authors' names and forenames
* **abstract**
* one and only one **primary category** (*mathematics*, *physics*, *computer science* a.o., six in total)
* first subcategory (e.g. *math:AI*, *physics:astrophysics.GA*)
* none or a few further subcategories (possibly from other primary categories)

The main objective of the project is to predict the **primary category** of a paper given it's meta-data.
To that end we'll use **titles** and **abstracts** labeled by the **primary categories**.

The project naturally splits into few tasks:
* Harvest the data using the public API
* Explore and clean the data
* Build and test pipelines with shallow classifiers
...

