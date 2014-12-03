from main import app
from flask import render_template, request
from config import FREEZER_BASE_URL


@app.route('/')
def index():
    page_title = "Timeline: A Year Of 'Systemic Failure' At DCF"
    page_url = FREEZER_BASE_URL.rstrip('/') + request.path

    social = {
        'title': "Timeline: A Year Of 'Systemic Failure' At DCF",
        'subtitle': "This year has brought a series of tragedies and revelations about problems at Vermont's Department for Children and Families. VPR looks back over the months.",
        'img': "http://www.vpr.net/apps/timeline-dcf-systemic-failure/static/img/timeline-social-snap.png",
        'description': "This year has brought a series of tragedies and revelations about problems at Vermont's Department for Children and Families. VPR looks back over the months.",
        'twitter_text': "Timeline: A Year Of 'Systemic Failure' At DCF",
        'creator': "Taylor Dobbs and Angela Evancie",
        'twitter_hashtag': "VT"
    }

    return render_template('content.html',
        page_title=page_title,
        page_url=page_url,
        social=social)
