from selenium import webdriver
from flask_testing import LiveServerTestCase
from application import app, db



# Create the base class
class TestBase(LiveServerTestCase):
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
    def test_filter_pl(self):
        self.driver.get(f'http://35.189.93.228:5000/playlists')
        

