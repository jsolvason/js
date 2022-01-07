# Description

This repo is intended for rotation students to accelerate their research

# Installation

To install these scripts I suggest doing the following:

1. Create folder in home directory called pybin. Open terminal then type 

    ```mkdir ~/pybin```

2. Clone this github repo into pybin. 
    
    ```cd pybin``` 
    
    ```git clone https://github.com/jsolvason/js```
    
3. Go back to your home directory 

    ```cd ~```

4. Find your bash profile (The profile will be called ```.bash_profile```,```.bashrc```, or ```.zshrc```).

    ```ls -a ~``` 

5. Open your bash profile with the terminal word processor (this assumes its named ```.zshrc```) 

    ```nano ~./zshrc```

6. Add the following line to your bash profile 

    ```export PYTHONPATH=~/pybin/js:~/pybin/:$PYTHONPATH```


7. Test this works by creating a new terminal window and typing the follwoing. If this does not return an error message, then it works!

    ```python```

    ```import js``` 
    
8. You will also need to install the python library ```Biopython``` to your conda environment to use some of my scripts. Activate the conda environment you will use ```js``` in and install the following conda package https://anaconda.org/anaconda/biopython

