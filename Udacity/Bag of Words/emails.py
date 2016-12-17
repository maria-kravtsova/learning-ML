from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

email1 = "Hello Mariia, thank you for purchasing your new Nexus 5."
email2 = "Dear Mariia, please enjoy your free offer of Project Fi on your Nexus 5."
email3 = "Thank you for being a loyal customer of nexus and Project Fi."

emails = [email1, email2, email3]

bag_of_words = vectorizer.fit(emails)
bag_of_words = vectorizer.transform(emails)
print bag_of_words
print vectorizer.vocabulary_.get("nexus")
