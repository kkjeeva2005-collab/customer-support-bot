# Customer support chatbot

A small Streamlit customer support demo with a chat interface, sample FAQs,
example order tracking, and a responsive contact fallback. It uses a local
rule-based knowledge base, so it runs without an AI provider or API key.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

## Customize before publishing

Edit `support_bot.py` to replace the sample return policy, support email, and
order statuses with verified business information. The sample order numbers
are illustrative only; this demo does not connect to a live order system.
Keep customer data and credentials out of the source code. To add an AI
provider or a live order API, store credentials in Streamlit secrets and
connect only to systems authorized for your business.

Run the built-in tests with:

```powershell
python -m unittest
```
