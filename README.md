# HawkHacks22-AssemblyAI
This is a node module (not yet an npm package) to get speech-to-text transcriptions using AssemblyAI API.
# How to use
### What you will need
Python3 installed on your system
### Clone/Download the repository
Type the following command on your terminal
```bash
git clone https://github.com/Saksham-Gupta-30/HawkHacks22-AssemblyAI.git
```
### Get your API_KEY from AssemblyAI.com after SignUp And edit the app . py
```python
API_KEY = 'Enter Your API_KEY'
```
### Add your Audio File via URL or via File Path
To add your file using URL, comment the following part in app. py
```python
media_file_path = 'Path of your audio file'
response_upload = ai1.upload_audio_by_file(media_file_path)
response_json_output = response_upload.json()
transcript_id = response_json_output['id']
```
To add your file using File Path comment the following the following part in app. py
```python
media_url = 'Add your url(starts with https)'
response_upload_by_url = ai1.upload_audio_by_url(media_url)
transcript_id = response_upload_by_url.json()['id']
```
#### Run the app python file as a python script and wait for a while. If output states Queued or Processing, run the print command at last again.
