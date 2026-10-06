from __future__ import annotations

import unittest

from support_bot import get_response


class GetResponseTests(unittest.TestCase):
    def test_returns_sample_order_status(self) -> None:
        self.assertIn("on its way", get_response("Where is order ORD-2048?"))

    def test_handles_unknown_order_number(self) -> None:
        response = get_response("Track order 9999")
        self.assertIn("couldn't find", response)
        self.assertIn("ORD-2048", response)

    def test_asks_for_order_number(self) -> None:
        self.assertIn("Send an order number", get_response("Where is my delivery?"))

    def test_explains_return_policy(self) -> None:
        self.assertIn("30 days", get_response("How do returns work?"))

    def test_payment_answer_warns_against_sharing_card_details(self) -> None:
        self.assertIn("Don't send full card details", get_response("I have a billing issue"))

    def test_unknown_question_offers_human_follow_up(self) -> None:
        self.assertIn("email", get_response("Can you help me with something unusual?"))

    def test_greeting_detection_matches_words_not_substrings(self) -> None:
        self.assertIn("Hello!", get_response("Hi there"))
        self.assertIn("email", get_response("Can you help me with something unusual?"))


if __name__ == "__main__":
    unittest.main()
