import pytest
from datetime import datetime, timedelta
from app.helpers import pretty_date

def test_just_now():
	now = datetime.utcnow()
	assert pretty_date(now) == 'just now'

def test_yesterday():
	assert (pretty_date(datetime.utcnow()-timedelta(days=1))) == 'Yesterday'

def test_seconds_ago():
	assert (pretty_date(datetime.utcnow()-timedelta(seconds=50))) == '50 seconds ago'

def test_one_minute():
	assert (pretty_date(datetime.utcnow()-timedelta(minutes=1))) == 'a minute ago'

def test_minutes_ago():
	assert (pretty_date(datetime.utcnow()-timedelta(minutes=40))) == '40 minutes ago'

def test_one_hour():
	assert (pretty_date(datetime.utcnow()-timedelta(hours=1))) == 'an hour ago'

def test_hours_ago():
	assert (pretty_date(datetime.utcnow()-timedelta(hours=10))) == '10 hours ago'
	
def test_days_ago():
	assert (pretty_date(datetime.utcnow()-timedelta(days=2))) == '2 days ago'

def test_weeks_ago():
	assert (pretty_date(datetime.utcnow()-timedelta(weeks=2))) =='2 weeks ago'

def test_months_ago():
	assert (pretty_date(datetime.utcnow()-timedelta(weeks=12))) == '2 months ago'

def test_years_ago():
	assert (pretty_date(datetime.utcnow()-timedelta(weeks=260))) == '4 years ago'

