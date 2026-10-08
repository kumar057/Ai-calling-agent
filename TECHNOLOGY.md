# Technology

Source: CONTEXT.md and owner instruction in the current M0 request.

## Fixed Stack

- Python
- Streamlit for the staff console
- FastAPI for the trusted backend
- LiveKit for voice in a later milestone

## Not Selected

- Database provider or engine for production
- LLM provider
- Speech/transcription/text-to-speech provider
- Telephony provider
- Identity provider

## Current Rules

- Do not silently choose paid providers.
- Use mock/synthetic data and mock telephony by default.
- Real calling must fail closed unless explicitly approved.
- Provider secrets stay server-side and out of UI/debug output.
- `.env.example` may document configuration keys, but real secrets must not be
  printed or committed.
