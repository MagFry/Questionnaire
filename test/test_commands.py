def test_command_delete_movies(host):
    cmd = host.run('python manage.py delete_movies')
    assert cmd.succeeded
    assert 'Successfully deleted all movies from db' in cmd.stdout.rstrip()

def test_command_populate_db(host):
    cmd = host.run('python manage.py delete_movies && PIIS_TEST=true python manage.py populate_db')
    assert cmd.succeeded
    assert '12 Angry Men' in cmd.stdout.rstrip()
    assert 'Successfully added all movies to db' in cmd.stdout.rstrip()
    # clean after test
    cmd = host.run('python manage.py delete_movies')
