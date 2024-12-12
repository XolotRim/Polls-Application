# Polls-Application
My first Django Application. I followed the [Django Tutorial](https://docs.djangoproject.com/en/5.1/intro/) from the Django Docs.
The project mysite contains the app 'polls'.The app contains:
- 'Question' and 'Choice' Models
- 'IndexView' to list down the latest questions.
- 'DetailView' to show the detail of a particular question and lets you vote for a particular option.
- 'ResultsView' to show the results of the questions' polls so far.

The templates uses HTMX as it lets you build webpages with "expected" functionalities without using js libraries.

The project contains dynamic urls to let you maneuver through different questions and their reults dynamically.

The project contains multiple tests for rigorous testing of the app functionalities.

The admin site is also customized to show relevant details and functionalites corresponding to different models.