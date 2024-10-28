# NeuroFocus

NeuroFocus is a concentration-enhancing game for children that uses SSVEP BCI brainwave technology. Brainwave signals are collected via the MAVE brainwave analysis machine and analyzed with Python to assess the user’s concentration level. The web interface is implemented using vanilla JavaScript, HTML, and CSS.

---

## Structure

### Frontend
#### Web: JavaScript, HTML, CSS

- **Pages**: Folder containing game screens. The flow progresses according to the numbered order at the end of each page’s file name.
  - **MainPage-1**: Main page.
  - **GamePage-2**: Game start page. Displays game images.
  - **WaitPage-3**: Relaxation page.
  - **PreAnalyisePage-4**: Pre-analysis page, shown before starting analysis.
  - **StimulusDesignPage-5**: Page where stimulus design is displayed, presenting the question.
  - **LoadingPage-6**: Loading page shown during brainwave analysis.
  - **ResultPage-7**: Results page where the selected image and correct answer are shown.
  - **Sound**: Page containing the alarm sound.

---

### Data Analysis
#### Implemented in Python

- **SignalProcessing.py**: Python script for analyzing actual brainwave data.

- **signalProcessing.exe**: Executable file that runs `SignalProcessing.py` to analyze brainwave data during gameplay. When executed, it waits for 75 seconds to collect enough data, then runs a calculation function to determine the frequency on which the user was focusing during that time. The identified frequency is saved in a text file as either "7Hz" or "13Hz," based on the results.
