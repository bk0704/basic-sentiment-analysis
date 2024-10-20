import discord
from discord.ext import commands
import dotenv
import os
import sentiment_analysis
from sentiment_analysis import analyze_sentiment
from utils import aggregate_sentiment

dotenv.load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

client = commands.Bot(command_prefix='!', intents=intents)
tree = client.tree

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

    try:
        await tree.sync()
        print('All commands synced')

    except Exception as e:
        print(f'Failed to sync commands: {e}')

@tree.command(name='sentiment', description='Analyze the sentiment of the last 100 messages in the channel')
async def sentiment(ctx):
    # Fetch the last 1000 messages in the current channel
    messages = []
    async for msg in ctx.channel.history(limit=100):
        messages.append(msg)

    # Perform sentiment analysis on the messages
    sentiment_scores = [analyze_sentiment(msg.content) for msg in messages]

    # Aggregate the sentiment scores
    overall_sentiment = aggregate_sentiment(sentiment_scores)

    # Categorize the overall sentiment score as positive, neutral, or negative
    if overall_sentiment > 0.05:
        sentiment_label = "positive 😊"
    elif overall_sentiment < -0.05:
        sentiment_label = "negative 😔"
    else:
        sentiment_label = "neutral 😐"

    # Respond with the overall sentiment score
    await ctx.response.send_message(f'The overall sentiment of the last 100 messages is: {sentiment_label} with a score of {overall_sentiment:.2f}')

client.run(token)