# # Imports the Google Cloud client library
# from google.cloud import language_v1

# # Instantiates a client
# client = language_v1.LanguageServiceClient()

# # The text to analyze
# text = "Hello, world!"
text = "I'm only using HDMI1 because all my content is streamed and I have been using an Amazon Firestick, and Google Chromecast. The Chromecast is plugged into HDMI1, and the TV automatically switches to it when you want to use it. However, I don't think I'll be using the Chromecast much, because Fire TV is so good, and has an amazing remote control."
# document = language_v1.Document(
#     content=text, type_=language_v1.Document.Type.PLAIN_TEXT
# )

# # Detects the sentiment of the text
# sentiment = client.analyze_sentiment(
#     request={"document": document}
# ).document_sentiment
# print(sentiment)

# # sentiment = client.annotate_text(request={"document": document})
# # sentiment = client.classify_text(request={"document": document})
# # sentiment = client.
# print("Text: {}".format(text))
# print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

from google.cloud import language_v1


def sample_classify_text(text_content):
    """
    Classifying Content in a String

    Args:
      text_content The text content to analyze.
    """

    client = language_v1.LanguageServiceClient()

    # text_content = "That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows."

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    content_categories_version = (
        language_v1.ClassificationModelOptions.V2Model.ContentCategoriesVersion.V2
    )
    response = client.classify_text(
        request={
            "document": document,
            "classification_model_options": {
                "v2_model": {"content_categories_version": content_categories_version}
            },
        }
    )
    # Loop through classified categories returned from the API
    for category in response.categories:
        # Get the name of the category representing the document.
        # See the predefined taxonomy of categories:
        # https://cloud.google.com/natural-language/docs/categories
        print("Category name: {}".format(category.name))
        # Get the confidence. Number representing how certain the classifier
        # is that this category represents the provided text.
        print("Confidence: {}".format(category.confidence))


sample_classify_text(text)


class AnalyseDocument:
    def __init__(self, document) -> None:
        self.document = document

    def analyse_sentiment(self):
        client = language_v1.LanguageServiceClient()

        # text_content = 'I am so happy and joyful.'

        # Available types: PLAIN_TEXT, HTML
        type_ = language_v1.Document.Type.PLAIN_TEXT

        # Optional. If not specified, the language is automatically detected.
        # For list of supported languages:
        # https://cloud.google.com/natural-language/docs/languages
        language = "en"
        document = {"content": self.document, "type_": type_, "language": language}

        # Available values: NONE, UTF8, UTF16, UTF32
        encoding_type = language_v1.EncodingType.UTF8

        response = client.analyze_sentiment(
            request={"document": document, "encoding_type": encoding_type}
        )
        # Get overall sentiment of the input document
        print("Document sentiment score: {}".format(response.document_sentiment.score))
        print(
            "Document sentiment magnitude: {}".format(
                response.document_sentiment.magnitude
            )
        )
        # Get sentiment for all sentences in the document
        for sentence in response.sentences:
            print("Sentence text: {}".format(sentence.text.content))
            print("Sentence sentiment score: {}".format(sentence.sentiment.score))
            print(
                "Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude)
            )

        # Get the language of the text, which will be the same as
        # the language specified in the request or, if not specified,
        # the automatically-detected language.
        print("Language of the text: {}".format(response.language))
        return response
