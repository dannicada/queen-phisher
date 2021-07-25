from django.urls import path

from .views import (
    PredictPhishingUrl
)

api_urlpatterns = [
    path(
        'predict_phishing/',
        PredictPhishingUrl.as_view(),
        name='predict-phishing',
    ),
    # path(
    #     'model_score/',
    #     GetScoreView.as_view(),
    #     name='model-score',
    # ),
    # path(
    #     'add_tweet/',
    #     AddReviewedTweetManuallyView.as_view(),
    #     name='add-tweet',
    # ),
]
