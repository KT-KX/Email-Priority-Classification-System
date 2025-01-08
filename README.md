# Email Priority Classification System

## Overview
This project implements a two-stage email filtering system that first identifies spam emails and then classifies non-spam emails by priority level. The system uses machine learning techniques to provide efficient email management.

## System Architecture

### Stage 1: Spam Classification
The first stage implements a spam filtering system using:
- CountVectorizer for text tokenization
- Naive Bayes Classifier for spam detection
- Binary classification (spam/not spam)

### Stage 2: Priority Classification
For emails that pass the spam filter, the system determines their priority through:
1. Text preprocessing:
   - Tokenization
   - Stop word removal
   - Punctuation and digit removal
   - Lemmatization
2. Feature engineering:
   - Weight calculation for important features
   - Priority threshold computation
3. Final classification:
   - Important
   - Not Important

## Implementation Flow

### Training Phase
1. **Spam Classifier Training:**
   - Input: Email training dataset
   - Process: Text to matrix conversion using CountVectorizer
   - Output: Trained spam classifier model

2. **Priority Classifier Training:**
   - Input: Clean email training dataset
   - Process: Complete text preprocessing pipeline
   - Output: Trained priority email model

### Testing Phase
1. **Spam Check:**
   - Input: New email
   - Process: CountVectorizer transformation
   - Output: Spam/Not Spam decision

2. **Priority Classification (for non-spam emails):**
   - Input: Email that passed spam filter
   - Process: Full preprocessing pipeline
   - Output: Important/Not Important classification

## Requirements
- Python 3.x
- scikit-learn
- NLTK
- NumPy
- Pandas

## Installation
```bash
git clone https://github.com/yourusername/email-priority-classifier
cd email-priority-classifier
pip install -r requirements.txt
```

## Usage
```python
# Example code for using the classifier
from email_classifier import SpamClassifier, PriorityClassifier

# Initialize classifiers
spam_classifier = SpamClassifier()
priority_classifier = PriorityClassifier()

# Process new email
email_text = "Your email content here"
if not spam_classifier.is_spam(email_text):
    priority = priority_classifier.get_priority(email_text)
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- Thanks to all contributors who helped in developing this email classification system
- Special thanks to the machine learning community for providing valuable resources and insights
