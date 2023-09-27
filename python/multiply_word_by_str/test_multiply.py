import unittest
from multiply_word import modify_multiply


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(
            modify_multiply("This is a string", 3, 5),
            "string-string-string-string-string",
            "The string is incorrect",
        )
        self.assertEqual(
            modify_multiply(
                "Creativity is the process of having original ideas that have value. It is a process; it's not random.",
                8,
                10,
            ),
            "that-that-that-that-that-that-that-that-that-that",
        )
        self.assertEqual(
            modify_multiply(
                "Self-control means wanting to be effective at some random point in the infinite radiations of my spiritual existence",
                1,
                1,
            ),
            "means",
        )
        self.assertEqual(
            modify_multiply(
                "Is sloppiness in code caused by ignorance or apathy? I don't know and I don't care.",
                6,
                8,
            ),
            "ignorance-ignorance-ignorance-ignorance-ignorance-ignorance-ignorance-ignorance",
        )
        self.assertEqual(
            modify_multiply(
                "Everything happening around me is very random. I am enjoying the phase, as the journey is far more enjoyable than the destination.",
                2,
                5,
            ),
            "around-around-around-around-around",
        )


if __name__ == "__main__":
    unittest.main()
