from google.cloud import language_v1
from googleapiclient import discovery
import json
from flask import current_app


class AnalyseDocument:
    def __init__(self, document) -> None:
        self.document = document

    def analyse_sentiment(self):
        client = language_v1.LanguageServiceClient()

        type_ = language_v1.Document.Type.PLAIN_TEXT
        language = "en"
        document = {"content": self.document, "type_": type_, "language": language}
        encoding_type = language_v1.EncodingType.UTF8

        response = client.analyze_sentiment(
            request={"document": document, "encoding_type": encoding_type}
        )

        return response

    def analyse_context(self):

        client = language_v1.LanguageServiceClient()
        type_ = language_v1.Document.Type.PLAIN_TEXT
        language = "en"
        document = {"content": self.document, "type_": type_, "language": language}
        content_categories_version = (
            language_v1.ClassificationModelOptions.V2Model.ContentCategoriesVersion.V2
        )

        response = client.classify_text(
            request={
                "document": document,
                "classification_model_options": {
                    "v2_model": {
                        "content_categories_version": content_categories_version
                    }
                },
            }
        )

        return response

    def analyse_toxicity(self):
        client = discovery.build(
            "commentanalyzer",
            "v1alpha1",
            developerKey=current_app.config["PERSPECTIVE_API_KEY"],
            discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
            static_discovery=False,
        )

        analyze_request = {
            "comment": {"text": self.document},
            "requestedAttributes": {"TOXICITY": {}},
        }
        response = client.comments().analyze(body=analyze_request).execute()

        res = {"value": 0, "type": "PROBABILITY"}
        if response["attributeScores"]["TOXICITY"]["summaryScore"]:
            res = response["attributeScores"]["TOXICITY"]["summaryScore"]

        return res
