from django.test import TestCase
from Responses.models import Responses,UserMetadata,RespondMetadata

class ResponsesTests(TestCase):
    def test_parse_from_csv_data(self):
        data = """409;6;Magda;174;The Manchurian Candidate;-1
410;6;Magda;194;There Will Be Blood;-1
411;6;Magda;35;Die Hard;-1
412;7;Ewa;7;Alien;3
411;6;Magda;32;AAaa;71
"""
        new_responds, new_users = Responses.parse_from_csv_data(data)
        self.assertEqual(len(new_users), 2)
        self.assertEqual(new_users[0].user_id, 6)
        self.assertEqual(new_users[0].user_name, "Magda")
        self.assertEqual(new_users[1].user_id, 7)
        self.assertEqual(new_users[1].user_name, "Ewa")
        self.assertEqual(len(new_responds), 5)
        self.assertEqual(new_responds[0].respond_id, 1)
        self.assertEqual(new_responds[0].movie_id, 174)
        self.assertEqual(new_responds[0].user_id, 6)
        self.assertEqual(new_responds[0].user_rate, -1)
        self.assertEqual(new_responds[3].respond_id, 4)
        self.assertEqual(new_responds[3].movie_id, 7)
        self.assertEqual(new_responds[3].user_id, 7)
        self.assertEqual(new_responds[3].user_rate, 4)

    def test_parse_from_csv_data2(self):
        data = """respond_id;user_id;user_name;movie_id;movie_title;user_rate
409;6;Magda;174;The Manchurian Candidate;-1
410;6;Magda;194;There Will Be Blood;-1
411;6;Magda;35;Die Hard;-1
412;7;Ewa;7;Alien;3
411;6;Magda;32;AAaa;71
"""
        new_responds, new_users = Responses.parse_from_csv_data(data)
        self.assertEqual(len(new_users), 2)
        self.assertEqual(new_users[0].user_id, 6)
        self.assertEqual(new_users[0].user_name, "Magda")
        self.assertEqual(new_users[1].user_id, 7)
        self.assertEqual(new_users[1].user_name, "Ewa")
        self.assertEqual(len(new_responds), 5)
        self.assertEqual(new_responds[0].respond_id, 1)
        self.assertEqual(new_responds[0].movie_id, 174)
        self.assertEqual(new_responds[0].user_id, 6)
        self.assertEqual(new_responds[0].user_rate, -1)
        self.assertEqual(new_responds[3].respond_id, 4)
        self.assertEqual(new_responds[3].movie_id, 7)
        self.assertEqual(new_responds[3].user_id, 7)
        self.assertEqual(new_responds[3].user_rate, 4)
