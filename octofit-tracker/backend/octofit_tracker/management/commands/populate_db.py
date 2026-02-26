from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        marvel_members = ['Iron Man', 'Spider-Man', 'Captain Marvel']
        dc_members = ['Superman', 'Batman', 'Wonder Woman']

        Team.objects.create(name='marvel', members=marvel_members)
        Team.objects.create(name='dc', members=dc_members)

        User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel')
        User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel')
        User.objects.create(email='superman@dc.com', name='Superman', team='dc')
        User.objects.create(email='batman@dc.com', name='Batman', team='dc')

        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2026-02-26')
        Activity.objects.create(user='Spider-Man', type='jump', duration=15, date='2026-02-25')
        Activity.objects.create(user='Superman', type='fly', duration=60, date='2026-02-24')
        Activity.objects.create(user='Batman', type='fight', duration=45, date='2026-02-23')

        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        Workout.objects.create(name='Pushups', description='Do pushups', suggested_for='marvel')
        Workout.objects.create(name='Flight', description='Fly for 1 hour', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
