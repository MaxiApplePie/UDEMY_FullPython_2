from main import add


def test_add_two_numbers():
    assert add(5, 12) == 17

    # def test_add_two_booleans(self):
    #     self.assertEqual(add(True, False), 1)
    #     self.assertEqual(add(True, True), 2)
    #     self.assertEqual(add(False, True), 1)
    #
    # def test_add_two_nones(self):
    #     with self.assertRaises(TypeError):
    #         add(None, None)
