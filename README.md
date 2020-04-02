Dear Students,

The notebooks in the Lecture directory will contain my part of the Machine Learning course. I have done my best to annotate them and make them selfcontained. However I was not prepared for the neccesity of essentially writing a textbook on Machine Learning. So I am counting on your understanding of the situation. 

The notebooks assume some basic understanding of probability and statistics, but that anyway were the prerequisites for the course. The notebooks contain python code without much explanation. It's up to you to look up the documentation of the library functions that I have used. 

To run the notebooks you need a Python environment. I strongly suggest you use `conda`. 

First install [anaconda](https://www.anaconda.com/distribution/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html). Please install python 3.6 or higher. 

Then create a new _virtual environment_ for your projects e.g.
```
conda -n machinelearning python=3.7
```
This will create a virtual environment named `machinelearning`. 

To activate the environment you type:
```
conda activate machinelearning 
```


In case of Anaconda distribution most of the needed packages will be preinstalled. In case of miniconda you have to install them yourself using `conda install`. 

Here is a hopefully complete list of packages you will need for the start:

```
conda install notebook  jupyter jupyterlab
conda install numpy scipy 
conda install matplotlib
conda install pandas
conda install scikit-learn
```
 
Then you can type
```
jupyter lab 
```
to open jupyter notebook  and start working :)

To close environment you type 
```
conda deactivate
```
 
This repository will grow with time and I suggest you clone it and update regularly. There maybe however a problem when updating repository. Any changes you make to the notebooks and that includes just running them will  result most probably in merge conflicts hard to resolve. To solve this you can clone  agian the repository to another location or copy the notebooks you are working on and give them some  other name like my_notebook.ipynb. 
 
 
Hope this helps. 







