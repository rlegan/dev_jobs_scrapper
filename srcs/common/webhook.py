from discord_webhook import DiscordWebhook, DiscordEmbed
from common.constants import DISCORD_WEBHOOK


def create_embed(job_name, job_company, job_location, job_link, job_thumbnail):
    """
    Create a discord embed object from the
    data of a Station F job listing.
    """

    embed = DiscordEmbed(title='🛎 NEW JOB FOUND ! 🛎')
    embed.set_description(job_name)
    embed.set_url(job_link)
    embed.add_embed_field(name='Company', value='🏢 {}'.format(job_company))
    embed.add_embed_field(name='Location', value='📍 {}'.format(job_location))
    embed.set_thumbnail(url=job_thumbnail)
    return embed


def send_embed(embed, website):
    """
    Send an embed to the webhook specified in the .env file.
    """

    webhook = DiscordWebhook(url=DISCORD_WEBHOOK, username=website.discord_username,
                             avatar_url=website.discord_avatar_url)

    webhook.add_embed(embed)
    response = webhook.execute()
    if (response.status_code == 404):
        print('Couldn\'t send the embed to the webhook ' + DISCORD_WEBHOOK)
