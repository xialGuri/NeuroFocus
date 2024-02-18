# NeuroFocus

This is a concentration-enhancing game for children using SSVEP BCI brainwave technology.
We received brainwave signals through the MAVE brainwave analysis machine.
The data received was analyzed using Python to assess the child's (user's) level of concentration.
Additionally, the web service was implemented using vanilla JS, CSS, and HTML.


# Structure
## Frontend
### Web: Javascript, HTML, CSS


* Pages: This is a folder containing game screens - the flow progresses in the order of the numbers at the end.

* MainPage-1: Main page.
* GamePage-2: Game start page. Images are displayed on this page.
* WaitPage-3: Relaxation page.
* PreAnalyisePage-4: Page before starting the analysis. 
* StimulusDesignPage-5: This is the page where the stimulus design is displayed. It's when the problem is presented.
* LoadingPage-6: This is the loading page that appears during brainwave analysis.
* ResultPage-7: This is the page where the selected picture is revealed and the correct answer is provided.
* sound: This is the page with the alarm sound.

## Data Analysis
### Implemented in Python.

* SignalProcessing.py: This is the Python code file for analyzing actual brainwave data.

* signalProcessing.exe: 
This is the executable file that runs SignalProcessing.py for analyzing brainwave data while the user progresses through the game. When the file is executed, it waits for sufficient data collection for 75 seconds. After that, a calculation function is executed to determine which frequency the user was focusing on during the last 75 seconds. The determined frequencies are then saved in a text file format. For example, if it determines that the user was focusing at 7Hz, it saves "7Hz" in the text file, and if it determines the user was focusing at 13Hz, it saves "13Hz" in the text file.
