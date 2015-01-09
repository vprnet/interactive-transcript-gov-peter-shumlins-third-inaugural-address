from main import app
from flask import render_template, request
from config import FREEZER_BASE_URL


@app.route('/')
def index():
    page_title = "Interactive Audio Transcript: Gov. Peter Shumlin's Third Inaugural Address"
    page_url = FREEZER_BASE_URL.rstrip('/') + request.path

    social = {
        'title': "Timeline: A Year Of 'Systemic Failure' At DCF",
        'subtitle': "Gov. Peter Shumlin's third inaugural address focused on renewable energy and water quality issues.",
        'img': "http://mediad.publicbroadcasting.net/p/vpr/files/201501/shumlin-inaugural-vpr-evancie-20150108.jpg",
        'description': "Gov. Peter Shumlin's third inaugural address focused on renewable energy and water quality issues.",
        'twitter_text': "Interactive Transcript: @GovPeterShumlin's third inaugural address",
        'creator': "Averbach Transcription",
        'twitter_hashtag': "vtpoli"
    }

    return render_template('content.html',
        page_title=page_title,
        page_url=page_url,
        social=social)
