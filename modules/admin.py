import lib.cmd
import lib.events
import lib.irc
import settings
import sys


@lib.events.subscribe('invite')
def join_on_invite(bot=None, sender=None, channel=None):
    """If the bot owner invites the bot to a channel, it will join."""
    if sender.nick == settings.OWNER:
        bot.send(lib.irc.join(channel))


@lib.cmd.command()
def quit(msg):
    """Shuts down the bot. Only possible if you are the owner of the bot!"""
    if msg.sender != settings.OWNER:
        return 'I would love to but you are not my owner...'
    text = 'Goodbye :)'
    response = (lib.irc.say_to(msg.sender, text) if msg.private else
                lib.irc.say(msg.channel, text))
    msg.bot.send(response)
    msg.bot.disconnect()
    sys.exit()
