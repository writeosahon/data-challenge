## REPO  DESCRIPTION
This repo contains a simple data challenge. Objectives of the challenge are:

 - Pull daily gas prices data from the specified remote location.
 - The pulled data should be formatted/saved in .csv data file
 - The csv file should contain 2 columns - date and gas prices

## Summary of Available Features

 - Script pulls the **daily** gas prices data from the provided (default) url.
 - The gas prices data is formatted and stored as CSV (using the specified 2-columns format)
 - Script is interactive, so user can change the default url. *NOTE: If new url is provide, then the format and type of the 'pulled' data MUST be identical to that of the default url*
 - The pulled data (in excel format) can be sorted by 'DATE' (in ascending or descending order) before it stored in csv
 - A visualisation (Time-Series graph) of the newly created csv data can be  generated for users to view on their default browser

## *PROJECT ENVIRONMENT*
 - Python 3.7.6
 - Conda Virtual Environment (or any other python virtual environment user prefers)

## *PACKAGE DEPENDENCIES*
The script depends on the following python packages:
 - requests (for pulling data from remote location)
 - panda (for reading, formatting, sorting and saving the pulled data)
 - plotly (for generating graph visualisation when requested by user)

All  packages can be installed in the created virtual environment using:

    pip install [package-name]

## *RUNNING THE SCRIPT*

 - clone this repository `git clone https://github.com/writeosahon/data-challenge.git`
 - create the python virtual environment and activate it
 - change directory into the location of the cloned repository
 - run `python main-script.py`
 - Enjoy!! :-)

