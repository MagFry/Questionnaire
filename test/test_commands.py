def test_command_delete_movies(host):
    cmd = host.run('python manage.py delete_movies')
    assert cmd.succeeded
    assert 'Successfully deleted all movies from db' in cmd.stdout.rstrip()
    # this is a poster file for the 1st movie (12 Angry Men)
    assert not host.file('media/3W0v956XxSG5xgm7LB6qu8ExYJ2.jpg').exists

def test_command_populate_db(host):
    cmd = host.run('python manage.py delete_movies && PIIS_TEST=true python manage.py populate_db')
    assert cmd.succeeded
    assert '12 Angry Men' in cmd.stdout.rstrip()
    assert 'Successfully added all movies to db' in cmd.stdout.rstrip()
    assert host.file('media/3W0v956XxSG5xgm7LB6qu8ExYJ2.jpg').exists
    # clean after test
    cmd = host.run('python manage.py delete_movies')
    # this is a poster file for the 1st movie (12 Angry Men)
    assert not host.file('media/3W0v956XxSG5xgm7LB6qu8ExYJ2.jpg').exists
