# Machine Learning

This repository contains the materials for my part of the "Machine Learning" course.

## Content

### Lecture

The lectures are provided in the Lecture directory in form of the jupyter notebooks. I have done my best to annotate them and make them selfcontained. However I was not prepared for the neccesity of essentially writing a textbook on Machine Learning. So I am counting on your understanding of the situation. 

The notebooks assume some basic understanding of probability and statistics, but that anyway were the prerequisites for the course. The notebooks contain python code without much explanation. It's up to you to look up the documentation of the library functions that I have used. 

### Data

The Data directory contains the data used in the examples throughout the lectures. Only relatively small datasets are included. You will be encouraged the download bigger datasets via links in the notebooks. 

### Classes

This directory  contains the problems you will be required to solve. Those will be also presented in form of the notebooks. 

## Running the notebooks

To run the notebooks you need a Python environment. I strongly suggest you use `conda` for managing this. 

First install [anaconda](https://www.anaconda.com/distribution/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html). Please install python 3.6 or higher. 

Then create a new _virtual environment_ for your projects e.g.
```
conda create -n machinelearning python=3.7
```
This will create a virtual environment named `machinelearning`. 

To activate the environment you type:
```
conda activate machinelearning 
```

In case of Anaconda distribution most of the needed packages will be preinstalled. In case of miniconda you have to install them yourself using `conda install`. 
After activating your environment you can install packages using the command below

```
conda install notebook  jupyter jupyterlab numpy scipy matplotlib  pandas scikit-learn
```
You can of course install packages one by one if you prefer. 


Then you can type
```
jupyter lab 
```
or
```
jupyter notebook
```
to open jupyter lab/notebook  and start working :)

To close environment you type 
```
conda deactivate
```
 
## Version control

This repository will grow with time and I suggest you clone it and update regularly. There maybe however a problem when updating (pulling) repository. Any changes you make to the notebooks, and that includes just running them, will most probably   result in hard to resolve merge conflicts. To solve this you can clone  again the repository to another location or copy the notebooks you are working on and work on your copy.  
 
## Reporting issues

If you find my explanations inadequate or find errors in code or description please do not hesistate to contact me! You can do this via email or by Teams channel that I have setup for this purpose. 
 
Hope this helps. 








