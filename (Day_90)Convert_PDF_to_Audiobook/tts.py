#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


from google.cloud import texttospeech
import os


# authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = \
    r'/Users/whatthefuck/Downloads/dotted-howl-370604-0fea70f2962a.json'


def tts(text, output_path):

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open(output_path, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
