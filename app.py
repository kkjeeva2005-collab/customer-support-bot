"""A small, self-contained customer support chat demo built with Streamlit."""

from __future__ import annotations

import streamlit as st

from support_bot import get_response


st.set_page_config(
    page_title="Customer support",
    page_icon=":material/support_agent:",
    layout="wide",
)


def start_new_chat() -> None:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": (
                "Hi there! I'm your support assistant. I can help with orders, "
                "shipping, returns, payments, and more. What can I help you with?"
            ),
        }
    ]


def send_message(message: str) -> None:
    st.session_state["messages"].append({"role": "user", "content": message})
    st.session_state["messages"].append(
        {"role": "assistant", "content": get_response(message)}
    )


if "messages" not in st.session_state:
    start_new_chat()

with st.sidebar:
    st.markdown("## :material/support_agent: Support desk")
    st.caption("A ready-to-customize customer support demo")
    if st.button(
        "Start a new chat",
        icon=":material/add:",
        width="stretch",
        on_click=start_new_chat,
    ):
        pass

    st.space("medium")
    st.markdown("### Before you launch")
    st.info(
        "This demo uses example store policies and sample order numbers. "
        "Update `support_bot.py` with your own support information before "
        "sharing it with customers."
    )
    st.markdown("### Need a person?")
    st.write("Email **support@example.com** and include your order number.")
    st.caption("Example contact details — replace these with your own.")

st.title("How can we help?", icon=":material/chat:")
st.caption(
    "Ask a question in your own words, or choose a popular topic below. "
    "This sample bot works without an AI API key."
)

chat_column, details_column = st.columns([2.2, 1], gap="large")

with chat_column:
    with st.container(border=True):
        st.markdown("### :material/forum: Conversation")
        for message in st.session_state["messages"]:
            with st.chat_message(message["role"]):
                if message["role"] == "user":
                    st.text(message["content"])
                else:
                    st.markdown(message["content"])

    st.caption("Popular questions")
    suggestion_columns = st.columns(3)
    suggestions = (
        "Where is my order?",
        "What is your return policy?",
        "How can I contact support?",
    )
    for column, suggestion in zip(suggestion_columns, suggestions, strict=True):
        with column:
            st.button(
                suggestion,
                key=f"suggestion_{suggestion}",
                width="stretch",
                on_click=send_message,
                args=(suggestion,),
            )

    if prompt := st.chat_input("Type your message"):
        send_message(prompt)
        st.rerun()

with details_column:
    with st.container(border=True):
        st.markdown("### :material/bolt: Quick help")
        st.write("**Orders**")
        st.caption("Check a sample delivery status using its order number.")
        st.write("**Returns**")
        st.caption("See the example return and refund policy.")
        st.write("**Payments**")
        st.caption("Get help with common billing questions.")

    with st.container(border=True):
        st.markdown("### :material/schedule: Support hours")
        st.write("Monday–Friday, 9:00 AM–5:00 PM")
        st.caption("Example hours. Update them for your team and time zone.")
