"""Example support content and deterministic message handling."""

from __future__ import annotations

import re


DEMO_ORDERS = {
    "2048": "Your order is on its way and is expected to arrive in 2–3 business days.",
    "3106": "Your order is being prepared. We'll email you when it ships.",
    "4821": "Your order was delivered. If you can't find it, check around your "
    "delivery area or contact support@example.com.",
}

RETURN_POLICY = (
    "Our example return policy accepts unused items within 30 days of delivery. "
    "Refunds are issued to the original payment method after the return is "
    "received and inspected. Replace this sample policy with your actual terms."
)

_ORDER_ID = re.compile(r"\b(?:order\s*)?(?:ord[-\s#]*)?(\d{4})\b", re.IGNORECASE)


def _has_any(text: str, phrases: tuple[str, ...]) -> bool:
    return any(
        re.search(rf"\b{re.escape(phrase)}\b", text)
        for phrase in phrases
    )


def get_response(message: str) -> str:
    """Return a concise response based on the sample support knowledge base."""
    text = " ".join(message.lower().split())
    if not text:
        return "Please tell me a little more about what you need help with."

    order_match = _ORDER_ID.search(message)
    if order_match:
        order_status = DEMO_ORDERS.get(order_match.group(1))
        if order_status:
            return f"**Order #{order_match.group(1)}:** {order_status}"
        return (
            "I couldn't find that in the sample order list. Try **ORD-2048**, "
            "**ORD-3106**, or **ORD-4821**, or contact support@example.com for "
            "help with a real order."
        )

    if _has_any(text, ("track", "tracking", "order", "delivery", "shipped")):
        return (
            "I can check a sample delivery status. Send an order number such as "
            "**ORD-2048**, **ORD-3106**, or **ORD-4821**. These are demo orders, "
            "not live customer data."
        )

    if _has_any(text, ("return", "returns", "refund", "refunds", "exchange")):
        return RETURN_POLICY

    if _has_any(text, ("cancel", "change", "edit address", "update address")):
        return (
            "If an order hasn't shipped yet, our example policy is to contact "
            "support@example.com as soon as possible. Include your order number; "
            "changes aren't guaranteed after dispatch."
        )

    if _has_any(text, ("payment", "billing", "charged", "charge", "card")):
        return (
            "For a declined payment, check that your billing details are correct "
            "or try another payment method. For an unfamiliar charge, email "
            "support@example.com with the date and amount. Don't send full card "
            "details in chat."
        )

    if _has_any(text, ("human", "agent", "contact", "email", "person", "support")):
        return (
            "You can reach the sample support team at **support@example.com**. "
            "Include your order number if you have one. Replace this demo address "
            "with your real support contact."
        )

    if _has_any(text, ("hours", "open", "time")):
        return "The sample support hours are Monday–Friday, 9:00 AM–5:00 PM. Update this with your team's hours and time zone."

    if _has_any(text, ("hello", "hi", "hey", "good morning", "good afternoon")):
        return (
            "Hello! I can help with order tracking, returns, payments, and "
            "contacting support. What would you like to know?"
        )

    return (
        "I don't have an answer for that yet. I can help with orders, returns, "
        "payments, or support hours. For anything else, email "
        "**support@example.com** and a person can take a look."
    )
