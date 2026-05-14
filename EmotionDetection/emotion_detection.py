import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, headers=headers, json=input_json)
    response.raise_for_status()
    
    response_json = response.json()
    
    # The API returns a 'text' attribute as a JSON string, convert it to dict
    emotion_data = json.loads(response_json.get('text', '{}'))
    
    # Extract emotions with scores
    emotions = {
        'anger': emotion_data.get('anger', 0),
        'disgust': emotion_data.get('disgust', 0),
        'fear': emotion_data.get('fear', 0),
        'joy': emotion_data.get('joy', 0),
        'sadness': emotion_data.get('sadness', 0)
    }
    
    # Find dominant emotion (highest score)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Prepare output dictionary
    output = emotions.copy()
    output['dominant_emotion'] = dominant_emotion
    
    return output