import speech_recognition as sr 


sample_rate = 48000
 

sr_Obj = sr.Recognizer()   #Initialize the recognizer

def get_text_from_speech():
	with sr.Microphone(sample_rate = sample_rate) as source:

	    sr_Obj.adjust_for_ambient_noise(source)  # adjusting to ambient noise levels
	    
	    print("Listening...")
	    audio = sr_Obj.listen(source)   # getting the audio input 
	        
	    try: 
	        text = sr_Obj.recognize_google(audio)  # speech to text conversion
	        return text
	    
	    except sr.UnknownValueError: 
	        return "Audio not understandable."

