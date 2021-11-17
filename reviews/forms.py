from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "You Rating"
        }

        error_messages = {
            "user_name": {
                "required": "Your must not be empty",
                "max_length": "Please enter a shorter name!"
            }
        }
