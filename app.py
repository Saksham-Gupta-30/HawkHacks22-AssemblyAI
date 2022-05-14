from rich import print
from assembly import AssemblyAI

API_KEY = '<Enter your API_KEY>'

ai1 = AssemblyAI(API_KEY)

# # Example 1.1 Uplaod Media File (By URL)
# media_url = 'https://drive.google.com/file/d/1ewRY75Alp_ddCaVnTznc8uwUkKJERwJ1/view?usp=sharing'
# response_upload_by_url = ai1.upload_audio_by_url(media_url)
# transcript_id = response_upload_by_url.json()['id']


# # Exampel 1.2 Upload Media File (With A Local File)
media_file_path = './thunder.mp3'
response_upload = ai1.upload_audio_by_file(media_file_path)
response_json_output = response_upload.json()
transcript_id = response_json_output['id']


# Step 2. Retrieve Job Status
response_status = ai1.retrieve_transcript(transcript_id)
print(response_status)
print(response_status['status'])
print(response_status['text'])
