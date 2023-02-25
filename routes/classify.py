from flask import Blueprint, current_app, request


# Create Flask blueprint
bp_classify = Blueprint('classify', __name__)

# Route for classifying text
@bp_classify.route('/text', methods=['POST'])
def classify_text():
    # Get classifier from app config
    classifier = current_app.config['MODEL']

    # Get text from request body
    try:
        text = request.json['text']
    except KeyError:
        return {
            'error': 'Missing text in request body'
        }, 400
    
    # Classify text
    return {
        'result': classifier.classify(text)
    }, 200
