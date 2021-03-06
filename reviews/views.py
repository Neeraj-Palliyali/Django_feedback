from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review
# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    # context_object_name="forms"

class ThankYouView(TemplateView):
    template_name = "reviews/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"]="Works properly"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name="reviews"

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"

    model = Review

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context



class AddFavoriteView(View):
    def post(self, request):
        
        review_id = request.POST["review_id"]
        print(review_id)
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect(review_id)

