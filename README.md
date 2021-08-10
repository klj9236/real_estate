Real estate

Setup

Repo Setup

Use the GitHub.com online interface to create a new remote project repository called something like "real_estate". When prompted by the GitHub.com online interface, add a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub.com at an address like https://github.com/YOUR_USERNAME/real_estate.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

``cd ~/Desktop/real_estate

Use your text editor or the command-line to create a new sub-directory called "app" with a file called "real_estate.py", and then place inside some example print statements like the following:

this is the "app/real_estate.py" file

print("-------------------------") print("SELECTED SYMBOL: XYZ") print("-------------------------") print("REQUESTING STOCK MARKET DATA...") print("REQUEST AT: 2018-02-20 02:00pm") print("-------------------------") print("LATEST DAY: 2018-02-20") print("LATEST CLOSE: $100,000.00") print("RECENT HIGH: $101,000.00") print("RECENT LOW: $99,000.00") print("-------------------------") print("RECOMMENDATION: BUY!") print("RECOMMENDATION REASON: TODO") print("-------------------------") print("HAPPY INVESTING!") print("-------------------------") Make sure to save Python files like this whenever you're done editing them. After setting up a virtual environment, we will be ready to run this file.

Use your text editor or the command-line to create a new file called "requirements.txt" in the root directory of your repository, and then place inside the following contents:

this is the "requirements.txt" file

it might be helpful to use pandas. if you do, uncomment the last line below ...

requests python-dotenv

pandas

After setting up a virtual environment, we will be ready to install these packages.

Environment Setup

Create and activate a new Anaconda virtual environment:

conda create -n realestate-env python=3.8 # (first time only) conda activate realestate-env From within the virtual environment, install the required packages specified in the "requirements.txt" file you created:

pip install -r requirements.txt From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

``python app/real_estate.py Basic Requirements

Repository Requirements

Your project repository should contain an "app" directory with a "robo_advisor.py" file inside (i.e. "app/robo_advisor.py").

Your project repository should contain a "README.md" file. The README file should provide instructions to help someone else install, setup, and run your program. This includes instructions for installing package dependencies, for example using Pip. It also includes instructions for setting an environment variable named ALPHAVANTAGE_API_KEY (see "Security Requirements" section below).

Your project repository should contain a file called ".gitignore" which prevents the ".env" file and its secret credentials from being tracked in version control. The ".gitignore" file generated during the GitHub repo creation process should already do this, otherwise you can create your own ".gitignore" file and place inside the following contents:

this is the ".gitignore" file

ignore secret environment variable values in the ".env" file:

.env Finally, your project repository should contain a "data" directory with another ".gitignore" file inside. In the "data/.gitignore", place inside the following contents to track the empty directory (thus allowing CSV files to be written there without error), while ignoring the CSV files themselves:

this is the "data/.gitignore" file

ignore all files in this "data" directory:

except this ".gitignore" file:

!.gitignore Security Requirements

Your program will need an API Key to issue requests to the US Real Estate API. But the program's source code should absolutely not include the secret API Key value. Instead, you should set an environment variable called USREALESTATE_API_KEY, and your program should read the API Key from this environment variable at run-time.

You are encouraged to use a "dotenv" approach to setting project-specific environment variables by using a file called ".env" in conjunction with the dotenv package. Example ".env" contents:

this is the ".env" file

USREALESTATE_API_KEY="abc123"

The ".env" file should absolutely not be tracked in version control or included in your GitHub repository. Use a local ".gitignore" file for this purpose.

API Requirments 

Vist https://rapidapi.com/datascraper/api/us-real-estate/ and set up an account to gain API access. 
Choose Get/sold-homes and copy and paste sample code into real_estate.py file. 

Convert String into DataFrames

