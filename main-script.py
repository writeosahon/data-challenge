""" THIS IS THE MAIN SCRIPT FOR THE DATA CHALLENGE.
Script pulls data from the specified remote  location and creates a CSV file """

__version__ = '0.0.1 (2020-01-27)'
__author__ = 'OSAHON OKUNGBOWA'

import requests # pip install requests
import pandas # pip install pandas
import plotly # pip install plotly
import plotly.io as pio # pip install plotly 
import plotly.graph_objects as plotlygraph # pip install plotly

import datetime
import os
import sys

# VARIABLES/ATTRIBUTES
downloadURL = "https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls" # holds the cuurent download url


# define function used to download the data to be coverted to CSV
def downloadGasPricesData() -> str :
    """ Function downloads the gas prices data. 
    The function retunrns the filepath for the downloaded data OR 
    raises an exception if something goes wrong """

    global downloadURL # define module attribute as global so this function can update if needed
    # track if user wants to change the default download url
    changeDownloadURL = input("""The current URL for gas prices download is """ + 
                            f"""'{downloadURL}' . \n""" + 
                            """Do you wish to use a differnt URL? \n""" + 
                            """Enter 'Y' or 'N' for yes or no \u27A4   """)

    # check if user wants to change the download url
    if changeDownloadURL.upper().startswith("Y"): # user wants to change the download url
        downloadURL = input("""Enter the new gas price download url  \u27A4   """)
    elif changeDownloadURL.upper().startswith("N"): # user does not want to change the download url
        downloadURL = downloadURL # set the download url to whatever was being used previously
    else: # invalid input. so use what was set previously
        print("Invalid input. so using value set previously...")
        downloadURL = downloadURL # set the download url to whatever was being used previously

    # begin download from the provided 'downloadURL
    print("Downloading gas prices data file to location 'tempdownload'......")
    
    # create the directory for storing the downloaded data. This can be changed to a temp dir
    try:
        os.mkdir("tempdownload")
    except FileExistsError:
        # do nothing
        pass

    # download the data file
    response = requests.get(downloadURL)
    tempfilePath = 'tempdownload/{year}-{month:02}-{day:02}-gasprice.xls'.\
        format(year=datetime.date.today().year,
               month=datetime.date.today().month,
               day=datetime.date.today().day)
    
    with open(tempfilePath, 'wb') as tempfile: 
        tempfile.write(response.content)
        print(f"Downloaded gas prices data file to location '{tempfilePath}'")

    return tempfilePath  # return the filepath for the just created object 

def convertDataToCSV(gasPriceDataFilePath : str):
    """ Function converts to the downloaded gas prices data to specified CSV data format """
    
    #read the excel data into panda dataframes
    print("converting Excel Data to CSV...")
    dataFrame = pandas.read_excel(gasPriceDataFilePath, sheet_name=1, skiprows=3, header=None)
    
    # ask the user if they want the data sorted. (CURRENTLY ONLY SORTING BY DATE)
    changeSortOrder = input("""Do you wish to sort the data 'DATE' column in Ascending or Descending order?\n""" +  
                            """Enter 'A' or 'D' for 'Ascending' or 'Descending' order \u27A4   """)

    if changeSortOrder.upper().startswith("A"): # user wants to sort in ascending order
        dataFrame.sort_values(by=0, axis=0, ascending=True, inplace=True)
    elif changeSortOrder.upper().startswith("D"): # user wants to sort in descending order
        dataFrame.sort_values(by=0, axis=0, ascending=False, inplace=True) 
    else: # invalid input, so sort in ascending
        print("INVALID INPUT, SO SORTING IN ASCENDING ORDER")
        dataFrame.sort_values(by=0, axis=0, ascending=True, inplace=True)

    # save the sorted dataframe
    print("Sorting and Saving Data in csv....")
    # create the full filepath for the CSV data file
    csvFilePath = '{year}-{month:02}-{day:02}-daily-gas-price.csv'.\
        format(year=datetime.date.today().year,
               month=datetime.date.today().month,
               day=datetime.date.today().day)

    dataFrame.to_csv(csvFilePath, index=False, header=["DATE", "GAS PRICE"])
    print(f"CSV data file for daily gas price saved to location '{csvFilePath}' ")

def plotGraph():
    """ Function is used to plot a time series graph based on the downloaded CSV data """

    # set the default rendering engine for plotly graphs
    pio.renderers.default = "browser"
    # create a time series graph using the created csv data file
    dataFrame = pandas.read_csv('2020-01-27-daily-gas-price.csv')

    fig = plotlygraph.Figure([plotlygraph.Scatter(x=dataFrame['DATE'], y=dataFrame['GAS PRICE'])])
    fig.update_layout(
    title="Gas Price",
    xaxis_title="DATE",
    yaxis_title="GAS PRICES")
    
    fig.show()


if __name__ == "__main__": # this is the main module being executed

    # print application title for user
    programHeading = "\nDATA CHALLENGE"
    print(programHeading)
    print('=' * len(programHeading))
    programHeading = "CONVERTING DAILY GAS PRICES FROM EXCEL TO CSV"
    print(programHeading)
    print('=' * len(programHeading))

    
    # call the function used to download/pull data
    try:
        tempGasPricesFilePath = downloadGasPricesData()
    except KeyboardInterrupt as keyinterrupt:
        print("\nUSER EXITED APPLICATION")    
        sys.exit(0) # exit the application gracefully

    except Exception as e:
        print("SORRY AN ERROR OCCURED WHILE TRYING TO DOWNLOAD DAILY GAS PRICES")
        sys.exit(0) # exit the application gracefully

    # call the function to convert downloaded data to CSV
    try:
        convertDataToCSV(tempGasPricesFilePath)
    except KeyboardInterrupt as keyinterrupt:
        print("\nUSER EXITED APPLICATION")        
        sys.exit(0) # exit the application gracefully
    except Exception as e:
        print("SORRY AN ERROR OCCURED WHILE CONVERTING DATA TO CSV")
        sys.exit(0) # exit the application gracefully
    
    # plot Graph
    plotGraph()


    
    

