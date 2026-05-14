"""Flask server for emotion detection."""

from flask import Flask, jsonify, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/')
def home():
    """
    Home endpoint.

    Returns:
        str: Status message.
    """
    return "Emotion Detection API is running!"


@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_api():
    """
    Emotion detector endpoint.

    Returns:
        str: Emotion analysis result.
    """

    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify(
            {"error": "Please provide 'text' in JSON body"}
        ), 400

    text_to_analyze = data['text']

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is "
        f"{result['dominant_emotion']}."
    )

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)