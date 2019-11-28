def test_command_delete_movies(host):
    cmd = host.run('python manage.py delete_movies --media-dir=test/media')
    assert cmd.succeeded
    assert 'Successfully deleted all movies from db' in cmd.stdout.rstrip()
    # this is a poster file for the 1st movie (12 Angry Men)
    assert not host.file('test/media/389.jpg').exists

def test_command_populate_db(host):
    cmd = host.run('python manage.py delete_movies --media-dir=test/media && PIIS_TEST=true python manage.py populate_db --media-dir=test/media')
    assert cmd.succeeded
    assert '12 Angry Men' in cmd.stdout.rstrip()
    assert 'Successfully added all movies to db' in cmd.stdout.rstrip()
    assert host.file('test/media/389.jpg').exists
    # clean after test
    cmd = host.run('python manage.py delete_movies --media-dir=test/media')
    # this is a poster file for the 1st movie (12 Angry Men)
    assert not host.file('test/media/389.jpg').exists

def test_command_delete_users(host):
    cmd = host.run('python manage.py delete_users')
    assert cmd.succeeded
    assert 'Successfully deleted all users from db' in cmd.stdout.rstrip()

def test_command_list_users(host):
    cmd = host.run('python manage.py list_users')
    assert cmd.succeeded
