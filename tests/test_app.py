# Import the necessary modules
from flask import url_for
from flask_testing import TestCase
import unittest

# import the app's classes and objects
from application import app, db
from application.models import Songs, Playlist

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='mister11',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()
        # Create test registree
        sample1 = Songs(title="Gimmie More", artist="Brittney Spears", feature="JT", category="Pop", reldate='2005-08-19', length='00:03:45')
        sample2 = Playlist(sg_num = 1, sg_title = 'Gimmie More', pl_name = 'Pop Music', count = 0)
        # save users to database
        db.session.add(sample1)
        db.session.add(sample2)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()
        
# Write a test class to test Read functionality
class TestViews(TestBase):
    def test_add_songs(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b'Gimmie More', response.data)

    def test_delete_songs(self):
        response = self.client.get(url_for('delete', id=1))
        follow_redirects=True
        self.assertNotIn(b'Gimmie More', response.data)

    def test_update_songs(self):
        response = self.client.post('update/1', 
        data=dict(
            title='ntitle',
            artist='nartist',
            feature='nfeature',
            category='ncategory',
            reldate='nreldate',
            length='nlength',
            otitle='title',
            oartist='artist',
            ofeature='feature',
            ocategory='category',
            oreldate='reldate',
            olength='length'
        ), 
        follow_redirects=True)
        self.assertIn(b'ntitle', response.data)
        self.assertIn(b'nartist', response.data)

    def test_view_songs(self):
        response = self.client.get(url_for('songs'))
        self.assertIn(b'Gimmie More', response.data)

    def test_add_pl(self):
        response = self.client.get(url_for('add_pl'))
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_all_pl(self):
        response = self.client.get(url_for('allplaylists'))
        self.assertIn(b'Gimmie More', response.data)

    def test_filter_pl(self):
        response = self.client.get(url_for('playlists'))
        self.assertNotIn(b'vfdgsg', response.data)