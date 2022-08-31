from KazukoBot.sample_config import Config

class Development(Config):
    OWNER_ID = 5136746907  # your telegram ID
    OWNER_USERNAME = "sadrobo"  # your telegram username
    API_KEY = "5397538082:AAFyZdcyT-C8SxVaybpNZcpBuxGfBQvtoVg"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://fzbxklpm:UJDo18ordGuj6jQQvaMR6NdBzl-jpFH_@jelani.db.elephantsql.com/fzbxklpm'  # sample db credentials
    JOIN_LOGGER = '-1234567890' # some group chat that your bot is a member of
    USE_JOIN_LOGGER = True
    DRAGONS = [18673980, 5136746907]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
