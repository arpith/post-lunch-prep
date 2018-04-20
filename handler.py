import json
import os
import zulip


def send_message(message):
    client = zulip.Client(
        site="https://recurse.zulipchat.com",
        email=os.environ["email"],
        api_key=os.environ["api_key"]
    )

    request = {
        "type": "stream",
        "to": "455 Broadway",
        "subject": "Post-lunch Prep!",
        "content": message
        # "type": "private",
        # "to": "sean.rankine@me.com",
        # "content": message
    }
    result = client.send_message(request)
    print(result)


def test(event, context):
    send_message("Hi, I'm PrepBot (kinda like SwoleBot but for your brain.)")


def pre_announce(event, context):
    additional_link = " and [here]({link})".format(
        link=os.environ["additional_link"]) if os.environ.get("additional_link") else ""

    send_message("""
Hi @*Currently at RC*

Today's topic will be {topic}!

Today's resource on our topic can be found [here]({link}){additional_link}. Please do give it a read through if you'd like to refresh your understanding and see some code samples!

The questions will be projected in the Mainspace from 1:45 PM to 2:45 PM. The leftmost question will tend to be more introductory, while the rightmost question will typically have a more involved implementation.
""".format(topic=os.environ["topic"], link=os.environ["link"], additional_link=additional_link))


def announce(event, context):
    send_message("""
For those following along, today's questions are:

1) {easy_link}
2) {hard_link}

If you're interested in pairing come to the projector in the main space and we'll see if we can match you up :)

Please feel free to join us in Turing @ 2:45 PM for our discussion! {name} will be running today's session.
    """.format(easy_link=os.environ["easylink"], hard_link=os.environ["hardlink"], name=os.environ["person"]))


def post_announce(event, context):
    send_message("""
Our post-lunch prep discussion will be in Turing in 10 minutes!

Please come join regardless of whether you have completed, or even attempted, the questions :)

If you have a solution you would like to present or discuss, send it over via PM.
""")
