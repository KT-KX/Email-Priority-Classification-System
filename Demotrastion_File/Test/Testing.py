import pickle
import pandas as pd

with open('spam_classifier_model.pkl', 'rb') as file:
    model1 = pickle.load(file)


with open('count_vectorizer.pkl', 'rb') as file:
    count = pickle.load(file)

def checkSpam(df):
    if df.empty or 'email_text' not in df.columns:
        raise ValueError("DataFrame is empty or does not contain 'email_text' column.")
    
    email_text = df.iloc[0]['email_text']
    email_vector = count.transform([email_text])
    prediction = model1.predict(email_vector.toarray())
    return prediction[0] == 1  
data = {
    'email_text': [
        "Subject: urgent we have meeting right now!"
    ]
}
df = pd.DataFrame(data)


is_spam = checkSpam(df)
print(is_spam)  
