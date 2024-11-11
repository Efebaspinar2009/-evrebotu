import discord
from discord.ext import commands

import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# 1. Evde yapılabilecek plastik el işleri için fikirler
@bot.command(name="elisi_fikri")
async def elisi_fikri(ctx):
    ideas = [
        "Eski plastik şişelerden saksı yapabilirsiniz.",
        "Plastik kapaklardan küçük süs eşyaları yapabilirsiniz.",
        "Boş deterjan kutularını kullanarak saklama kutusu yapabilirsiniz.",
        "Plastik kaşık ve çatallardan dekoratif çerçeveler oluşturabilirsiniz."
    ]
    await ctx.send(f"İşte bir el işi fikri: {random.choice(ideas)}")

# 2. Atıkları ayırma rehberi
@bot.command(name="atık_ayırma")
async def atik_ayirma(ctx, item: str):
    recyclable_items = ["plastik şişe", "kağıt", "karton", "cam şişe", "metal kutu"]
    trash_items = ["kirli kağıt", "peçete", "süngertaşı", "plastik poşet"]

    if item.lower() in recyclable_items:
        await ctx.send(f"{item.capitalize()} geri dönüştürülebilir. Lütfen geri dönüşüm kutusuna atın.")
    elif item.lower() in trash_items:
        await ctx.send(f"{item.capitalize()} çöp kutusuna atılmalıdır.")
    else:
        await ctx.send(f"{item.capitalize()} hakkında bilgi mevcut değil.")

# 3. Ayrışma süresi bilgisi
@bot.command(name="ayrışma_süresi")
async def ayarisma_suresi(ctx, item: str):
    decomposition_times = {
        "plastik şişe": "450 yıl",
        "kağıt": "2-6 hafta",
        "cam şişe": "1 milyon yıl",
        "alüminyum kutu": "200-500 yıl",
        "muz kabuğu": "2-5 hafta"
    }

    time = decomposition_times.get(item.lower(), "Bu eşya hakkında bilgim yok.")
    await ctx.send(f"{item.capitalize()} doğada yaklaşık {time} sürede ayrışır.")



bot.run("TOKEN")
